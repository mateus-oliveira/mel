#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import ldap3
import getpass
import pwd
import grp
import syslog
import stat
import string
import random

class Curso:
    def __init__(self, codigo, abreviacao, descricao):
        self.codigo = codigo
        self.abreviacao = abreviacao
        self.descricao = descricao
        
dados_cursos = [
        ('14403', 'redes', 'Técnico de Nível Médio em Redes de Computadores, na Forma Subsequente'),
        ('14401', 'info', 'Técnico de Nivel Médio em Informática, na Forma Integrado (2012)'),
        ('14806', 'tsi', 'Tecnologia em Sistemas para Internet (2012)'),
        ]

cursos = {codigo: Curso(codigo, abreviacao, descricao) for (codigo, abreviacao, descricao) in dados_cursos}

codigos_permitidos = ['14403']

# Fonte: https://stackoverflow.com/questions/19213232/python-v3-random-password-generator
def criar_senha_aleatoria():
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    senha = ''.join([random.choice(caracteres) for _ in range(10)])
    return senha

def fatia(matricula: str):
    pos = {
           'ano_per': (0, 5),
           'cod_curso': (5, 10),
           'cod_est': (10, 15)
          }

    dados = {k:matricula[slice(*v)] for (k,v) in pos.items()}
    return dados

def criar_usuario(nome_usuario: str, nome_completo:str, matricula: str, campus:str, senha: str) -> bool:
    os.system(f"sudo lxc exec mange /usr/local/bin/mel-criar-usuario {nome_usuario} '{nome_completo}' {matricula} {campus} {senha}")

'''    campus_dir = f'/home/{campus}'
    os.makedirs(campus_dir, mode=0o750, exist_ok=True)
    os.system(f'chgrp {grupo} {campus_dir}')
    os.system(f'groupadd {grupo}')

    comando = f"useradd --base-dir {campus_dir} --create-home --comment '{nome_completo},{matricula}' --shell /bin/bash {usuario}"
    os.system(comando)
    os.chmod(f'{campus_dir}', stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP)
    os.system(f'usermod -aG {grupo} {usuario}')
    senha_linux = criar_senha_aleatoria()
    cmd_senha = f'echo {usuario}:{senha_linux} | chpasswd'
    os.system(cmd_senha)
    os.system(f'chage -d 0 {usuario}')
'''

#if len(matricula) == 14:
#    dados_mat = fatia(matricula)
#    grupo = cursos[dados_mat['cod_curso']].abreviacao+dados_mat['ano_per']
#    #if dados_mat['cod_curso'] not in codigos_permitidos:
#    #    print('Sinto muito, mas aqui na Mange não está liberada a criação de contas para seu curso.')
#    #    sys.exit(2)
#else:
#    grupo = 'professor' # TODO. Chute. Pode ser um servidor técnico-administrativo.
#    
#servidor = ldap3.Server(host='10.22.0.155', get_info=ldap3.ALL)
#
#if True:
#   conexao = ldap3.Connection(servidor, user=f'{matricula}@ifrn.local', password=senha, auto_bind=True)
#   base = "dc=ifrn, dc=local"
#   criterio = f"(&(objectClass=user)(sAMAccountName={matricula}))"
#   conexao.search(search_base=base,
#                  search_filter=criterio,
#                  attributes=ldap3.ALL_ATTRIBUTES)
#
#   respostas = conexao.response_to_json()
#   with open(f'/var/lib/dysconta/{matricula}.json', 'w') as bkp:
#       bkp.write(respostas)
#
#   dados = conexao.entries[0]
#   conexao.unbind()
#   # conexao.entries[0].entry_to_json()
#   # https://www.programcreek.com/python/example/107944/ldap3.ALL
#   
#   if dados:
#      email = dados['extensionAttribute5'].value
#      usuario = email.split('@')[0]
#      nome_completo = dados['displayName'].value
#      # grupos = dados['memberOf'][0].split(',')
#      print('Agora será criado o usuário "{}"'.format(usuario))
#      group_dir = f'/home/{grupo}'
#      os.makedirs(group_dir, mode=0o750, exist_ok=True)
#      os.system(f'chgrp {grupo} {group_dir}')
#      os.system(f'groupadd {grupo}')
#
#      comando = f"useradd --base-dir {group_dir} --create-home --comment '{nome_completo},{matricula}' --shell /bin/bash {usuario}"
#      os.system(comando)
#      os.chmod(f'{group_dir}', stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR|stat.S_IRGRP|stat.S_IXGRP)
#      os.system(f'usermod -aG {grupo} {usuario}')
#      senha_linux = criar_senha_aleatoria()
#      cmd_senha = f'echo {usuario}:{senha_linux} | chpasswd'
#      os.system(cmd_senha)
#      os.system(f'chage -d 0 {usuario}')
#      try:
#         dados_usuario = pwd.getpwnam(usuario) 
#         home = dados_usuario.pw_dir
#         if dados:
#             mensagem = "Criacao da conta {}".format(usuario)
#             os.system('etckeeper commit "{}"'.format(mensagem))
#             syslog.syslog(syslog.LOG_INFO, mensagem)
#
#
