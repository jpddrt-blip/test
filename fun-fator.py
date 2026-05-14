def fat(n):
    resultado = 1
    if n > 1:
        resultado = n * fat(n-1)
    
    
    return resultado

    
print(fat(5))