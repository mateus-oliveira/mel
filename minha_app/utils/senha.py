import string
import random
# import os

def criar_senha():
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    senha = ''.join([random.choice(caracteres) for _ in range(10)])
    return senha

    # comando = f"""useradd 
    # --base-dir {group_dir} 
    # --create-home --comment '{nome_completo},{matricula}' 
    # --shell /bin/bash 
    # {usuario}
    # """
    # os.system(comando)