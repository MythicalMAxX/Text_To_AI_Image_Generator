from huggingface_hub import notebook_login

notebook_login()

import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)

pipe = pipe.to("cuda")

from sys import exit

def prompt():
  try:
    prompt = input("Enter your Prompt:")
    if prompt == "":
      print("Prompt can't be empty")
      exit
    else:
      return prompt
  except:
    print("An unidentical Error occoured")
    exit()



def ImageCount():
  try:
    Total_images = int(input("Enter total number of Images:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return Total_images

Prompt = prompt()
Total_images = ImageCount()



def Generate_multiple(num,prompt):
    for i in range(num):
        image = pipe(prompt).images[0]
        image.save(f"image.png")

Generate_multiple(Total_images,Prompt)
