import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

radio_inicial = 2.25
angulo_cono = np.pi / 3  # Ángulo del cono (equivalente a asin(sqrt(3)/6) en radianes)
frecuencia = np.sqrt(9.8 * np.cos(angulo_cono) / radio_inicial) / np.sin(angulo_cono)
frecuencia_angular = np.sqrt(3 * 9.8 * np.cos(angulo_cono) / radio_inicial)
tiempo = np.arange(0, 2 * np.pi * frecuencia_angular / frecuencia, 0.01)

# Cálculos para la trayectoria
radio = radio_inicial + 0.25 * np.sin(frecuencia_angular * tiempo)
angulo = frecuencia * tiempo - 2 * (0.25 / radio_inicial) * (frecuencia / frecuencia_angular) * np.sin(frecuencia_angular * tiempo)
coordenada_x = radio * np.cos(angulo) * np.sin(angulo_cono)
coordenada_y = radio * np.sin(angulo) * np.sin(angulo_cono)
coordenada_z = radio * np.cos(angulo_cono)

# Configuración de la grafica
figura = plt.figure()
eje = figura.add_subplot(111, projection='3d')
eje.view_init(70, 120)

# La Superficie cónica
angulo_superficie = np.linspace(0, 2 * np.pi, 40)
radio_superficie = np.linspace(0, 4, 40)
angulo_superficie, radio_superficie = np.meshgrid(angulo_superficie, radio_superficie)
x_superficie = radio_superficie * np.cos(angulo_superficie) * np.sin(angulo_cono)
y_superficie = radio_superficie * np.sin(angulo_superficie) * np.sin(angulo_cono)
z_superficie = radio_superficie * np.cos(angulo_cono)

eje.plot_surface(x_superficie, y_superficie, z_superficie, color='gray', alpha=0.2, edgecolor='none')

eje.plot(coordenada_x, coordenada_y, coordenada_z, color=[0.7, 0, 0], linewidth=1.5)

eje.set_xlabel('x')
eje.set_ylabel('y')
eje.set_zlabel('z')
eje.set_title('Movimiento en una superficie cónica')
# Mostrar la grafica
plt.grid(True)
plt.show()
