
Built by https://www.blackbox.ai

---

```markdown
# PDF to JSON Converter

## Project Overview

The **PDF to JSON Converter** is a web application that allows users to convert PDF documents containing text, images, and numbers into a structured JSON format. Built with Node.js and FastAPI, the application can handle large PDF files and extracts text and images efficiently.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-to-json-converter.git
   cd pdf-to-json-converter
   ```

2. **Install the necessary dependencies:**
   You need Node.js and Python installed on your system. Then install the required dependencies:

   **For Node.js backend:**
   ```bash
   npm install
   ```

   **For FastAPI:**
   ```bash
   pip install fastapi[all] PyMuPDF
   ```

3. **Prepare the uploads and static directories:**
   For PDF uploads and image storage, ensure the following directories exist:
   ```bash
   mkdir uploads
   mkdir static/images
   ```

## Usage

1. **Start the Node.js server:**
   ```bash
   npm start
   ```
   This will start the server on port 3000 by default.

2. **Run the FastAPI server:**
   You can use the provided `main.py` to run the FastAPI application.
   ```bash
   uvicorn main:app --reload
   ```

3. **API Endpoint for PDF Conversion:**
   - **POST** `/api/convert` - Upload your PDF file to convert it to JSON format.
   - Example using `curl`:
     ```bash
     curl -F "file=@path_to_your_pdf.pdf" http://localhost:3000/api/convert
     ```

## Features

- Convert PDF files to JSON format while extracting text, metadata, and images.
- Support for large PDF files.
- Basic validation for uploaded files to ensure they are PDFs.
- An easily accessible API endpoint for integrating with other systems or applications.

## Dependencies

The project relies on the following packages:

- **Node.js dependencies:**
  - [express](https://www.npmjs.com/package/express) - A minimal and flexible Node.js web application framework.
  - [multer](https://www.npmjs.com/package/multer) - Middleware for handling multipart/form-data, used for uploading files.
  - [pdf-parse](https://www.npmjs.com/package/pdf-parse) - A library for extracting text and metadata from PDF files.
  - [cors](https://www.npmjs.com/package/cors) - Middleware for enabling CORS (Cross-Origin Resource Sharing).

- **Python dependencies:**
  - [fastapi](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs with Python 3.7+ based on standard Python type hints.
  - [fitz (PyMuPDF)](https://pymupdf.readthedocs.io/en/latest/) - A Python binding for MuPDF, a lightweight PDF and XPS viewer.

## Project Structure

The project directory structure is organized as follows:

```
pdf-to-json-converter/
├── uploads/              # Folder for storing uploaded PDF files
├── static/               # Static files directory for serving images
│   └── images/           # Folder for extracted images from PDF
├── node_modules/         # Node.js dependencies
├── main.py               # FastAPI application for PDF processing
├── package.json          # Node.js project metadata and dependencies
└── server.js             # Node.js server entry point
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for enhancements or bug fixes.

## License

This project is licensed under the MIT License.
```