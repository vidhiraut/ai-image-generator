# AI Product Image Generator

Generate clean, eCommerce-ready product images using AI — fully automated from structured product data.

This project demonstrates a real-world image generation pipeline similar to what eCommerce and marketing teams use to scale product visuals.

---

## ✨ Features

- Automated product image generation from JSON data
- Prompt templating for consistent brand style
- Multiple visual styles (minimalist, lifestyle, detail focus)
- Local image generation fallback (no heavy model downloads)
- Clean, GitHub-safe setup (no secrets committed)

---

## 📂 Project Structure

ai-image-generator/
│
├── data/
│ └── products.json # Product metadata
│
├── prompts/
│ └── product_prompt.txt # Prompt template
│
├── images/
│ └── P001.png # Generated sample output
│
├── generate_images.py # Main pipeline
├── .gitignore
└── README.md


---

## 🧠 How It Works

1. Products are defined in `products.json`
2. Prompts are dynamically generated using placeholders
3. The pipeline generates images per product
4. Output images are saved automatically

This simulates how large catalogs can generate visuals at scale.

---

## ▶️ Run Locally

python generate_images.py
Generated images will appear in the images/ folder.

🛠 Tech Stack
Python
Prompt templating
Local image rendering
JSON-based data pipelines

📌 Why This Project Matters
This project focuses on automation, scalability, and practical constraints:
Handles API limitations
Avoids large local model downloads
Designed like a real production tool
It reflects how AI is applied in eCommerce, marketing, and creative tech.

📷 Sample Output
