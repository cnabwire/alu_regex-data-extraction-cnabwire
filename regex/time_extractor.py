import re

def extract_times(text):
    pattern = r'(?:1[0-2]|0?[1-9]):(?:[0-5][0-9])(?:\s?(?:AM|PM))?|(?:2[0-3]|[01]?[0-9]):(?:[0-5][0-9])'
    return re.findall(pattern, text)
