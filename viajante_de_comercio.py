# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:17:52 2024

@author: ahino
"""
import math

def lee_lista(n):#modificado el leer_lista para que me lea las coordenadas de las ciudades
    coordenadas = []
    for _ in range(n):
        x, y = map(float, input().split())
        coordenadas.append((x, y))
    return coordenadas

def imprime_lista(a):
    n = len(a)
    if n==0:
        pass   # No hacer nada. Salir del if/función
    elif n==1:
        print(a[0])  # print(a)
    else:
        print(a[0],end=' ')   # imprime el primer elemento y un espacio
        imprime_lista(a[1:])  # imprime el resto de la lista (sin el primer elemento)


def distancias_euclideas(c1,c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def viaje_wrapper(n,ciudades):
    visitada=[False] * n
    camino=[0] * n 
    mejor_camino=[0]*n
    dist_min=math.inf #valor grande para que la primera nueva distancia sea menor
  
    dist_min=viaje(0,0,n,ciudades,visitada,camino,dist_min,mejor_camino)
    
    return dist_min,mejor_camino

def viaje(i,dist_total,n,ciudades,visitada,camino,dist_min,mejor_camino):
    if all(visitada):#ya ha recorrido todas las ciudades
        dist_total += distancias_euclideas(ciudades[camino[-1]],ciudades[camino[0]])#calcular por último cuando ya se han recorrido todas las ciudades, sumarle la distancia desde la última ciudad visitada hasta la primera ciudad desde la cual se empezo el camino
        if dist_total < dist_min:
            dist_min=dist_total
            for j in range(len(camino)):
                mejor_camino[j]=camino[j]
    else:
        for k in range(0,n):#generar candidatos
            if not visitada[k]:
                camino[i]=k
                visitada[k]=True
                #calcula la distancia entre la última ciudad del camino y la nueva ciudad que es el candidato
                if i == 0:#en caso de que el candidato sea la primera ciudad del camino
                    nueva_dist = dist_total + distancias_euclideas(ciudades[0], ciudades[k])
                else:#en caso de que ya haya otras ciudades en el camino
                    nueva_dist = dist_total + distancias_euclideas(ciudades[camino[i - 1]], ciudades[k])
                    
                if nueva_dist < dist_min:#optimizacion de que no siga buscando por esa solucion si la distancia no es menor a la antes calculada
                    dist_min=viaje(i + 1, nueva_dist,n,ciudades,visitada,camino,dist_min,mejor_camino)
                #sino quitarla como visitada para que se pueda utilizar esa ciudad en otros caminos   
                visitada[k]=False
            
    return dist_min


n=int(input())
coordenadas=lee_lista(n)
distancia_minima, camino_optimo=viaje_wrapper(n,coordenadas)
print(f"{distancia_minima:.4f}")
imprime_lista(camino_optimo)

