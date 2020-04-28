import telegram

bot=telegram.Bot(token = '1101854162:AAG6DnVaCykWxo9qKZivylL13j0LA6HCYaA')

for i in bot.getUpdates():
    print(i.message)
    # 봇에게 온 메세지, 보낸사람 등을 출력할 수 있게 해주는 코드"""

#bot.sendMessage(chat_id=914003638, text='안녕 주인놈아')
#내 아이디를 입력하여 봇이 나에게 텍스트 아래 메세지를 보낼 수 있게 해줌



