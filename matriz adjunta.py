import numpy as np

matriz = np.array([(5,3,-2),(-1,4,0),(4,2,1)])
signos = np.array([[(-1) ** (i + j) for j in range(3)] for i in range(3)])
matriz2 = np.array([(5,3),(-1,4)])

def determinante (mat):
    return (mat[0,0]*mat[1,1])-(mat[0,1]*mat[1,0])

#Transforma matriz de 3*3 a 2*2 

def trans (mat,fila,columna):
    if fila== 0 and  columna == 0:
        return np.array([(mat[1,1], mat[1,2]), (mat[2,1], mat[2,2])])
    elif fila == 0 and columna == 1:
        return np.array([(mat[1,0], mat[1,2]), (mat[2,0], mat[2,2])])
    elif fila == 0 and columna ==2:
        return np.array([(mat[1,0], mat[1,1]), (mat[2,0], mat[2,1])])
    elif fila == 1 and columna == 0:
        return np.array([(mat[0,1], mat[0,2]), (mat[2,1], mat[2,2])])
    elif fila == 1 and columna == 1:
        return np.array([(mat[0,0], mat[0,2]), (mat[2,0], mat[2,2])])
    elif fila == 1 and columna == 2:
        return np.array([(mat[0,0], mat[0,1]), (mat[2,0], mat[2,1])])
    elif fila == 2 and columna == 0:
        return np.array([(mat[0,1], mat[0,2]), (mat[1,1], mat[1,2])])
    elif fila == 2 and columna == 1:
        return np.array([(mat[0,0], mat[0,2]), (mat[1,0], mat[1,2])])
    elif fila == 2 and columna == 2:
        return np.array([(mat[0,0], mat[0,1]), (mat[1,0], mat[1,1])])

def adj (mat) :
    adj_de_mat = np.array([(0,0,0),(0,0,0),(0,0,0)])
    for i in range(0,3):
        for j in range(0,3):
            adj_de_mat[i,j]=int(determinante(trans(mat,i,j)))
    return adj_de_mat*signos




            

    

print(adj(matriz))

