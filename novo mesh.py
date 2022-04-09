#  uma classe para implementar um ponto no plano ou no espaco
#  outra classe para implementar um segmento
#  outra classe para implementar um poligono

# introduzimos construtores :

class Vertex :
    def __init__ ( self, co ) :
        # declarado com dois argumentos
        # estranhamente, usado com apenas um argumento
        self .coords = co

class Segment :
    def __init__ ( self, V, W ) :
        # declarado com tres argumentos
        # estranhamente, usado com apenas dois argumentos
        self .base = V
        self .tip  = W

class Polygon :
    def __init__ ( self, bd ) :
        # usando "assert", confirmar que a ponta de cada
        # segmento coincide com a base do proximo
        self .bdry = bd  # lista de segmentos

def Triangle ( s1, s2, s3 ) :
    return Polygon ( [ s1, s2, s3 ] )

def Quadrangle ( s1, s2, s3, s4 ) :
    return Polygon ( [ s1, s2, s3, s4 ] )

'''def draw_ps ( list_of_cells, filename ) :
    f = open ( filename, 'w' )
    list_of_seg = []
    nb_of_bdry_seg = 0
    for cll in list_of_cells :
        for i in range ( len ( cll .bdry ) ) :
            new_seg = cll .bdry [i]
            assert new_seg .base == cll .bdry [i-1] .tip
            found = False
            for s in list_of_seg :
                assert ( ( new_seg .base != s .base ) or ( new_seg .tip != s .tip ) )
                if ( new_seg .base == s .tip ) and ( new_seg .tip == s .base ) :
                    found = True
            if found : nb_of_bdry_seg -= 1
            else :
                nb_of_bdry_seg += 1
                list_of_seg .append ( new_seg )
    print ( nb_of_bdry_seg, " boundary segments" )
    xmin =  1.e8
    xmax = -1.e8
    ymin =  1.e8
    ymax = -1.e8
    for s in list_of_seg :
        for v in [ s.base, s.tip ] :
            c = v .coords
            if c[0] > xmax : xmax = c[0]
            if c[1] > ymax : ymax = c[1]
            if c[0] < xmin : xmin = c[0]
            if c[1] < ymin : ymin = c[1]
    if xmax-xmin < ymax-ymin : maxside = ymax-ymin
    else : maxside = xmax-xmin
    border = 0.02 * maxside
    scale_factor = 500. / maxside
    translation_x = - scale_factor * xmin
    translation_y = - scale_factor * ymin
    print ( "%!PS-Adobe-3.0 EPSF-3.0", file=f )
    print ( "%%Title:       triangles", file=f )
    print ( "%%BoundingBox:  0 0", scale_factor*(xmax-xmin+2*border), \
            scale_factor*(ymax-ymin+2*border), file=f                  )
    print ( "%%EndComments", file=f )
    print ( "gsave", file=f )
    print ( translation_x + scale_factor*border, translation_y + scale_factor*border, \
            "translate", file=f                                                        )
    print ( scale_factor, "dup scale", file=f )
    print ( "gsave", 1.5 / scale_factor, " setlinewidth", file=f )
    for s in list_of_seg :
        print ( s .base .coords[0], s .base .coords[1], 'moveto', \
                s .tip  .coords[0], s .tip  .coords[1], 'lineto stroke', file = f )
    print ( "grestore", file=f )
    print ( "grestore", file=f )
    print ( "showpage", file=f )
    print ( "%%Trailer", file=f )
    print ( "%EOF", file=f )'''

from random import sample
L=sample(range(80,100),10)
print(L)
print(sorted(L))

import numpy as np

A = Vertex ( [0.,0.,0.] )
B = Vertex ( [2.,4.,0.] )
C = Vertex ( [2.,3.,0.] )
D = Vertex ( [1.,1.,0.] )

lista_vertices=[A.coords,B.coords,C.coords,D.coords]

AB = Segment ( A, B )
BC = Segment ( B, C )
AC = Segment ( A, C )
CA = Segment ( C, A )
CD = Segment ( C, D )
DA = Segment ( D, A )

ABC = Triangle ( AB, BC, CA )
ACD = Triangle ( AC, CD, DA )

#print(vertice)

#print(BC.base.coords)

#print(ABC.bdry.coords)

'''rng = np.random.default_rng()
nb_vertices = rng.integers(1, len(lista_vertices), size=3) #esta repite los números
print(nb_vertices)'''

nb_vertices1 = [sample(range(1, len(lista_vertices)), 3)]
print (nb_vertices1)

lista_seg = [AB.base.coords,BC.base.coords,CA.base.coords, AC.base.coords, CD.base.coords,DA.base.coords]
        
lista_triangulos=np.array_split(lista_seg,len(lista_seg)/3)
#print(lista_triangulos[1])
        


#AB, BC, CA = 12 23 31


#4. Exportar para ficheiro.
nb_nodes=len(lista_vertices) #Calcular número de pontos da malha.
nb_elements = len(lista_triangulos)
#nb_elements=len(mesh) #Calcular o número de elementos da malha.
file=open("mesh.dat","w")

file.write("{}{} {}{}".format("$MeshFormat\n","2.2","0 8","\n$EndMeshFormat"))

file.write("{}\n".format("\n$Nodes"))
file.write("{}\n".format(nb_nodes))
for i,lista in enumerate(lista_vertices,start=1): #Enumerate permite enumerar cada node. 
    file.write("{} {} {} {}\n".format(i,lista[0],lista[1],lista[2]))
file.write("{}\n".format("$EndNodes"))

file.write("{}\n".format("\n$Elements"))
file.write("{}\n".format(nb_elements))
for j,element in enumerate(nb_vertices1, start=1):
    file.write("{} {} {} {}\n".format(j,element[0],element[1],element[2]))
file.write("{}\n".format("$EndElements"))

#Esto hace lo que queremos, pero no soy capaz de imprimirlo bien el fichero
#Solo me sale una linea :(
'''for i, vertices in enumerate( range(len(lista_triangulos)), start=1):
    vertices = [sample(range(1, len(lista_vertices)), 3)]
    print(i,vertices)'''


file.close()

#draw_ps ( [ ABC, ACD ], "two-triangles.eps" )

def mesh_converter(list_of_triangles):
    #f = open ( filename, 'w' )
    print([ABC,ACD])

mesh_converter([ABC,ACD])

#lista_vertices=[A,B,C,D]
#print(lista_vertices)

#n=len(lista_vertices)
#print(n)

#for i in enumerate(lista_vertices):
#    L=i
#print(L)
