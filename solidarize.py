import streamlit as st # type: ignore
import pandas as pd
import altair as alt



def nav_button(label, anchor):
    st.markdown(f'<a href="#{anchor}" style="text-decoration: none;">{label}</a>', unsafe_allow_html=True)






# Configuração do título do aplicativo
st.title('Solidarize')
#st.title(":blue[Solidarize]")



# Resumo da campanha
#st.header('Resumo da Campanha')
st.write("""
         
    A campanha **Solidarize** visa arrecadar alimentos e apoiar aqueles que enfrentam dificuldades em nossa comunidade. 
    Sua participação é fundamental e fará toda a diferença na vida de muitas famílias.

    **Como você pode ajudar:**

    📦 **Doações:** Alimentos não perecíveis.  
    🗓️ **Período:** 10/08/2024  
    📍 **Locais de arrecadação:** Principais Mercados da Cidade e Drive Thru (Comunidade Cristã Camaquã) 

    Juntos podemos :blue[mais !] :palms_up_together:
         

""")
""
""
""
""
########### DADOS DA CAMPANHA

entradas = pd.read_csv(st.secrets.gsheet.entradas).sort_values(by=['Quantidade'],ascending=False)
st.header("Acompanhe em tempo real :bar_chart:")

""
""
"" 
col1, col2 = st.columns(2)
col1.metric(label="Total Arrecadado (kg)", value="70.000")
col2.metric(label="Total Cestas Básicas", value="5000")
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





""
""
""
st.header("Itens Prioritários :warning:")
necessidades = pd.read_csv(st.secrets.gsheet.necessidades, index_col="Localidade")



st.dataframe(necessidades)