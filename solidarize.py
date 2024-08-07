import streamlit as st # type: ignore
import pandas as pd
import altair as alt


st.set_page_config(layout="wide")


def nav_button(label, anchor):
    st.markdown(f'<a href="#{anchor}" style="text-decoration: none;">{label}</a>', unsafe_allow_html=True)






# Configuração do título do aplicativo


# st.image('C:\Projetos\Solidarize\logo_small.png', width=100)
st.title(':blue[Solidarize]')
#st.title(":blue[Solidarize]")
tab1, tab2, tab3 = st.tabs(["Saiba mais", "Acompanhe", "Prioridades :warning:"])

with tab1:
    # Resumo da campanha
    st.header('Saiba mais')
    st.write("""
            
    A campanha **Solidarize** ocorre anualmente e visa arrecadar alimentos e apoiar aqueles que enfrentam dificuldades em nossa comunidade.
     
    Sua participação é fundamental e fará toda a diferença na vida de muitas famílias.

    **Como você pode ajudar:**

    📦 **Doações:** Alimentos não perecíveis.  
    🗓️ **Período:** 10/08/2024  
    📍 **Locais de arrecadação:** 
            
    - Principais Mercados da Cidade  
    - Drive Thru
        - Camaquã: Av. Jose Loureiro da Silva, 787 - Carvalho Bastos, Camaquã - RS, 96784-058
        - Cristal: Rua Pedro Osório, 109 - Centro, Cristal - RS, 96195-000
        - Tapes: Av. Borges de Medeiros, 156, Tapes - RS, 96760-000
        
            

    Juntos podemos :blue[mais !] :palms_up_together:
            

    """)
    ""
    ""
    ""
    ""

with tab2:

########### DADOS DA CAMPANHA

    entradas = pd.read_csv(st.secrets.gsheet.entradas).sort_values(by=['Quantidade'],ascending=False)
    st.header("Até agora com a sua ajuda já arrecadamos ...")

    ""
    ""
    "" 

    col1,col2 = st.columns(2)
    
    total_kgs = entradas["Quantidade"].sum()
    
    tile1 = col1.container(height=200)
    tile1.markdown(f"<h1 style='text-align: center; color: black; font-size:70px'>{total_kgs}</h1>", unsafe_allow_html=True)
    tile1.markdown("<h3 style='text-align: right; color: black;'>Quantidade (Kgs)</h3>", unsafe_allow_html=True)
 

    total_cestas = entradas["Cestas"].sum()

    tile2 = col2.container(height=200)
    tile2.markdown(f"<h1 style='text-align: center; color: black; font-size:70px'>{total_cestas}</h1>", unsafe_allow_html=True)
    tile2.markdown("<h3 style='text-align: right; color: black;'>Cestas Básicas Montadas</h3>", unsafe_allow_html=True)
    
    #col1, col2, col3 = st.columns(3)
    #col2.metric(label="Total Arrecadado (kg)", value="70.000")


    #st.write(""" 
    ##### E já conseguimos montar **700** cestas básicas !
             
    #""")

    ""
    ""
    ""
    ""
    
    # Gráfico de barras com Altair
    # color='blues'
    chart = alt.Chart(entradas).mark_bar().encode(
        x=alt.X('Localidade:N',axis=alt.Axis(title='') ),
        y=alt.Y('Quantidade:Q',axis=alt.Axis(labels=False, title='Quantide em KGs')),
        tooltip=['Localidade', 'Quantidade']
    ).properties(
        title='Quantidade (kgs) por Localidade'
    )
    st.altair_chart(chart, use_container_width=True)

    chart2 = alt.Chart(entradas).mark_bar().encode(
        x=alt.X('Localidade:N',axis=alt.Axis(title='') ),
        y=alt.Y('Cestas:Q',axis=alt.Axis(labels=False, title='Quantide Cestas')),
        tooltip=['Localidade', 'Cestas']
    ).properties(
        title='Quantidade de Cestas por Localidade'
    )
    st.altair_chart(chart2, use_container_width=True)

with tab3:

    ############## ITENS PRIORITARIOS
    ""
    ""
    ""
    st.header("Itens Prioritários")
    necessidades = pd.read_csv(st.secrets.gsheet.necessidades, index_col="Localidade")

    ""
    ""
    st.dataframe(necessidades)