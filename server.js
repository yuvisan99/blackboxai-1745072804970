const express = require('express');
const multer = require('multer');
const pdfParse = require('pdf-parse');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());
app.use(express.static('public'));

app.post('/api/convert', upload.single('pdf'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No PDF file uploaded' });
  }

  try {
    const dataBuffer = fs.readFileSync(req.file.path);
    const data = await pdfParse(dataBuffer);

    // Basic JSON structure with text and metadata
    const result = {
      numpages: data.numpages,
      numrender: data.numrender,
      info: data.info,
      metadata: data.metadata,
      text: data.text,
      // images extraction is not supported by pdf-parse, so images will be omitted here
      // For images, a more advanced library or approach is needed
    };

    // Delete the uploaded file after processing
    fs.unlinkSync(req.file.path);

    res.json(result);
  } catch (error) {
    res.status(500).json({ error: 'Failed to process PDF', details: error.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
