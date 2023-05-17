import string
import random

def generador_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def main():
    longitud = int(input("¿De cuántos caracteres quieres tu contraseña?: "))
    contraseña = generador_contraseña(longitud)
    print(f"Tu contraseña aleatoria es: {contraseña}")

if __name__ == "__main__":
    main()
