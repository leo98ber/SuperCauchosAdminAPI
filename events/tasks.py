from celery import shared_task
from .models import Event
from twilio.rest import Client
# import requests
from work_shop_api import settings
import pywhatkit

@shared_task
def notify_event():

    # pywhatkit.sendwhatmsg_instantly("+584129096960", "Hey All!", tab_close=True)

    # numbers = ['584243408279', '584129096960', '584124936640']
    # for number in numbers:
    #     client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    #     message = client.messages.create(
    #         from_='whatsapp:+14155238886',
    #         body='Prueba de leonardo para envio de whatsapp responder si fue recibido',
    #         to=f'whatsapp:+{number}'
    #     )
    #
    #     if message.error_code is not None:
    #         print(f"Error al enviar el mensaje: {message.error_message}")
    #     else:
    #         print(f"Mensaje enviado exitosamente! a {number}")

    print("--------------------------------------------------------------EJECUTANDO EVENTO--------------------------------------------------------------")

