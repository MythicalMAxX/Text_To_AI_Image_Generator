from huggingface_hub import notebook_login

notebook_login()

import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)

pipe = pipe.to("cuda")

Prompt = "realistic mango fruit, ripened purple fruit, delicious, photo realistic, 4k, sharp focus in unreal engine 5, ultra detailed, cinematic, artstationcoding, unreal engine 5, octane renderisometricis"

image = pipe(Prompt, height=102, width=768).images[0]
image.save(f"image.png")
