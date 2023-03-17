from diffusers import StableDiffusionPipeline
import torch
import time

if False:
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

    prompt = "a photograph of an astronaut riding a horse"

    print(prompt)
    t0 = time.time()
    image = pipe(prompt).images[0]
    print(f"Finish in {time.time() - t0:.2f}s")

    # you can save the image with
    image.save(f"astronaut_rides_horse.png")


# make sure you're logged in with `huggingface-cli login`
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("mps")

# Recommended if your computer has < 64 GB of RAM
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
image = pipe(prompt).images[0]
image.save(f"astronaut_rides_horse_on_mars.png")
