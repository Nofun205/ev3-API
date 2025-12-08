import requests
from prettytable import PrettyTable


def obtener_users_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names=['N°','Nombre','Nombre Usuario','Correo','Latitud']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_usuarios = respuesta.json()
        for usuario in listado_usuarios:
            tabla_usuarios.add_row([
                usuario['id'],
                usuario['name'],
                usuario['username'],
                usuario['email'],
                usuario['address']['geo']['lat']])
    print(tabla_usuarios)

def crear_user_api(url):
    nombre = input('Nombre: ')
    nomre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    web = input('Web: ')
    
    user = {
    "name": nombre,
    "username": nomre_usuario,
    "email": correo,
    "phone": telefono,
    "website": web
    }
    
    respuesta = requests.post(url,data=user)
    print(f'{respuesta.text} {respuesta.status_code}')

def modificar_user_api(url):
    nombre = input('Nombre: ')
    nomre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    web = input('Web: ')
    
    user = {
    "name": nombre,
    "username": nomre_usuario,
    "email": correo,
    "phone": telefono,
    "website": web
    }
    
    respuesta = requests.put(url,data=user)
    print(respuesta.text)

def eliminar_user_api(url):    
    respuesta = requests.delete(url)
    print(respuesta.text)

def guardar_user_db():
    pass

def modificar_user_db():
    pass

def eliminar_user_db(arg):
    pass