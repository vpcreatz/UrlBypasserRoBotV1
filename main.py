from pyrogram import Client, filters
from pybypasser import Bypasser

api_id = '20960397'
api_hash = 'd68d847d3abb2087bf74f5d0683c2993'
bot_token = '6195431573:AAGzo189bV07zowDnL2bm0pV2OOdxhSpvQ4'

bot = Client('bypass_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
bypasser = Bypasser()

@bot.on_message(filters.command('bypass'))
def handle_bypass_command(client, message):
    if len(message.command) < 2:
        message.reply_text('Please provide a URL to bypass.')
        return
    url = message.command[1]
    bypassed_url = bypasser.bypass(url)
    message.reply_text(bypassed_url)

bot.run()
