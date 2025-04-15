import asyncio
from telegram_bot.bot_logic import send_message_to_telegram

# Ejecutar el envío de mensaje
async def main():
    await send_message_to_telegram("Hola, Jeisson! Este es un mensaje de prueba desde el bot.")

# Iniciar el loop de asyncio
asyncio.run(main())
