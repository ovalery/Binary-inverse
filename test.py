#python 3.4

def Binary_inverse(data):
    
    if data[0] == 0:
        return [0]
          
# Перевод числа с основанием (-2) в число с основанием 10    
    data.reverse()  
   
  
    dec = 0
    for i in range(len(data)):
        dec = dec * (-2) + data[i]
       
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
