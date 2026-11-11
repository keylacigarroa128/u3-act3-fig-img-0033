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

print("---Cuadro azul en la imagen---")
img_Tom = cv2.imread("TomHolland.jpg")
plt.imshow(img_Tom)
x = [70, 310, 310, 70, 70]
y = [60, 60, 300, 300, 60]
plt.plot(x,y,c="blue")
plt.show()
print("---Circulo verde en la imagen---")
I = cv2.imread("TomHolland.jpg")
plt.imshow(I)

N = 30  # Lados del polígono
x = np.zeros((N+1,))
y = np.zeros((N+1,))

(xc, yc) = (200, 205)  # Centro del círculo
r = 160  # Radio

for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c="green")
plt.show()

