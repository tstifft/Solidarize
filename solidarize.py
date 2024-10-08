import streamlit as st # type: ignore
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)




def nav_button(label, anchor):
    st.markdown(f'<a href="#{anchor}" style="text-decoration: none;">{label}</a>', unsafe_allow_html=True)



# Configuração do título do aplicativo


# st.title(':blue[Solidarize]')
st.markdown(f"<h1 style='text-align: left; color: #028BF9; font-size: 7vmax'>Solidarize</h1>", unsafe_allow_html=True)
    

tab1, tab2, tab3 = st.tabs(["**Saiba mais**", "**Acompanhe**", "**Prioridades**"])

with tab1:
    # Resumo da campanha
    # st.header('Saiba mais')
    st.write("""
            
    A campanha **Solidarize** ocorre anualmente e visa arrecadar alimentos e apoiar aqueles que enfrentam dificuldades em nossa comunidade.
     
    Sua participação fará toda a diferença na vida de muitas famílias.

    **Como você pode ajudar:**

    📦 **Doações:** Alimentos não perecíveis.  
    🗓️ **Período:** 10/08/2024  
    📍 **Locais de arrecadação:** 
            
    - Principais Mercados da Cidade  
    - Drive Thru
        - **Camaquã**: Av. Jose Loureiro da Silva, 787 - Carvalho Bastos, Camaquã - RS, 96784-058
        - **Cristal**: Rua Pedro Osório, 109 - Centro, Cristal - RS, 96195-000
        - **Tapes**: Av. Borges de Medeiros, 156, Tapes - RS, 96760-000
        
            

    Juntos podemos :blue[mais !] :palms_up_together:
            

    """)


with tab2:

########### DADOS DA CAMPANHA

    entradas = pd.read_csv(st.secrets.gsheet.entradas).sort_values(by=['Quantidade'],ascending=False)
    st.header("Juntos já arrecadamos  ...")

    ""
    col1,col2 = st.columns(2)
    
    total_kgs = '{0:,}'.format(entradas["Quantidade"].sum()).replace(',','.')
    
    
    tile1 = col1.container(height=200)
    tile1.markdown(f"<h1 style='text-align: center; color: #028BF9; font-size:70px'>{total_kgs}</h1>", unsafe_allow_html=True)
    ""
    tile1.markdown("<h3 style='text-align: right; color: #028BF9;'>Quantidade (Kgs)</h3>", unsafe_allow_html=True)
 

    total_cestas = '{0:,}'.format(entradas["Cestas"].sum()).replace(',','.')


    tile2 = col2.container(height=200)
    tile2.markdown(f"<h1 style='text-align: center; color: #028BF9; font-size:70px'>{total_cestas}</h1>", unsafe_allow_html=True)
    tile2.markdown("<h3 style='text-align: right; color: #028BF9;'>Cestas Básicas Montadas</h3>", unsafe_allow_html=True)
    
    #col1, col2, col3 = st.columns(3)
    #col2.metric(label="Total Arrecadado (kg)", value="70.000")


    #st.write(""" 
    ##### E já conseguimos montar **700** cestas básicas !
             
    #""")

    "veja por localidade aqui 	:point_down:"
    ""
    ""
    ""
    
    # Gráfico de barras com Altair
    # color='blues'
    chart = alt.Chart(entradas).mark_bar().encode(
        x=alt.X('Localidade:N',axis=alt.Axis(title='') ),
        y=alt.Y('Quantidade:Q',axis=alt.Axis(labels=False, title='Qtd em KGs')),
        tooltip=['Localidade', 'Quantidade']
    ).properties(
        title='Quantidade (kgs) por Localidade'
    )
    st.altair_chart(chart, use_container_width=True)

    chart2 = alt.Chart(entradas).mark_bar().encode(
        x=alt.X('Localidade:N',axis=alt.Axis(title='') ),
        y=alt.Y('Cestas:Q',axis=alt.Axis(labels=False, title='Qtd Cestas')),
        tooltip=['Localidade', 'Cestas']
    ).properties(
        title='Quantidade de Cestas por Localidade'
    )
    st.altair_chart(chart2, use_container_width=True)

with tab3:

    ############## ITENS PRIORITARIOS
    st.header("Itens Prioritários")
    necessidades = pd.read_csv(st.secrets.gsheet.necessidades, index_col='Localidade')

    # "Esses são os itens prioritários em cada localidade"
    ":red[*Isso nos ajuda a termos uma distribuição adqueada para montagem das cestas básicas*]"
    
    st.dataframe(necessidades, use_container_width=True)
    
    # locais = necessidades['Localidade'].unique()
    
    # for local in locais:
    #     st.write(f"##### {local}")
    #     df_filter = necessidades[necessidades['Localidade'] == local]
    #     produtos = df_filter['Produto'].unique()
    #     for prod in produtos:
    #         st.write(f' - {prod}')
    #     ""
    #     ""