from langchain import PromptTemplate
from langchain.llms import OpenAI, OpenAIChat


template = """
    Nedan är en text som kan ha felstavade ord, ord som saknas eller grammatiska fel.
    Din uppgift är att:
    - Ge en text där felen är rättade. Om det inte finns några av ovan listade fel, gör inga ändringar.
    - Efter texten, skriv en punktlista med alla rättningar som gjordes och varför de gjordes.
    - Om texten inte innehåller någon begriplig text, skriv: "Jag förstår tyvärr inte." och skriv inga rättningar.
    - Ge svaret på {language}

    Below is the text and language:
    LANGUAGE: {language}
    TEXT: {text}
    
    YOUR {language} RESPONSE:
"""


prompt = PromptTemplate(
    input_variables=["language", "text"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    #llm = OpenAI(temperature=.0, openai_api_key=openai_api_key)

    llm =  OpenAIChat(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=openai_api_key)
    return llm



def hämta_rättat_text_och_förklaring(option_language, text_input, llm):
    prompt_with_text = prompt.format(language=option_language, text=text_input)
    formatted_text = llm(prompt_with_text)
    return formatted_text