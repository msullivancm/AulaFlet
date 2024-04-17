import flet as ft
import os
from flet.security import encrypt, decrypt
import secrets

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50

    #Chave criptográfica deve ser adquirida nas variáveis de ambiente
    #secret_key = os.getenv("SECRET_KEY")
    secret_key = secrets.token_hex(30)

    #Criptografar
    texto = "Testo de exmplo para ser criptografado e depois descriptografado"

    texto_criptografado = encrypt(texto, secret_key)
    page.add(ft.Text('Texto Criptografado: ' + texto_criptografado, size=20))

    texto_descriptografado = decrypt(texto_criptografado, secret_key)
    page.add(ft.Text('Texto Descriptografado: ' + texto_descriptografado, size=20))

    page.client_storage.set('senha', texto_criptografado)
    print(page.client_storage.get('senha'))

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
