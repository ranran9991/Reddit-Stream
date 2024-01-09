import requests
from src.transformers.consts import API_KEY, TRANSLATE_API_URL

headers = {"Authorization": f"Bearer {API_KEY}"}


def translate_eng_to_hebrew(text: str) -> str:
    def query(payload):
        response = requests.post(TRANSLATE_API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": f"{text}",
        "parameters": {"src_lang": "heb_IL", "tgt_lang": "en_XX"}
    })
    output_text = output[0]['translation_text']
    return output_text


print(translate_eng_to_hebrew('אני רוצה לקנות תפוח'))
