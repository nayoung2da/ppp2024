import random
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
 
token = "7052514700:AAFNQ-MFxDyWnv3KpBY0lzte0UedHynh8-Y"
id = "6941693546"
 
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="타로봇입니다. 오늘의 타로를 알고 싶다면 '타로'라고 입력해주세요.")

tarot_fortunes = [
    ("The Fool", "새로운 시작이 다가오고 있습니다. 모험을 두려워하지 마세요."),
    ("The Magician", "당신의 의지와 창조력이 빛을 발할 때입니다."),
    ("The High Priestess", "직관을 신뢰하고 내면의 목소리에 귀 기울이세요."),
    ("The Empress", "풍요와 창조성이 넘치는 시기입니다. 주변 사람들과의 관계가 좋아질 것입니다."),
    ("The Emperor", "안정과 권위를 중요시하세요. 결단력이 필요한 순간입니다."),
    ("The Hierophant", "전통과 교육이 중요한 역할을 할 것입니다."),
    ("The Lovers", "사랑과 조화가 가득한 시간입니다. 중요한 관계에 집중하세요."),
    ("The Chariot", "승리와 결단력이 필요한 시기입니다. 앞으로 나아가세요."),
    ("Strength", "용기와 인내가 필요한 때입니다. 내면의 힘을 믿으세요."),
    ("The Hermit", "혼자만의 시간을 가지며 내면을 탐구해보세요."),
    ("Wheel of Fortune", "운명이 당신 편입니다. 긍정적인 변화를 기대하세요."),
    ("Justice", "공정과 균형이 중요한 시기입니다. 진실을 추구하세요."),
    ("The Hanged Man", "관점을 전환하고 새로운 시각으로 문제를 보세요."),
    ("Death", "변화의 시기입니다. 새로운 시작을 준비하세요."),
    ("Temperance", "절제와 조화가 필요합니다. 인내심을 가지세요."),
    ("The Devil", "유혹과 속박을 주의하세요. 물질적 욕망을 경계하세요."),
    ("The Tower", "갑작스러운 변화와 혼란이 있을 수 있습니다. 유연하게 대처하세요."),
    ("The Star", "희망과 영감이 가득한 시기입니다. 재생의 기회를 놓치지 마세요."),
    ("The Moon", "환상과 불확실성을 주의하세요. 무의식의 메시지를 받아들이세요."),
    ("The Sun", "행복과 성공이 기다리고 있습니다. 활기차게 움직이세요."),
    ("Judgement", "심판의 시기입니다. 내면의 목소리에 귀 기울이세요."),
    ("The World", "성취와 완성이 눈앞에 있습니다. 여행을 떠나보세요.")
]

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
        bot.send_message(chat_id=id, text="안녕하세요? 오늘의 타로카드를 확인해주는 쳇봇입니다! 타로를 보고 싶다면 '타로'라고 작성해주세요!") # 답장 보내기
    elif user_text.lower() == "타로":
        tarot, fortune = random.choice(tarot_fortunes) # 랜덤으로 타로카드와 운세 선택
        bot.send_message(chat_id=id, text=f"오늘의 타로카드: {tarot}\n운세: {fortune}") # 타로카드와 운세 전송

    else:
        bot.send_message(chat_id=id, text="타로 운세를 알려면 '타로'를 입력하세요.")
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)