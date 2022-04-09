#Libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import Delaunay
from turtle import *

#1. Criar função para gerar malha de triângulos.
    #L: Lado;
    #h: Altura;
    #n_elementos: N.º de nós entre valores mínimo e máximo.
    
L=int(input("Introduzir altura da malha: "))
h=int(input("Introduzir largura da malha: "))
n_elementos=int(input("Introduzir número de elementos da malha: "))
Nodes=[]

def lista_triangulos(L,h,n_elementos):
    for x in np.linspace(0,L,num=n_elementos):
        for y in np.linspace(0,h,num=n_elementos):
            #for z in np.linspace(0,0,num=n_elementos):
            Nodes.append([x,y])
                #Nodes.append([x,y,z])
    print(Nodes)

lista_triangulos(L,h,n_elementos)

#3. Visualizar Nodes.
points=np.array(Nodes)
plt.plot(points[:,0],points[:,1],'o',color="Black")
plt.ylabel('h')
plt.xlabel('L')
plt.show()

#3. Criar elementos da malha através da Triangulação de Delaunay.
tri=Delaunay(points) #Pontos de união dos triângulos.
#print(tri)
plt.triplot(points[:,0],points[:,1],tri.simplices,color="Black") #tri.simplices contém uma matriz com os índices dos pontos de união dos triângulos.
plt.plot(points[:,0],points[:,1],'o',color="Black")
plt.show()

mesh=tri.simplices #Elementos.

#4. Exportar para ficheiro.
nb_nodes=len(points) #Calcular número de pontos da malha.
nb_elements=len(mesh) #Calcular o número de elementos da malha.

file=open("mesh.dat","w")

file.write("{}{} {}{}".format("$MeshFormat\n","2.2","0 8","\n$EndMeshFormat"))

file.write("{}\n".format("\n$Nodes"))
file.write("{}\n".format(nb_nodes))
for i,node in enumerate(Nodes): #Enumerate permite enumerar cada node. 
    file.write("{} {} {}\n".format(i,node[0],node[1]))
file.write("{}\n".format("$EndNodes"))

file.write("{}\n".format("\n$Elements"))
file.write("{}\n".format(nb_elements))
for j,element in enumerate(mesh):
    file.write("{} {} {} {}\n".format(j,element[0],element[1],element[2]))
file.write("{}\n".format("$EndElements"))

file.close()
