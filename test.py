#python 3.4

def binary_inverse(data):
    
    if sum(data) == 0:
        return [0]
          
# Перевод числа с основанием (-2) в число с основанием 10    
    data.reverse()  
   
  
    dec = 0
    for i in data:
        dec = dec * (-2) + i
       
# Обратное число       
    inv = dec * (-1)
        
# перевод числа с основанием 10 в число с основанием (-2)    
    binary = []  

    while inv != 0:
        inv, X = divmod(inv, -2)
        if X < 0:
            inv, X = inv + 1, X + 2
        binary.insert(0, X) 
               
    return binary
