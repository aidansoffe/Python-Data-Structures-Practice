def calculate(operation, a, b, make_int=False, message='The result is'):
 
    

    if operation == 'add':
        res = a + b
    elif operation == 'substract':
        res = a - b
    elif operation == 'multiply':
        res = a * b
    elif operation == 'divide':
        res = a / b
  
    if make_int:
        res = int(res)
         
    return f"{message} {res}"

print (calculate('add', 4, 2))        

