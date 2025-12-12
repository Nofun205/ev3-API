from modelos import Usuario
from datos import insertar_objeto, sesion
from auxiliares.encriptacion import Encriptador

def registrar_usuario_app():
    print("\n--- REGISTRO DE USUARIO ---")
    username = input("Ingrese nombre de usuario: ")
    email = input("Ingrese correo: ")
    password = input("Ingrese contraseña: ")

    # Encriptamos
    pass_encriptada, salt = Encriptador.encriptar(password)

    nuevo_usuario = Usuario(
        username=username,
        email=email,
        contrasena=pass_encriptada,
        sal=salt
    )

    try:
        insertar_objeto(nuevo_usuario)
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar: {e}")

def login_app():
    print("\n--- INICIO DE SESIÓN ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    # Buscamos al usuario por nombre
    usuario_encontrado = sesion.query(Usuario).filter_by(username=username).first()

    if usuario_encontrado:
        # Validamos la contraseña usando nuestra clase Encriptador
        if Encriptador.validar(password, usuario_encontrado.contrasena):
            print(f"¡Bienvenido {usuario_encontrado.username}!")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("Usuario no encontrado.")
        return False