"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    caracteres = {'O':'0', 'I':'1', 'A':'@'}
    for letra in result:
        if letra in caracteres:
            result = result.replace(letra,caracteres.get(letra))
    result = list(result)
    return result
