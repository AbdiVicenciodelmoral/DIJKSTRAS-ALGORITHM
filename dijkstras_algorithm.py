#!/usr/bin/env python
# coding: utf-8

import math

######## DATA STRUCTURES  #########
class graph:
    def __init__(self):
        self.V = {}
        self.E = []
        
class vertex:
    def __init__(self,label, d=None, pi=None):
        self.label = label
        self.d = d
        self.pi = pi    
        
def MAKE_GRAPH(elements):
    g = graph()
    for v in elements:
        vert = vertex(v)
        g.V[v] = vert
        for e in elements[v]:
            g.E.append([v,e,elements[v][e]])
            
    #g.E.sort(key=lambda x: x[2])
    return g  


def GET_MST(G):
    A = []
    for v in G.V:
        if G.V[v].pi == None:
            A.append(['Start',G.V[v].label,G.V[v].d])
        else:
            A.append([G.V[v].pi.label,G.V[v].label,G.V[v].d])
    A.sort(key=lambda x: x[2])
    return A


###### DIJKSTRA'S ALGORITHM  ######

def INITIALIZE_SINGLE_SOURCE(G,s):
    for v in G.V:
        G.V[v].d = math.inf
        G.V[v].pi = None
    G.V[s].d = 0
    
def RELAX(u,v,w):
    if v.d > u.d + w:
        print("Relaxing Edge: ({},{}) with new weight: {}".format(u.label,v.label,w))
        v.d = u.d + w
        v.pi = u
          
def EXTRACT_MIN(Q):
    min_v = math.inf
    index = None
    for v, val in Q.items():
        if min_v > val.d:
            min_v = val.d
            index = v
    del Q[index] 
    return index,min_v
    
    
def Dijkstras(G,s):
    INITIALIZE_SINGLE_SOURCE(G,s)
    S = []
    Q = G.V.copy()
    while len(Q) > 0:
        u,cost = EXTRACT_MIN(Q)
        S.append(u)
        print("Current Vertex: {}".format(u))
        for u,v,w in G.E:
            RELAX(G.V[u],G.V[v],w)
    return S,G
            


# representation of the elements that make up the graph           
elements = { "A": {"B":4,"F":2},
          "B": {"A":1,"C":3,"D":4},
          "C": {"A":6,"B":3,"D":7},
          "D": {"A":6,"E":2},
          "E": {"D":5},
          "F": {"D":2,"E":3},
           }
                   
#Create the graph from the class graph, using the MAKE_GRAPH function        
G = MAKE_GRAPH(elements)

# Use Disjkstras algorithm.
S,A = Dijkstras(G,"C")
mst = GET_MST(A)
print("MST PATH:")
for u,v,w in mst:
    if u == 'Start':
        print("EDGE: ({} , {}) {:>17s} {}".format(u,v,"CURRENT WEIGHT:",w))
    else:
        print("EDGE: ({} , {}) {:>21s} {}".format(u,v,"CURRENT WEIGHT:",w))   






