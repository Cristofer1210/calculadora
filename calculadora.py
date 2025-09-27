# calculadora.py
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def mostrar_menu():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    print("Bienvenido a la calculadora simple.")
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción (1-5): ")
        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                if opcion == '1':
                    print(f"{num1} + {num2} = {sumar(num1, num2)}")
                elif opcion == '2':
                    print(f"{num1} - {num2} = {restar(num1, num2)}")
                elif opcion == '3':
                    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcion == '4':
                    print(f"{num1} / {num2} = {dividir(num1, num2)}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
# Una calculadora simple que realiza operaciones básicas: suma, resta, multiplicación y división.