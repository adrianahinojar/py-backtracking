# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:41:36 2024

@author: ahino
"""
def lee_lista(n):  
    a = []
    if n>0:
        cadenaEntrada = input()
        for i in range(0, n): 
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)
            
    return a


def max_peso_mochilas_wrapper(pesos,capacidad_mochila1,capacidad_mochila2):
    sol=[0] * (len(pesos)) #solucion parcial actual
    sol_opt= [0] * (len(pesos))#solucion parcial optima
    
    v_total = max_peso_mochilas(0,capacidad_mochila1,capacidad_mochila2,0,sum(pesos),sol,sol_opt,-1,pesos,capacidad_mochila1,capacidad_mochila2)
     
    return v_total

def max_peso_mochilas(i,capacidad_mochila1_restante,capacidad_mochila2_restante,v_actual,max_v,sol,sol_opt,v_opt,pesos,capacidad_mochila1,capacidad_mochila2):
    if i == len(sol):
       if v_actual > v_opt:
           v_opt = v_actual
           for k in range(len(sol)):
               sol_opt[k] = sol[k]
    else:
       for k1 in range(0,2):#genera candidatos para la mochila 1
          for k2 in range(0,2): #genera candidatos para la mochila 2
          
              if (k1 == 1 and k2== 0) or (k1==0 and k2==1) or (k1==0 and k2==0):
                   if k1 * pesos[i] <= capacidad_mochila1_restante and k2 * pesos[i] <= capacidad_mochila2_restante:
                       
                       if k1==0 and k2==0:#no se mete en ninguna de las dos mochilas se resta del maximo beneficio posible
                          nuevo_max_v= max_v - pesos[i]
                       else:
                           nuevo_max_v=max_v#si se guarda en alguna de las dos mochilas no cambia nada
                       
                       if nuevo_max_v> v_opt:#comprueba si se puede podar el arbol de recursion por valor
                           sol[i]=(k1,k2)#expandir la solucion parcial
                    
                           nueva_capacidad_mochila1_restante = capacidad_mochila1_restante - k1 * pesos[i]
                           nueva_capacidad_mochila2_restante = capacidad_mochila2_restante - k2 * pesos[i]
                    
                           nuevo_v_actual = v_actual + k1 * pesos[i] + k2 * pesos[i]
                           
                           v_opt = max_peso_mochilas(i + 1, nueva_capacidad_mochila1_restante, nueva_capacidad_mochila2_restante, nuevo_v_actual,nuevo_max_v, sol, sol_opt, v_opt, pesos, capacidad_mochila1, capacidad_mochila2)
                       
   
    return v_opt #devuelve el mejor valor conseguido                   
               
n=int(input()) 
pesos=lee_lista(n)     
capacidades=lee_lista(2)  
capacidad_mochila1=capacidades[0]
capacidad_mochila2=capacidades[1]
resultado=max_peso_mochilas_wrapper(pesos,capacidad_mochila1,capacidad_mochila2)    
print(resultado)