'''
Script para recomendar posibles palabras correctas
a traves del calculo de distancias.
Pablo Camacho Gonzalez
'''

from nltk.corpus import words
import numpy as np
Palabras_correctas = words.words()

def recomendador1(palabra):
    lista = listaPalabras(palabra)
    palabra_correcta = ''
    grande = 1
    for ys in lista:
        sumaInter = 0
        sumaUnion = 0
        for xs in range(0,len(palabra)-2):
            original = palabra[xs:xs+3]
            posible = ys[xs:xs+3]
            inter = set(original).intersection(posible)
            union = set(original).union(posible)
            sumaInter += len(inter)
            sumaUnion += len(union)
        distancia = (sumaUnion - sumaInter)/sumaUnion
        if distancia < grande:
            grande = distancia
            palabra_correcta = ys
    return palabra_correcta


def recomendador2(palabra):
    lista = listaPalabras(palabra)
    palabra_correcta = ''
    grande = 1
    for ys in lista:
        sumaInter = 0
        sumaUnion = 0
        for xs in range(0,len(palabra)-3):
            original = palabra[xs:xs+4]
            posible = ys[xs:xs+4]
            inter = set(original).intersection(posible)
            union = set(original).union(posible)
            sumaInter += len(inter)
            sumaUnion += len(union)
        distancia = (sumaUnion - sumaInter)/sumaUnion
        if distancia < grande:
            grande = distancia
            palabra_correcta = ys
    return palabra_correcta

def listaPalabras(palabra):
    palabras_iguales = []
    for xs in Palabras_correctas:
        if xs[0] == palabra[0]:
            palabras_iguales.append(xs)
    return palabras_iguales

def recomendador3(palabra):
    lista = listaPalabras(palabra)
    maximo = 10
    palabra_correcta = ''
    for ys in lista:
        m = levenshtein(palabra, ys)
        if m < maximo:
            maximo = m
            palabra_correcta = ys
    return palabra_correcta


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return matrix[size_x - 1, size_y - 1]


def ejercicio1():
    return [recomendador1('cormulent'),recomendador1('incendenece'),recomendador1('validrate')]

def ejercicio2():
    return [recomendador2('cormulent'),recomendador2('incendenece'),recomendador2('validrate')]

def ejercicio3():
    return [recomendador3('cormulent'),recomendador3('incendenece'),recomendador3('validrate')]


if __name__ == "__main__":
    ejercicio1()
    ejercicio2()
    print(ejercicio3())
