# coding: utf-8
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Usuario, UsuarioSSH
from mel.local_settings import EMAIL_HOST_USER
from .utils.senha import criar_senha

import markdown
import requests

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'index.html', {})

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'profile.html', {})

def extra_data(request):
    dados = request.user.social_auth.get().extra_data
    resposta = requests.get(
        url='https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/',
        headers={'Authorization': 'Bearer {0}'.format(dados['access_token'])}
    )
    print(resposta.text)
    return HttpResponse(f'{dados}, {resposta.text}')

@login_required
def ssh(request):
    nome_usuario = request.user.email.split('@')[0]
    usuario = UsuarioSSH.objects.filter(nome_usuario=nome_usuario)
    return render(request, 'ssh.html', {'usuario_ssh': usuario})
    
@login_required
def ssh_iniciar(request):
    return HttpResponse('liga SSH')

@login_required
def ssh_criar(request):
    # Codigo para mandar email
    # Verificar se não existe
    user = request.user
    nome_usuario = user.email.split('@')[0]

    usuario_ssh = UsuarioSSH.objects.filter(nome_usuario=nome_usuario)
    usuario_app = Usuario.objects.filter(identificacao=user)

    if usuario_ssh:
        return HttpResponse(f'{usuario_ssh[0].nome}')
    else: 
        UsuarioSSH.objects.create(
            nome=user.get_full_name(),
            nome_usuario=nome_usuario,
            home=f'/home/{usuario_app[0].campus.lower()}/{nome_usuario}/'
        )

        senha_linux = criar_senha()

        mensagem = f'''
# Conta SSH

{user.get_full_name()}, sua conta foi criada com sucesso. Agora siga os seguintes passos:

Antes de acessar a Mange via SSH, você deve iniciar o serviço a partir do link: <https://mange.ifrn.edu.br/ssh>

1. Encerre esta sessão da conta estudante `(CTRL+D ou comando "exit")`;
2. Inicie uma sessão com seu usuário:
    * `ssh {nome_usuario}@mange.ifrn.edu.br`
3. Quando solicitada, ofereça a senha: `{senha_linux}`
4. Será solicitada a troca desta senha:

    1. Digite a senha atual: `{senha_linux}`
    2. Digite a nova senha
    3. Repita a nova senha

5. Sua sessão foi automaticamente encerrada após a troca da senha.
6. Repita o comando do passo (2).
7. Seja bem-vindo(a) à Mange.
    
Divirta-se!
'''

        md = markdown.Markdown(output_format='html')
        mensagem_html = md.convert(mensagem)

        send_mail(
            subject="Bem vind@!",
            message=mensagem,
            html_message=mensagem_html,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True,
        )

        return HttpResponse('Usuário criado!')
