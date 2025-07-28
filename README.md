# 📘 Round 1A – Structural PDF Outline Extractor
**Adobe India Hackathon 2025**  
Challenge Theme: *Connecting the Dots Through Docs*

---

## 🧠 Problem Statement

You're handed a PDF, but instead of simply reading it, you're tasked with making sense of it *like a machine would*.  
Build a solution that extracts a structured outline from the document – **title**, **headings (H1, H2, H3)** – in a clean, hierarchical JSON format.

---

## 🎯 What This Solution Does

This extractor:
- Accepts one or more PDF files (max 50 pages each) placed in `/app/input`
- Identifies:
  - `Title` of the document
  - Section headings (with levels: `H1`, `H2`, `H3`)
  - Page numbers for each heading
- Outputs a valid JSON file per PDF in the format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
