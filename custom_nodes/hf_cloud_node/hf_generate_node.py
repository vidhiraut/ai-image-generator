import requests
import os
from datetime import datetime

class HFCloudGenerate:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "modern motel at night, cinematic lighting"})
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "generate"
    OUTPUT_NODE = True
    CATEGORY = "HuggingFace"

    def generate(self, prompt):

        API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-2-1"

        headers = {
                 "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
                 "Content-Type": "application/json"
         }


        data = {"inputs": prompt}

        response = requests.post(API_URL, headers=headers, json=data)

        print("Status:", response.status_code)
        print("Response:", response.text[:300])

        if response.status_code != 200:
            return ()

        filename = f"hf_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        output_folder = os.path.join(os.getcwd(), "output")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with open(os.path.join(output_folder, filename), "wb") as f:
            f.write(response.content)

        print(f"Saved image: {filename}")

        return ()


NODE_CLASS_MAPPINGS = {
    "HFCloudGenerate": HFCloudGenerate
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HFCloudGenerate": "HFCloudGenerate"
}
