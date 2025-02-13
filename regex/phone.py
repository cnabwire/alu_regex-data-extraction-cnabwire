import re

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}'
    return re.findall(pattern, text)
