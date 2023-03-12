
import streamlit as st
from LLM import load_LLM, hämta_rättat_text_och_förklaring, template
import os


st.set_page_config(page_title="Rätta och förklara", page_icon=":robot:")
st.header("Rätta och förklara skrivfel")

st.markdown("Se vilka fel i stavning och grammatik en text har. Få den korrekta texten utskriven. Appen använder Open AI-modellen gpt-3.5-turbo.")
st.markdown("## Skriv in text att rätta")


openai_api_key = os.getenv('API_KEY_OPEN_AI')

option_language = 'Swedish'

def get_text():
    input_text = st.text_area(label="Textfält",  placeholder="Din text...", key="text_input")
    return input_text

text_input = get_text()

if len(text_input.split(" ")) > 100:
    st.write("Texten behöver vara kortare")
    st.stop()

def update_text_with_example():
    print ("in updated")
    st.session_state.text_input = "Hur många grisar finns det på gården? Är mångare än trä?"

st.button("*Se ett exempel*", help="Klicka för att se exmpel på text som kan rättas.", on_click=update_text_with_example)

st.markdown("### Din rättade text:")


if text_input:
    llm = load_LLM(openai_api_key=openai_api_key)
    svar = hämta_rättat_text_och_förklaring(option_language, text_input, llm)
    st.write(svar)


with st.expander(label= "Se promptmall som appen använder", expanded=False):
    st.text_area(label = "promptmall", value= template)
