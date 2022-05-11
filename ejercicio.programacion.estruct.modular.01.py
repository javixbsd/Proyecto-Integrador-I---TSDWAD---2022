'''Ejercicio Programación estructurada y modular:
1. Realice un programa que contengan funciones de los tres tipos de triángulos. Los mismos deben estar
acompañados de los mensajes respecto a la función decoradora. Para mejorarlo pueden agregar los
nombres de cada función según los triángulos.'''


from ctypes.wintypes import LPWIN32_FIND_DATAA


def main():
    "Ingreso de datos"
    print("Ingrese los lados de un triangulo, el programa te dira que tipo de triangulo es")
    l1 = float(input("\nIngrese el primer lado: "))
    l2 = float(input("\nIngrese el segundo lado: "))
    l3 = float(input("\nIngrese el tercer lado: "))
    if l1 == l2 == l3 :
        equilatero(l1,l2,l3)
    if l1 != l2 and l1 != l2 and l2 != l3:
        escaleno(l1,l2,l3)    
    else:
        isosceles(l1,l2,l3)

def equilatero(l1,l2,l3):
    "funcion triangulo equilatero"
    p = l1 + l2 + l3
    print("El triangulo es equilatero y su perimeto es:", p)
    exit()

def escaleno(l1,l2,l3):
    "funcion triangulo escaleno"
    p = l1 + l2 + l3
    print("El triangulo es ecaleno y su perimeto es:", p)

def isosceles(l1,l2,l3):
    "funcion triangulo isosceles"
    p = l1 + l2 + l3
    print("El triangulo es isosceles y su perimeto es:", p)

main()