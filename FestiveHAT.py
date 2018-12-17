from sense_hat import SenseHat
from colorsys import hsv_to_rgb
import time
import numpy as np
import random

def make_snow(threshold):
  if random.random() < threshold:
    return [255,255,255]
  else:
    return [0,0,0]

if __name__ == "__main__":
    e = [0,0,0]
    o = [150,30,30]
    g = [0,255,0]
    w = [255,255,255]
    b = [0,0,255]
    r = [255,0,0]
    y = [255,255,0]
    
    print("Setting up SenseHAT")
    sense = SenseHat()
    background = [
      e,e,e,y,y,e,e,e,
      e,e,e,g,g,e,e,e,
      e,e,g,g,b,g,e,e,
      e,e,g,r,g,g,e,e,
      e,g,g,b,g,r,g,e,
      e,g,r,g,r,g,g,e,
      e,e,e,o,o,e,e,e,
      w,w,w,o,o,w,w,w,
      ]
      
    sense.rotation = 270
    foreground = [
    e,e,e,e,e,e,e,e,  #Row 0: (0,8)
    e,e,e,e,e,e,e,e,  #Row 1: (8,16)
    e,e,e,e,e,e,e,e,  #Row 2: (16,24)
    e,e,e,e,e,e,e,e,  #Row 3: (24,32)
    e,e,e,e,e,e,e,e,  #Row 4: (32,40)
    e,e,e,e,e,e,e,e,  #Row 5: (40,48)
    e,e,e,e,e,e,e,e,  #Row 6: (48,56)
    e,e,e,e,e,e,e,e,  #Row 7: (56,64)
    ]
    
    try:
      
      while True: 
        image = background[:]
        #Update foreground
        for i in range(0,8):
          foreground[i+56] = foreground[i+48]
          foreground[i+48] = foreground[i+40]
          foreground[i+40] = foreground[i+32]
          foreground[i+32] = foreground[i+24]
          foreground[i+24] = foreground[i+16]
          foreground[i+16] = foreground[i+8]
          foreground[i+8] = foreground[i]
          foreground[i] = make_snow(0.13)
        for i in range(0, 64):
          image[i] = foreground[i] if foreground[i] == w else background[i]
        sense.set_pixels(image)
        time.sleep(0.5)
    
    except(KeyboardInterrupt):
      print("Clearing SenseHAT...")
      sense.clear()
      