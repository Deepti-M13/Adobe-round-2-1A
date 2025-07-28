import fitz  # PyMuPDF
import json
import os

# Thresholds to decide heading levels
H1_THRESHOLD = 17
H2_THRESHOLD = 14
H3_THRESHOLD = 11

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get('title', '') or "Untitled"
    outline = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                text = ""
                font_sizes = []

                for span in line["spans"]:
                    text += span["text"].strip() + " "
                    font_sizes.append(span["size"])

                text = text.strip()
                if not text:
                    continue

                font_size = max(font_sizes)

                # Decide heading level based on font size
                if font_size >= H1_THRESHOLD:
                    level = "H1"
                elif font_size >= H2_THRESHOLD:
                    level = "H2"
                elif font_size >= H3_THRESHOLD:
                    level = "H3"
                else:
                    continue  # skip body text

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {"title": title, "outline": outline}

def main():
    input_dir = '/app/input'
    output_dir = '/app/output'

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            outline = extract_outline(pdf_path)
            json_filename = os.path.splitext(filename)[0] + '.json'
            json_path = os.path.join(output_dir, json_filename)

            with open(json_path, 'w') as json_file:
                json.dump(outline, json_file, indent=4)

if __name__ == "__main__":
    main()
