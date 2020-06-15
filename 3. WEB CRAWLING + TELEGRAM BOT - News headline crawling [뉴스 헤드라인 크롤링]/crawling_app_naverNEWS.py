import requests
from bs4 import BeautifulSoup
import telegram
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
  # 크롤링, 텔레그램봇 연동, 스케쥴링 등에 필요한 모듈을 import한다.
  
def news_notice():
  # 스케쥴링에 따라 전체 기능이 실행될 수 있도록, 크롤링 및 메세지 발송 과정을 news_notice라는 메소드로 만들었다.
    bot = telegram.Bot(token='')
    res = requests.get('https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y')
  # bot 개체에 사용할 텔레그램 봇의 토큰을 입력한다. 
  # res라는 개체에 네이버 뉴스 페이지에서 얻은 개체를 저장한다.

    soup = BeautifulSoup(res.content, 'html.parser')
  # soup 개체에 res의 컨텐츠를 저장하고, parser 단위로 구분한다.

    title = soup.select("#main_content > div.list_body.newsflash_body > ul > li > a > strong")
  # soup 개체에 저장된 내용들 중 위와 같은 셀렉터의 내용을 select하여 title 개체에 저장한다.

    now=datetime.now()
    time=('MONTH',now.month,'DAY',now.day)
  #오늘 날짜를 전송하기 위해 시간 정보를 저장한다.
    
    bot.sendMessage(chat_id=, text=time)
  # 메시지 발송 시점의 날짜 전송
  
    for i in range(len(title)):
        msg=title[i].get_text()
          # title은 일종의 리스트형 개체이므로, for문을 사용하여 한줄씩 출력할 수 있었다.
          # 또한 .get_text() 메소드를 사용해서 <strong> 태그를 제외한 결과를 깔끔하게 출력할 수 있다.
        bot.sendMessage(chat_id=, text=msg)

sched = BlockingScheduler()
sched.add_job(news_notice, 'interval', hours=12)
sched.start()

  # 고비1 : 불러온 내용을 어떻게 내보낼 것일까? (해결 - for문에서 결과를 출력하는 것이 아닌, msg에 저장하고 text를 msg로 하는 것으로 변경)
  # 고비2 : 첫번째 헤드라인만 전송됨. (해결 -  메세지 전송 코드를 for문 내부에 넣어 각 헤드라인을 모두 전송하도록 하였음)
  # 고비3 : 헤드라인이 7개면 한 번에 전송되지 않고, 7개의 메시지로 전송되어 알림이 많이 울림


  
  
