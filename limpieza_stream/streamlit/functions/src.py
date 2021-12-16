
import pandas as pd
import math
import numpy as np
import sys
sys.path.append('../')



def supermercado(supermercado):
    if supermercado == "Carrefour":
        return pd.read_csv("data/carr_cat.csv",encoding = "ISO-8859-1")
    if supermercado == "Mercadona":
        return pd.read_csv("data/mer_cat.csv",encoding = "ISO-8859-1")
    if supermercado == "Dia":
        return pd.read_csv("data/dia_cat.csv",encoding = "ISO-8859-1")
'''
producto_cantidad={}
producto_cantidad["f{sp.producto}"]=sp.cantidad
'''
def prod_cant(prod,cant):
    producto_cantidad={}
    producto_cantidad["f{producto}"]= cant
    return producto_cantidad

def anularnulos(a):
    if a == 0:
        return 1
    else:
        return a