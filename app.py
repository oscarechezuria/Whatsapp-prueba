from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app= Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    
    incoming_message= request.form.get("Body").strip()
    sender= request.form.get("From")
    
    response= MessagingResponse()
    
    if incoming_message.lower() == "hola oscar":
        response.message("Muy bien y tu?")
    else:
        response.message("Lo siento, no entendi tu mensaje")
    
    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)