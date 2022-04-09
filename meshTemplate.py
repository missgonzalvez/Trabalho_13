# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:30:01 2022

@author: acmgo
"""

$MeshFormat
2.2 0 8
$EndMeshFormat
$Nodes
6                      six mesh nodes:
1 0.0 0.0 0.0            node #1: coordinates (0.0, 0.0, 0.0)
2 1.0 0.0 0.0            node #2: coordinates (1.0, 0.0, 0.0)
3 1.0 1.0 0.0            etc.
4 0.0 1.0 0.0
5 2.0 0.0 0.0
6 2.0 1.0 0.0
$EndNodes
$Elements
2                      two elements:
1 3 2 99 2 1 2 3 4       quad #1: type 3, physical 99, elementary 2, nodes 1 2 3 4
2 3 2 99 2 2 5 6 3       quad #2: type 3, physical 99, elementary 2, nodes 2 5 6 3
$EndElements

$MeshFormat
version-number file-type data-size
$EndMeshFormat
$PhysicalNames
number-of-names
physical-dimension physical-tag "physical-name"
…
$EndPhysicalNames
$Nodes
number-of-nodes
node-number x-coord y-coord z-coord
…
$EndNodes
$Elements
number-of-elements
elm-number elm-type number-of-tags < tag > … node-number-list
…
$EndElements