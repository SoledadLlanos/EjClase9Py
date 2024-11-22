#Ej1: Cree una funcion que calcule el promedio de N notas

def calcular_promedio():
    n = input("Ingrese una cantidad de notas a promediar: ")
    if n.isdigit():
        n=int(n)
        total_notas=0
        for i in range(n):
            nota=input("Ingrese nota: ")
            if nota.isdigit():
                nota = int(nota)
                total_notas += nota
            else:
                print("El valor ingresado es no es un numero. Por favor, ingrese un numero: ")  
        promedio = total_notas/n
        print(f"El promedio de las notas ingresadas es:{promedio}")
    else:
        print("El valor ingresado es no es un numero. Por favor, ingrese un numero: ")

calcular_promedio()

'''Ej2: Cree una funcion que determine si un color es primario o no, se debe imprimir por
pantalla la leyenda “el color X es primario “ o “el color X no es primario”'''

def color_primario(color):
    if color.isalpha():
        color=color.lower()
        if color == "rojo" or color == "verde" or color == "azul":
            print(f"el color {color} es primario")
        else: 
            print(f"el color {color} NO es primario")
    else: 
        print("El valor ingresado no es una palabra")

color_primario("azul")

#Ej3: Cree una funcion que determine que numero de una serie de N numeros es mayor

def calcular_mayor():
    n = int(input("Ingrese cuantos numeros quiere analizar: "))
    piso = 0
    for i in range(n):
        num = int(input(f"Ingrese el numero: "))
        if num >= piso:
            piso = num 
    print(f"El mayor de todos es {piso}")
    
calcular_mayor()

#Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el usuario

def dibujar_rectangulo():
    filas= int(input("ingrese un numero de filas deseadas:"))
    columnas=int(input("ingrese un numero de columnas deseadas:"))
    for i in range(filas):
        for j in range(columnas):
            if i==0 or i==filas - 1 or j ==0 or j == columnas-1:
                print("x",end="")
            else:
                print(" ",end="")
        print()
    
dibujar_rectangulo()

#Cree una funcion que calcule el Factorial de un numero entero positivo

def calcular_factorial(numero):
    factorial = 1
    i = 1
    while (i <= numero) and numero > 0:
        factorial = factorial * i
        i = i + 1
    print (f"El factorial de {numero} es {factorial}")
    
calcular_factorial(7)
    
            
    
