import re
from langdetect import detect_langs


def is_mostly_hebrew(text: str) -> bool:
    lang_probas = detect_langs(text)
    for prob in lang_probas:
        if prob.lang == 'he' and prob.prob >= 0.9:
            return True
    return False


def remove_non_hebrew(text):
    # Regular expression pattern to match Hebrew characters, numbers, and punctuation
    pattern = re.compile(r'[\u0590-\u05FF0-9\s\.,;:!?"\'\-()]+')

    # Find all matches in the text
    filtered_text = ''.join(pattern.findall(text))

    return filtered_text
