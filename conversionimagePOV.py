"""
@author Team POV-Design
@about Convert images for POV display
"""

#   Libraries
import numpy as np
import csv  # para crear el archivo
import math # para usar operaciones trigonométricas 
import cv2  # para manipular la imagen

#   Configuration
nleds = 28              # Número de LED's
angleresolution = 1.8   # Ángulo de resolución multiplo de 360

#   Main   
def run():
    # Read image and copy
    name = "4550"                       # Colocar nombre de la imagen
    imagen = cv2.imread(name + '.png')  # Colocar imagen en la misma carpeta
    imagen_copy = imagen                # Copia de imagen para modificarla
    if imagen is None:
        sys.exit("Could not read the image.")   # Mensaje si no se encuentra ninguna imagen
    
    # Change size according to number of leds
    dsize = (nleds, nleds)
    imagen_copy = cv2.resize(imagen_copy,dsize)

    # Conversion
    total_stripes_POV = int(360/angleresolution)    # Tiras totales a crear
    POV_imagedata = []                              # Creación de lista vacia para imagen convertida

    # Corrido de todas las tiras
    for stripes_POV in range(0, total_stripes_POV,1):                   
        angle_POV = round(stripes_POV * 1.8,1)      # Conversión de tira actual a ángulo actual
        rad_angle_POV = ((angle_POV)* math.pi)/180  # Conversión de angulo de grados a radianes
        stripe = int(nleds/2)                       # Creación de tamaño de tira

        # Corrido de LED por LED de la tira actual
        for pos_LED in range(1, stripe + 1, 1):
            # Conversión de polar a cartesiano para extraer 
            # una posición aproximada de la ubicación del LED en cartesiano                     
            x = stripe - 1 + round(pos_LED *  math.cos(rad_angle_POV))  
            y = stripe - 1 + round(pos_LED *  math.sin(rad_angle_POV))

            #Extracción del color de la posición
            R = imagen_copy[x, y][2]
            G = imagen_copy[x, y][1]
            B = imagen_copy[x, y][0]

            #Se agrega el ángulo de la tira, la posición del LED y el color en RGB
            POV_imagedata.append([angle_POV * 10, pos_LED, R, G ,B]) # El ángulo inicia en 0°
    
    # Crear y escribir archivo en formato .csv para la imagen convertida
    # file = open(name + "_POVimage.csv", "w", newline='') # Nombre del archivo "POV_image.csv"
    # spamreader = csv.writer(file)
    # spamreader.writerow(POV_imagedata)
    np.savetxt("output.csv",   # Archivo de salida
           POV_imagedata,        # Trasponemos los datos
           fmt="%d",       # Usamos números enteros
           delimiter=",")  # Para que sea un CSV de verdad
    # file.close()
    
    # Confirmación de conversión
    print("Imagen " + name + ".png" " convertida a formato POV")
    print("Nombre del archivo " + name + "_POVimage.csv")

#   Run code
if __name__ == '__main__':
    run()
    