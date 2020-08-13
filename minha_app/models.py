from django.db import models

class Usuario(models.Model):
    identificacao = models.CharField(max_length=100, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    campus = models.CharField(max_length=10, null=False, blank=False)
    data_nascimento = models.DateField(auto_now=False, null=True)
    url_foto = models.CharField(max_length=50, null=True, blank=False)
    # access_token = models.CharField(max_length=30, null=False, blank=False)
    # refresh_token = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f"Usuario: {self.identificacao}, {self.nome}"

    def __repr__(self):
        return f"Usuario: {self.identificacao}, {self.nome}"


class UsuarioSSH(models.Model):
    # https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now
    data_de_criacao = models.DateTimeField(auto_now_add=True, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_usuario = models.EmailField(max_length=254, null=False, blank=False)
    home = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"Usuario: {self.nome}, {self.nome_usuario}"

    def __repr__(self):
        return f"Usuario: {self.nome}, {self.nome_usuario}"


class UnidadeOrganizacional(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sigla = models.CharField(max_length=10, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"Unidade Organizacional: {self.sigla} - {self.nome}"

    def __repr__(self):
        return f"Unidade Organizacional: {self.sigla} - {self.nome}"