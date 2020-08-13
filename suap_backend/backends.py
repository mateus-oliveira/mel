# coding: utf-8

from social_core.backends.oauth import BaseOAuth2
from minha_app.models import Usuario, UnidadeOrganizacional
from django.core.mail import send_mail
from django.utils.dateparse import parse_date

from mel.local_settings import EMAIL_HOST_USER, MEUS_DADOS


class SuapOAuth2(BaseOAuth2):
    name = 'suap'
    AUTHORIZATION_URL = 'https://suap.ifrn.edu.br/o/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'https://suap.ifrn.edu.br/o/token/'
    ID_KEY = 'identificacao'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = 'https://suap.ifrn.edu.br/api/eu/'
    STUDENT_DATA = MEUS_DADOS
    

    def user_data(self, access_token, *args, **kwargs):
        return self.request(
            url=self.USER_DATA_URL,
            data={'scope': kwargs['response']['scope']},
            method='GET',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        ).json()

    def get_user_details(self, response):
        """
        Retorna um dicionário mapeando os fields do settings.AUTH_USER_MODEL.
        você pode fazer aqui outras coisas, como salvar os dados do usuário
        (`response`) em algum outro model.
        """
        splitted_name = response['nome'].split()
        first_name, last_name = splitted_name[0], ''
        if len(splitted_name) > 1:
            last_name = splitted_name[-1]

        dados_extras = self.student_data(response["access_token"])

        usuario, criado = Usuario.objects.get_or_create(
            identificacao = response["identificacao"],
            nome = response["nome"],
            email = response["email"],
            campus = response["campus"],
            url_foto=dados_extras["url_foto_150x200"],
            data_nascimento=parse_date(dados_extras["data_nascimento"]),
            # access_token = response["access_token"],
            # refresh_token = response["refresh_token"],
        )
        
        if (criado):
            self.send_email(response['email'])

        return {
            'username': response[self.ID_KEY],
            'first_name': first_name.strip(),
            'last_name': last_name.strip(),
            'email': response['email'],
        }

    def send_email(self, email):
        send_mail(
            subject="Bem vind@!",
            message='Bem vind@ à aplicação do SUAP com Django',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,
        )
    
    def student_data(self, access_token):
        return self.request(
            url=self.STUDENT_DATA,
            method='GET',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        ).json()
