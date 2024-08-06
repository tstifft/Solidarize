import streamlit as st # type: ignore
import pandas as pd
import altair as alt



def nav_button(label, anchor):
    st.markdown(f'<a href="#{anchor}" style="text-decoration: none;">{label}</a>', unsafe_allow_html=True)






# Configuração do título do aplicativo
st.title('Solidarize')
#st.title(":blue[Solidarize]")
""
""
tab1, tab2, tab3 = st.tabs(["A Campanha", "Acompanhe", "Prioridades :warning:"])

with tab1:
    # Resumo da campanha
    st.header('A Campanha')
    st.write("""
            
    A campanha **Solidarize** visa arrecadar alimentos e apoiar aqueles que enfrentam dificuldades em nossa comunidade. 
    Sua participação é fundamental e fará toda a diferença na vida de muitas famílias.

    **Como você pode ajudar:**

    📦 **Doações:** Alimentos não perecíveis.  
    🗓️ **Período:** 10/08/2024  
    📍 **Locais de arrecadação:**  
            
    - Principais Mercados da Cidade  
        - SUPER SÃO JOSÉ (B. SÃO JOSE)  
        - SUPER SÃO JOSÉ (B. Viégas)  
        - SUPERMERCADO NACIONAL  
        - SUPERMERCADO KROLOW   
        - SUPERMERCADO PRADO  
        - SUPERMERCADO HÍPICO  
        - SUPERMERCADO CARLAU  
        - SUPERMERCADO ROXO    
        - SUPERMERCADO SCHMEGEL   
            

    - Drive Thru
        - Av. Jose Loureiro da Silva, 787 - Carvalho Bastos, Camaquã - RS, 96784-058
        - ...
            

    Juntos podemos :blue[mais !] :palms_up_together:
            

    """)
    ""
    ""
    ""
    ""

with tab2:

########### DADOS DA CAMPANHA

    entradas = pd.read_csv(st.secrets.gsheet.entradas).sort_values(by=['Quantidade'],ascending=False)
    st.header("Acompanhe em tempo real")

    ""
    ""
    "" 
    #col1, col2 = st.columns(2)
    #col1.metric(label="Total Arrecadado (kg)", value="70.000")
    #col2.metric(label="Total Cestas Básicas", value="5000")
    st.write(""" 
    ##### Até agora com a sua ajuda já arrecadamos ...
    ## **:blue[500.000]** Kgs 
    ''
    
    ##### E com isso já conseguimos montar
    ## 300 cestas básicas
             
                    
    """)
    #col1, col2, col3 = st.columns(3)
    #col2.metric(label="Total Arrecadado (kg)", value="70.000")


    #st.write(""" 
    ##### E já conseguimos montar **700** cestas básicas !
             
    #""")

    ""
    ""
    ""
    #st.bar_chart(entradas, x="Localidade", y="Quantidade", horizontal=True)
    # Gráfico de barras com Altair
    st.header('Total de Alimentos Arrecadados')
    chart = alt.Chart(entradas).mark_bar(color='skyblue').encode(
        x=alt.X('Localidade:N', title='Localidade'),
        y=alt.Y('Quantidade:Q', title='Quantidade'),
        tooltip=['Localidade', 'Quantidade']
    ).properties(
        title='Quantidade Total de Alimentos Arrecadados'
    )
    st.altair_chart(chart, use_container_width=True)



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