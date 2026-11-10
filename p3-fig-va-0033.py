import numpy as np 
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Keyla Paola NC = 0033 | Fecha 10/nov/2026
print("Keyla Paola NC = 0033")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread("TomHolland.jpg")
plt.imshow(mi_imagen)
plt.title("Tom Holland y Keyla Paola 0033")
plt.show()

print("---puntos en la imagen---")
plt.imshow(mi_imagen)
x = [114,100,300,]
y = [100,400,500]
plt.scatter(x,y, s=20,c="red")
plt.show()