import re

def convert_unicode_fraction_to_string(fraction:str) -> str:
    fraction_map = {
            "½": "1/2",
            "⅓": "1/3",
            "⅔": "2/3",
            "¼": "1/4",
            "¾": "3/4",
            "⅕": "1/5",
            "⅖": "2/5",
            "⅗": "3/5",
            "⅘": "4/5",
            "⅙": "1/6",
            "⅚": "5/6",
            "⅛": "1/8",
            "⅜": "3/8",
            "⅝": "5/8",
            "⅞": "7/8",
        }
    if (fraction.strip() in fraction_map):
        return fraction_map[fraction.strip()]
    else:
        return fraction

def replace_unicode_fractions(text:str) -> str:
    pattern = r"([\u00BC-\u00BE\u2150-\u215E])"
    output = re.sub(pattern,
                    lambda m:convert_unicode_fraction_to_string(m.group(0)),
                    text)
    return output

if __name__ == "__main__":
    text = input("Enter a string:")
    output = replace_unicode_fractions(text)
    print(output)
