def suma(c,d):
    # Los argumentos pueden llamarse como quiera lo importante es que ocupen los mismos lugares
    # y que se hagan referencia a ellos dentro de la funcion
    # r es una variable que almacena la respuesta de la funcion y tambien puede ser llamada como qiera

    r=c+d
    return r


a=float(input('introduce un numero:'))
b=float(input('introduce otro numero:'))

#Los argumentos que se envian a una funcion deben llamarse igual a las variables locales.
res=suma(a,b)

print ('el resultado de {} y {} es {}'.format (a,b,res))

