import re

def extract_credit_cards(text):
    card_nummber = {}
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    card_number['credit_cards'] = re.findall(credit_card_pattern, text)
    return data
