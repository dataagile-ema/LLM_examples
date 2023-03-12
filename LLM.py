from langchain import PromptTemplate
from langchain.llms import OpenAI, OpenAIChat

template = """
    Below is an text that may have misspelled words, missing words and gramathical error.
    Your goal is to:
    - Give a text where the errors are correct. If there are no errors in the text, do not make any changes-
    - After the text write a bullet list describing what was corrected in the text and why it was changed.
    - If the text does not contain meningful wors, write: "Jag förstår tyvärr inte." and dont write any corrections.
    - Give answer in {language}

    Below is the text and language:
    LANGUAGE: {language}
    TEXT: {text}
    
    YOUR {language} RESPONSE:
"""

template = """
    Nedan är en text som kan har felstavade ord, ord som saknas eller gramatiska fel.
    Din uppgift är att:
    - Ge en text där felen är rättade. Om det inte finns några av ovan listade fel, gör inga ändringar.
    - Efter texten, skriv en punktlista med alla rättningar som gjores och varför de gjordes.
    - Om texten inte innhåller någon begriplig text, skriv: "Jag förstår tyvärr inte." and dont write any corrections.
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