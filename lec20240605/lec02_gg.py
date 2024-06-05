import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
 
token = "7052514700:AAFNQ-MFxDyWnv3KpBY0lzte0UedHynh8-Y"
id = "6941693546"
 
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="테스트 중입니다.")
 
# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
 
# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "안녕": # 사용자가 보낸 메세지가 "안녕"이면?
        bot.send_message(chat_id=id, text="안녕하겠냐?") # 답장 보내기
    elif user_text == "뭐해": # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="프원실수업듣지그럼뭐하겠냐;") # 답장 보내기
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)