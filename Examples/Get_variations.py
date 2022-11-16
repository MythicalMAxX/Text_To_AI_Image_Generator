from diffusers import StableDiffusionImg2ImgPipeline
import torch
from torch import autocast
device = "cuda"
model_path = "CompVis/stable-diffusion-v1-4"

pipe1 = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_path,
    revision="fp16", 
    torch_dtype=torch.float16,
    use_auth_token=True
)
pipe1 = pipe1.to(device)

def Generate_with_inference(Prompt,Inference_steps):
  image1 = pipe(Prompt, num_inference_steps=50).images[0]

  image1.save(f"image.png")
  display(image1)
  return image1

def Inference():
  try:
    infer = int(input("Enter Inference steps(Int):"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return infer

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
    
def New_prompt():
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

def Generate_with_autocast(new_prompt,strength,guidance_scale,image = image1):

  generator = torch.Generator(device=device).manual_seed(0)
  with autocast("cuda"):
      image2 = pipe1(prompt=new_prompt, init_image=image, strength=strength, guidance_scale=guidance_scale, generator=generator).images[0]
      return image2

def GuidanceValue():
  try:
    guidance = float(input("Enter value for guidance scale\n Recommended Float Range 7-9:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return guidance

def Strength():
  try:
    strength = float(input("Enter value for guidance scale\n Recommended Float Range 0.5-1:"))
  except ValueError:
      print("Try using Integer next time")
      exit()
  return strength


prompt = prompt()
inference_steps = Inference()
image1 = Generate_with_inference(prompt,inference_steps)

guidance_scale = GuidanceValue()
strength = Strength()
new_prompt = New_prompt()
image2 = Generate_with_autocast(new_prompt,strength,guidance_scale)
image2.save(f"variation.png")
