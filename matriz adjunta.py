import numpy as np

matriz = np.array([[6, 1, -3], [-1, 5, 2], [7, -4, 7]])
signos = np.array([[(-1) ** (i + j) for j in range(3)] for i in range(3)])
matriz2 = np.array([(5,3),(-1,4)])

def determinante (mat):
    return (mat[0,0]*mat[1,1])-(mat[0,1]*mat[1,0])

#Transforma matriz de 3*3 a 2*2 

def trans(mat, fila, columna):
    # Crear índices para filas y columnas excluyendo la fila y columna especificadas
    filas = [i for i in range(3) if i != fila]
    columnas = [j for j in range(3) if j != columna]
    return mat[np.ix_(filas, columnas)]

def adj (mat) :
    adj_de_mat = np.array([(0,0,0),(0,0,0),(0,0,0)])
    for i in range(0,3):
        for j in range(0,3):
            adj_de_mat[i,j]=int(determinante(trans(mat,i,j)))
    return (adj_de_mat*signos).T

print(adj(matriz))

