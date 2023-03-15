
import streamlit as st
from LLM import load_LLM, hämta_rättat_text_och_förklaring, template
import os

openai_api_key = os.getenv('API_KEY_OPEN_AI')
llm = load_LLM(openai_api_key=openai_api_key)
    
st.set_page_config(page_title="Rätta och förklara", page_icon=":robot:")
st.header("Hitta skrivfelen")

st.markdown("AI-modellen hittar skrivfel och förklarar de ändringar som behöver göras i texten. Appen använder Open AI-modellen gpt-3.5-turbo.")
st.markdown("#### Skriv in text att rätta")

if 'kor_ratta_text' not in st.session_state:
    st.session_state['kor_ratta_text'] = False

if 'text_input' not in st.session_state:
    st.session_state['text_input'] = ""

option_language = 'Swedish'

def update_text_with_example():
    st.session_state.text_input = "Vill du ha äppla? Är du större än mig?"
    text_input_x = st.session_state.text_input
    st.session_state.kor_ratta_text = True


text_input_ta = st.text_area(label="",  placeholder="Din text...", key="text_input")

def rattatext():
    st.session_state.kor_ratta_text = True
    st.session_state.text_input = text_input_ta

col1, col2 = st.columns(2)

with col1:
    st.button("Rätta text", help="Klicka för att se exmpel på text som kan rättas.", on_click=rattatext)
with col2:
    st.button("*Text-exempel*", help="Klicka för att se exmpel på text som kan rättas.", on_click=update_text_with_example)


st.markdown("#### Den rättade texten:")
if st.session_state.kor_ratta_text == True:
    l = len(st.session_state.text_input.split(" "))
    if l > 100:
        st.write("Texten behöver vara kortare")
        st.stop()
    if len(st.session_state.text_input) == 0:
        st.write("Skriv en text i textrutan")
        st.stop()
        
    with st.spinner(text="In progress..."):
        svar = hämta_rättat_text_och_förklaring(option_language, st.session_state.text_input, llm)
    st.write(svar)


with st.expander(label= "Se promptmall som appen använder", expanded=False):
    st.text_area(label = "promptmall", value= template)

st.markdown('![Tick](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://dataagile-ema-llm-examples-llm-app-drtt1h.streamlit.app/&label=Tick&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')