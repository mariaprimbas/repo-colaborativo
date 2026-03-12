# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:41:04 2026

@author: olivi
"""

def registrar_habitos():
    '''
    Registrar los habitos de las personas 

    Returns
    -------
    lista : list
        Lista que guarda las actividades que hacen las personas.

    '''
    actividades = input("Ingresa una actividad: ")
    lista =[]  
    lista.append(actividades) 
    pregunta = input("Desea agregar actividades?")
    while pregunta == "Si"    : 
        actividades = input("Ingresa una actividad: ")
        pregunta = input("Desea agregar actividades?")
        continue
        if pregunta== "No":
            break
    return lista 
    
def analizar_habitos(lista):
    '''
    Contar cuantas veces se realiza cada actividad 

    Parameters
    ----------
    lista : list
        lista que guarda las actividades.

    Returns
    -------
    diccionario : dicc
        Guarda como  las actividades y sus respectivas cantidades 

    '''
    diccionario= {}
    for actividad in lista: 
        if actividad not in diccionario: 
            diccionario[actividad] = 1
        else: 
            diccionario[actividad] += 1 
    return diccionario

