import asyncio
from telegram import Bot

# Configuración del bot
TELEGRAM_TOKEN = "7207061325:AAFp-rKxuBhQljrDlJ3ZgUuIS8ig22M_EcY"
CHAT_ID = "6444278889"

async def send_message_to_telegram(message):
    """
    Enviar un mensaje al bot de Telegram de forma asincrónica.
    :param message: Contenido del mensaje a enviar.
    """
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Mensaje enviado a Telegram: {message}")
    except Exception as e:
        print(f"Error enviando mensaje a Telegram: {e}")
