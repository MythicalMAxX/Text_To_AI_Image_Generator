from huggingface_hub import notebook_login

notebook_login()

import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)

pipe = pipe.to("cuda")

def Inference():
  try:
    infer = int(input("Enter Inference steps(Int):"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return infer


def SeedInput():
  try:
    seed = int(input("Enter a Seed:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return seed

def GuidanceValue():
  try:
    guidance = float(input("Enter value for guidance scale\n Recommended Int Range 7-9:"))
  except ValueError:
      print("Try using Float Value next time")
      exit()
  return guidance

def Generate_with_guidancevalue(Prompt,seed_number,guidance_scale):
  generator = torch.Generator("cuda").manual_seed(seed_number)
  image = pipe(Prompt, num_inference_steps=50, guidance_scale = guidance_scale, generator=generator).images[0]
  return image

inference_steps = Inference()
guidance_scale = GuidanceValue()
seed_number = SeedInput()
image = Generate_with_guidancevalue(Prompt,seed_number,guidance_scale)
image.save(f"image.png")
