import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

account_sid= os.getenv("TWILIO_ACCOUNT_SID")
auth_token= os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number= os.getenv("TWILIO_PHONE_NUMBER")
print(twilio_phone_number)

client= Client(account_sid,auth_token)

def send_whatsapp_message(to, message):
    try:
        # Enviar el mensaje de WhatsApp
        msg = client.messages.create(
            from_=twilio_phone_number,
            body=message,
            to=f'whatsapp:{to}'
        )
        print(f"Mensaje enviado correctamente. SID: {msg.sid}")
    except Exception as e:
        print(f"Error enviando el mensaje: {e}")
    
if __name__ == "__main__":
    to_number = "+584127231955"
    text = "Mi nombre es oscar, como estas?"
    send_whatsapp_message(to_number, text)