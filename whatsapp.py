import pywhatkit as kit

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

# Example: Send a message to +9118384760 at 12:30 PM
send_whatsapp_message(9118384760, "Elvish Bhai")
