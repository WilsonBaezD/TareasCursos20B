import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

def definir_parametros():
    radio_min = 1
    radio_max = 4
    angulo_cono = np.pi / 6
    momento_angular_cuadrado = 2 * 9.8 * radio_min**2 * radio_max**2 * np.sin(angulo_cono)**2 * np.cos(angulo_cono) / (radio_min + radio_max)
    return radio_min, radio_max, angulo_cono, momento_angular_cuadrado

# Ecuaciones del sistema
def ecuaciones_movimiento(t, variables, momento_angular_cuadrado, angulo_cono):
    r, velocidad_radial, phi = variables
    aceleracion_radial = momento_angular_cuadrado / (r**3 * np.sin(angulo_cono)**2) - 9.8 * np.cos(angulo_cono)
    velocidad_angular = np.sqrt(momento_angular_cuadrado) / (r**2 * np.sin(angulo_cono)**2)
    return [velocidad_radial, aceleracion_radial, velocidad_angular]

# Resolución del sistema de ecuaciones diferenciales
def resolver_movimiento(momento_angular_cuadrado, angulo_cono, tiempo, condiciones_iniciales):
    return solve_ivp(ecuaciones_movimiento, tiempo, condiciones_iniciales, t_eval=np.linspace(tiempo[0], tiempo[1], 1000), args=(momento_angular_cuadrado, angulo_cono))

# Conversión a coordenadas cartesianas
def polar_a_cartesianas(solucion, angulo_cono):
    r_valores = solucion[:, 0]
    phi_valores = solucion[:, 2]
    x_cartesiana = r_valores * np.cos(phi_valores) * np.sin(angulo_cono)
    y_cartesiana = r_valores * np.sin(phi_valores) * np.sin(angulo_cono)
    z_cartesiana = r_valores * np.cos(angulo_cono)
    return x_cartesiana, y_cartesiana, z_cartesiana

# superficie del cono
def crear_superficie_cono(radio_max, angulo_cono):
    phi_malla, r_malla = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, radio_max, 40))
    x_superficie = r_malla * np.cos(phi_malla) * np.sin(angulo_cono)
    y_superficie = r_malla * np.sin(phi_malla) * np.sin(angulo_cono)
    z_superficie = r_malla * np.cos(angulo_cono)
    return x_superficie, y_superficie, z_superficie

# Configuración de la grafica
def graficar_cono_y_trayectoria(x_superficie, y_superficie, z_superficie, x_trayectoria, y_trayectoria, z_trayectoria):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x_superficie, y_superficie, z_superficie, color='lightgray', alpha=0.3, edgecolor='none')

    ax.plot(x_trayectoria, y_trayectoria, z_trayectoria, color='red', linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Movimiento en una superficie cónica')

    ax.view_init(elev=70, azim=120)
    plt.grid(True)
    plt.show()

radio_min, radio_max, angulo_cono, momento_angular_cuadrado = definir_parametros()

# Condiciones iniciales y t
condiciones_iniciales = [radio_min, 0, 0]
tiempo = [0, 20]

solucion = resolver_movimiento(momento_angular_cuadrado, angulo_cono, tiempo, condiciones_iniciales)

x_trayectoria, y_trayectoria, z_trayectoria = polar_a_cartesianas(solucion.y.T, angulo_cono)

x_superficie, y_superficie, z_superficie = crear_superficie_cono(radio_max, angulo_cono)

graficar_cono_y_trayectoria(x_superficie, y_superficie, z_superficie, x_trayectoria, y_trayectoria, z_trayectoria)
