"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    longitud = len(result)
    i = 1
    while (i<= longitud + 2):
        result.insert(i,"@")
        i = i+2
    return result
