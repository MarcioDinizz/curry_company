import streamlit as st
from PIL import Image

st.set_page_config (
    page_title="Home",
    page_icon=" "
)    
# image_path = 'logo.jpg'
image = Image.open('logo.jpg')
st.sidebar.image(image, width=120 )
    
st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('# Fastest Delivery in Town')
st.sidebar.markdown("""-----""")
    
st.write("# Curry Company Growth Dashbord")
    
st.markdown(
    """
    Growth Dashboard foi construído para acampanhar as métricas de crescimento dos Esntrgadores e Restaurantes.
    ### Como utilizar esses Growth Dashboard?
    - Visão Empresa:
      - Visão Gerencial: Métricas gerais de compartamento.
      - Visão Tática: Indicadores semanais de crescimento.
      - Visão Grográfica: Insights de geolocalização.
    - Visão Entragdor:
      - Acompanhamento dos indicadores semanais de crescimento
    - Visão Restaurante:
     - Indicadores semanais de crescimento dos restaurantes 
    ### Ask for Help
    - Time de Data Science do Discord
     - @maeigarom
""" )     
    
    
  
    