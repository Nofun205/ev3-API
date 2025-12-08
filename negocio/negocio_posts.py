import requests
from prettytable import PrettyTable


def obtener_posts_api(url):
    tabla_posts = PrettyTable()
    tabla_posts.field_names=['N°','Título','Contenido','Usuario']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            tabla_posts.add_row([
                post['id'],
                post['title'],
                post['body'],
                post['userId']])
    print(tabla_posts)