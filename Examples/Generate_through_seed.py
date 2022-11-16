from huggingface_hub import notebook_login

notebook_login()

import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)

pipe = pipe.to("cuda")


def Generate_through_seed(Prompt,Seed_number):
  generator = torch.Generator("cuda").manual_seed(Seed_number)
  image = pipe(Prompt, generator=generator).images[0]
  return image


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

def SeedInput():
  try:
    seed = int(input("Enter a Seed:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return seed


Prompt = prompt()
Seed_number = SeedInput()
image = Generate_through_seed(Prompt,Seed_number)
image.save(f"image.png")
