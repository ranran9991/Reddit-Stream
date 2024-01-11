import re
from langdetect import detect_langs


def get_language(text: str) -> str:
    lang_probas = detect_langs(text)
    lang = lang_probas[0].lang
    return lang


def remove_non_hebrew(text):
    # Regular expression pattern to match Hebrew characters, numbers, and punctuation
    pattern = re.compile(r'[\u0590-\u05FF0-9\s\.,;:!?"\'\-()]+')

    # Find all matches in the text
    filtered_text = ''.join(pattern.findall(text))

    return filtered_text
