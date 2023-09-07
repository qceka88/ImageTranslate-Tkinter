import re


def input_data_regex_validation(input_text):
    result = re.match(r"^[a-zA-Z]{2}$|^[a-zA-Z]{2}-[a-zA-Z]{2}$", input_text)
    if result:
        return result.group().lower()
