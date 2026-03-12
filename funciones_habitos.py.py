# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:41:04 2026

@author: olivi
"""

def registrar_habitos():
    actividades = input("Ingresa una actividad: ")
    lista =[]  
    lista.append(actividades) 
    pregunta = input("Desea agregar actividades?")
    while pregunta == "Si"    : 
        actividades = input("Ingresa una actividad: ")
        continue
        if pregunta== "No":
            break
    return lista 
    
def analizar_habitos(lista):
    diccionario= {}
    for actividad in lista: 
        if actividad not in diccionario: 
            diccionario[actividad] = 1
        else: 
            diccionario[actividad] += 1 
    return diccionario

