"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    caracteres = {'o':'0', 'i':'1', 'a':'@'}
    for letra in result:
        if letra in caracteres:
            result = result.replace(letra,caracteres.get(letra))
    return result
