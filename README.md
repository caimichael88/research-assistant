# Research Assistant

This is a simple research assistant application that extracts text from PDF files and generates a summary using a transformer-based language model.

## Features
- Extracts text from PDF documents
- Summarizes extracted text using Hugging Face Transformers
- Outputs the summary to a JSON file

## Requirements
- Python 3.7+
- PyMuPDF (`fitz`)
- transformers
- torch

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
Run the application from the command line:
```bash
python main.py [path_to_pdf]
```
- If no PDF path is provided, it defaults to `pdf/sample.pdf`.
- The summary will be saved to `output/summary.json`.

## Project Structure
- `main.py` - Main entry point
- `pdf/extract_text.py` - PDF text extraction logic
- `llm/summarize.py` - Summarization logic using transformers
- `output/` - Output directory for summaries

## License
MIT 