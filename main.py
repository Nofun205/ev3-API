import sys
s
from negocio.negocio_sistema import registrar_usuario_app, login_app
from negocio.negocio_users import obtener_users_api, crear_user_api, modificar_user_api, eliminar_user_api

from negocio.negocio_posts import obtener_posts_api

def mostrar_menu():
    print("\n" + "="*30)
    print("      MENÚ PRINCIPAL POO")
    print("="*30)
    print("1. Registro de Usuarios (App)")
    print("2. Login (Inicio de Sesión)")
    print("3. Obtener datos de API (GET) y guardar en BD")
    print("4. Enviar datos a API (POST)")
    print("5. Actualizar datos en API (PUT)")
    print("6. Eliminar datos en API (DELETE)")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    usuario_logueado = False
    
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            registrar_usuario_app()

        elif opcion == '2':
            if login_app():
                usuario_logueado = True
            else:
                usuario_logueado = False

        elif opcion == '3':
            if usuario_logueado:
                print("\n--- OBTENER DATOS (GET) ---")
                print("a. Usuarios")
                print("b. Publicaciones (Posts)")
                sub = input("Seleccione: ")
                url_base = "https://jsonplaceholder.typicode.com"
                
                if sub == 'a':
                    obtener_users_api(f"{url_base}/users")
                elif sub == 'b':
                    obtener_posts_api(f"{url_base}/posts")
                else:
                    print("Opción inválida")
            else:
                print("! DEBE INICIAR SESIÓN PRIMERO !")

        elif opcion == '4':
            if usuario_logueado:
                print("\n--- CREAR EN API (POST) ---")
                url = "https://jsonplaceholder.typicode.com/users"
                
                crear_user_api(url) # Se asume que crear_user_api maneja la creación de un nuevo usuario
            else:
                print("! DEBE INICIAR SESIÓN PRIMERO !")

        elif opcion == '5':
            if usuario_logueado:
                print("\n--- ACTUALIZAR EN API (PUT) ---")
                id_obj = input("Ingrese ID del usuario a modificar: ")
                url = f"https://jsonplaceholder.typicode.com/users/{id_obj}"
                modificar_user_api(url)
            else:
                print("! DEBE INICIAR SESIÓN PRIMERO !")

        elif opcion == '6':
            if usuario_logueado:
                print("\n--- ELIMINAR EN API (DELETE) ---")
                id_obj = input("Ingrese ID del usuario a eliminar: ")
                url = f"https://jsonplaceholder.typicode.com/users/{id_obj}"
                eliminar_user_api(url)
            else:
                print("! DEBE INICIAR SESIÓN PRIMERO !")

        elif opcion == '0':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()