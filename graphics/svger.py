# open image as numpy array
from multiprocessing.sharedctypes import Value
import numpy as np
import PIL.Image as Image

def run(imagename, filename):
  result = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
   width="200px" height="200px" viewBox="0 0 200 200"
   xml:space="preserve">"""
  SL = 6
  arr = np.array(Image.open(imagename)).astype(np.int32)
  
  arr = arr.transpose(1, 0, 2)
  sampler = np.array([
    [1, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
  ], dtype=np.int32)
  sampler.resize((sampler.shape[0], sampler.shape[1], 1))
  sampler_inv = -sampler + 1
  print(sampler.shape)
  print(arr.shape)

  
  SKL = 200/700
  svg_triangles = []
  width, height , _ = arr.shape
  for i in range(0, (width - (width % SL)), SL):
    for j in range(0, (height - (height % SL)), SL):
      lt_sample = arr[i:(i+SL),j:(j+SL),:] * sampler
      ut_sample = arr[i:(i+SL),j:(j+SL),:] * sampler_inv
      lower_triangle = np.sum(lt_sample, axis=(0, 1)) / ((SL ** 2) / 2)
      upper_triangle = np.sum(ut_sample, axis=(0, 1)) / ((SL ** 2) / 2)
      lt = lower_triangle.clip(0, 255).astype(np.uint8)
      ut = upper_triangle.clip(0, 255).astype(np.uint8)
      L, R, T, B = i * SKL, (i+4) * SKL, j * SKL, (j+4) * SKL
      svg_triangles.append(f"""<polygon fill="#{lt[0]:02x}{lt[1]:02x}{lt[2]:02x}" fill-opacity="1" stroke-opacity="1" stroke="#{lt[0]:02x}{lt[1]:02x}{lt[2]:02x}" stroke-width="1"
points="{L},{B} {L},{T} {R},{B}"/>""")
      svg_triangles.append(f"""<polygon fill="#{ut[0]:02x}{ut[1]:02x}{ut[2]:02x}" fill-opacity="1" stroke-opacity="1" stroke="#{ut[0]:02x}{ut[1]:02x}{ut[2]:02x}" stroke-width="1"
points="{L},{T} {R},{T} {R},{B}"/>""")

  with open(filename, 'w') as f:
    f.write(result)
    f.write("\n")
    for triangle in svg_triangles:
      f.write(triangle)
      f.write("\n")
    f.write("\n")
    f.write("</svg>")


if __name__ == "__main__":
  imagename = "pluto_6.jpeg"
  filename = "task9.svg"
  run(imagename, filename)
