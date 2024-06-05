import telegram

token = "7052514700:AAFNQ-MFxDyWnv3KpBY0lzte0UedHynh8-Y"
chat_id = "6941693546"
#bot = telegram.Bot(token=token)
#updates = bot.getUpdates()
#for u in updates:
#    print(u.message)

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="우나영사랑해")