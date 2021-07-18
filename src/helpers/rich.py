from helpers.constants import COLORS
import re

def printr(text: str):
    """
    Print rich
    ==========
    Outputs text with colors

    Parameters
    ==========
    text (str):
        Text that will be printed

    """ 
    tags = re.findall("<[^>]+>", text)
    for tag in tags:
        text = re.sub(tag, f"\33[{COLORS[tag]}m", text)

    print(text)
