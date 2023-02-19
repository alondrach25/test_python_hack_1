"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    text = "fooziman"
    text = text[::-1].capitalize()
    result = text[::-1]
    return result
