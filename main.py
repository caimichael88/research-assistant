from pdf.extract_text import extract_text_from_pdf
from llm.summarize import summarize
import json
import sys


def run(pdf_path: str):
    text = extract_text_from_pdf(pdf_path)
    summary = summarize(text)
    result = {
        "source_file": pdf_path,
        "summary": summary,
    }
    output_path = "output/summary.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"summary written to {output_path}")


if __name__ == "__main__":
    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "data/sample.pdf"
    run(pdf_file)