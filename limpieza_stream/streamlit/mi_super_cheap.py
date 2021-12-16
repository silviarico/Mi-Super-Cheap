import streamlit as st
import pandas as pd
import functions.src as sp

supermercado_ = st.selectbox("Select supermarket", ["Choose and option"] + ["Dia", "Carrefour" , "Mercadona"])
lista_productos=[]
lista_cantidad=[]
if supermercado_ == "Choose and option":
    st.write("selecciona supermercado")
else:

    df = sp.supermercado(supermercado_)
    df = pd.DataFrame(df)
    st.dataframe(df)
    unicos = list(df["categoria"].unique())

    producto  = st.selectbox("Select product", ["Choose and option"] + unicos)

    medida = st.selectbox("measure", ["Choose and option"] + ["Kilo", "Liter" , "unit","meter"])

    cantidad = st.number_input('quantity needed') 
    
    clicked=st.button("añadir producto")

 
    if clicked== True:
        count = 2
        df = sp.supermercado(supermercado_)
        df = pd.DataFrame(df)
        st.dataframe(df)
        producto = ""
        medida = ""
        cantidad = ""
        if len(producto) == 0 and len(medida) == 0 and len(cantidad):
            unicos = list(df["categoria"].unique())
        
            producto  = st.selectbox(f"Select product{count}", ["Choose and option"] + unicos)

            medida = st.selectbox(f"measure{count}", ["Choose and option"] + ["Kilo", "Liter" , "unit","meter"])

            cantidad = st.number_input(f'quantity needed{count}') 
        else:
            lista_cantidad.append(cantidad)
            lista_productos.append(producto)
            clicked=st.button(f"añadir producto{count}")
            count+=1
        print(lista_cantidad)
    

    
    else:
        dic_pq={}
        dic_pq[f"{producto}"]=cantidad
        df["cantidad_deseada"] = df["categoria"].map(dic_pq)
        df_filtrado=df[df["categoria"].isin(list(dic_pq.keys()))]
        df_filtrado["cantidad_deseada"] = df_filtrado["categoria"].map(dic_pq)
        df_filtrado["unidades_necesarias"] = df_filtrado.cantidad_deseada/df_filtrado.cantidad
        df_filtrado["unidades_necesarias"] = df_filtrado.unidades_necesarias.astype(int)
        df_filtrado["unidades_necesarias"]=df_filtrado.unidades_necesarias.apply(sp.anularnulos)
        df_filtrado["precio_final"]= df_filtrado.unidades_necesarias*df_filtrado.precio
    
    
    
        st.dataframe(df_filtrado.groupby("categoria").precio_final.min())


