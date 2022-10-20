import requests
import os
from datetime import date
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt


'''torch.device("mps")
device = "cuda" if torch.cuda.is_available() else "cpu"


#could modify image seize here https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/ eventually 

#print(torch.cuda.is_available())

#this takes years till this is updated. if i am done. what do i wanna do? I could create a galaxy prompt or i could do a bay area prompt. only works if generated image is not always the same with same prompt.
#need to check that.

model_id = "CompVis/stable-diffusion-v1-4"
#device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
pipe = pipe.to(device)

#Silicon Valley in a technopunk scenario. 
#Galaxy 

prompt = "Galaxy"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5).images[0]  
    
image.save("astronaut_rides_horse2.png")'''



'''url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


def getFilename():
    r = requests.get(url)
    path = "/Users/maxhager/Projects2022/PythonWorkflowScripts/BackgroundImage/backgroundImage/"
    titleUrl = r.json()['title'].replace(" ", "")
    filename = path + titleUrl + ".png"
    return filename


def downloadImageToday():
    r = requests.get(url)
    if r.status_code != 200:
        print('error')
        return
    pictureUrl = r.json()['url']
    if "jpg" not in pictureUrl:
        print("No image for today, must be a video")
    else:
        pic = requests.get(pictureUrl, allow_redirects=True)
        filename = getFilename()
        open(filename, 'wb').write(pic.content)
        print(f"saved picture of the day to {filename}!")'''


#if __name__ == '__main__':
 #   downloadImageToday()
  #  filename = getFilename()
   # cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename + "\"'"
    #os.system(cmd)
