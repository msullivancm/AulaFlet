from turtle import bgcolor
import flet as ft
import os
from flet.auth.providers import GitHubOAuthProvider
#pip install cryptography
from flet.security import encrypt, decrypt
import secrets
import json
import requests

from httpx import request

GITHUB_CLIENT_ID = 'eb3b6e5c2c63c8e04dc6'
GITHUB_CLIENT_SECRET = '1f01d828d0aee90126609bf36dae4c41b03df4ea'
SECRET = 'djgpfaoihjreopdghjaopi4124561h24' 

def main(page:ft.Page):
    page.window_width = 600.0
    page.window_height = 1039.0
    page.window_top = 0
    page.window_left = 0
    #Page resized 300.0 1039.0 0.0 1627.0
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 50
    
    page.scroll=ft.ScrollMode.AUTO

    #Não precisa logar novamente se o token já estiver salvo
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url='http://127.0.0.1:8080/api/oauth/redirect'
    )

    encrypted_token = page.client_storage.get('github_token')
    if encrypted_token:
        saved_token = decrypt(encrypted_token, SECRET)
        page.login(provider=provider, saved_token=saved_token)

    def on_login(e: ft.LoginEvent):
        if not e.error:
            token = page.auth.token.to_json()
            encrypted_token = encrypt(token, SECRET)
            page.client_storage.set('github_token', encrypted_token)
        else:
            print('Erro: ', e.error)
            print('Descrição do erro: ', e.error_description)

    page.on_login = on_login

    if page.auth:
        page.clean()
        page.add(
            ft.CircleAvatar(
                foreground_image_url=page.auth.user.get('avatar_url')
            ),
            ft.Text(
                value=page.auth.user.get('login'),
                size=30,
            ),
            ft.Text(
                value=page.auth.user.get('bio'),
                size=20,
            )
        )
        
        headers = {"Authorization": f'{page.auth.token.token_type} {page.auth.token.access_token}'}
        
        repos_resp = requests.get('https://api.github.com/user/repos', headers=headers)
        user_repos = repos_resp.json() 
        
        for repo in user_repos:
            page.add(
                ft.ListView(
                    [
                        ft.Text(repo.get('name'), size=20),
                        ft.Text(repo.get('description'), size=15),
                    ],
                    padding=50, 
                    spacing=0, 
                )
            )
    else:
        page.add(
            ft.ElevatedButton(
                text="Login com Github",
                on_click=lambda _: page.login(provider=provider)
            )
        )


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets', port=8080)
