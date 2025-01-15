import logging
logging.basicConfig(level=logging.DEBUG)

def buggy_function(a,b):
    result = a*b
    logging.debug(f"a: {a} b: {b} resutl: {result}")
    return result

print(buggy_function(2,3))
input("")