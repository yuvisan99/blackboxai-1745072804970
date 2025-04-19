from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import fitz  # PyMuPDF
import os
import uuid
import shutil

app = FastAPI()

# Create directory for uploaded PDFs and extracted images
UPLOAD_DIR = "uploads"
IMAGE_DIR = "static/images"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

def extract_pdf_to_json(pdf_path: str):
    doc = fitz.open(pdf_path)
    pdf_json = {
        "metadata": doc.metadata,
        "page_count": doc.page_count,
        "pages": []
    }

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        page_dict = {
            "page_number": page_num + 1,
            "text": page.get_text("text"),
            "blocks": [],
            "images": []
        }

        # Extract blocks (text, images, etc)
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            block_type = block["type"]
            if block_type == 0:  # text block
                page_dict["blocks"].append({
                    "type": "text",
                    "bbox": block["bbox"],
                    "text": block.get("text", "")
                })
            elif block_type == 1:  # image block
                # Extract image
                for image in block.get("images", []):
                    xref = image["xref"]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    image_id = str(uuid.uuid4())
                    image_filename = f"{image_id}.{image_ext}"
                    image_path = os.path.join(IMAGE_DIR, image_filename)
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    page_dict["images"].append({
                        "xref": xref,
                        "image_url": f"/static/images/{image_filename}",
                        "bbox": block["bbox"]
                    })
            else:
                # Other block types can be added if needed
                pass

        pdf_json["pages"].append(page_dict)

    return pdf_json

@app.post("/api/convert")
async def convert_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")

    file_id = str(uuid.uuid4())
    pdf_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = extract_pdf_to_json(pdf_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {str(e)}")
    finally:
        # Clean up uploaded PDF file
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    return JSONResponse(content=result)
