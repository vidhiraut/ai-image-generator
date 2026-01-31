print("RUNNING FILE:", __file__)
import json
import os
from PIL import Image, ImageDraw

# ensure images folder exists
os.makedirs("images", exist_ok=True)

# load product data
with open("data/products.json") as f:
    products = json.load(f)

# load prompt template
with open("prompts/product_prompt.txt") as f:
    prompt_template = f.read()

for product in products:
    prompt = prompt_template.format(
        product_name=product["name"],
        brand=product["brand"]
    )

    print(f"Generating LOCAL image for {product['name']}...")

    # create a simple placeholder image
    img = Image.new("RGB", (512, 512), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)

    text = f"{product['name']}\nBrand: {product['brand']}\n\n{prompt}"

    draw.multiline_text(
        (40, 200),
        text,
        fill=(0, 0, 0),
        spacing=10
    )

    img.save(f"images/{product['product_id']}.png")

    print("Saved image.")

