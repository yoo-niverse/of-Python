import requests
import telegram
from bs4 import BeautifulSoup
bot=telegram.Bot(token = '1101854162:AAG6DnVaCykWxo9qKZivylL13j0LA6HCYaA')
#텔레그램으로 생성한 봇을 불러왔다.
from apscheduler.schedulers.blocking import BlockingScheduler
#AP스케쥴러에서 하나의 요소만 스케쥴링 하므로 Blocking 사용


url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=05,207&theatercode=0061&date=20200428'
#예매 시간표를 받아오기 위해 CGV 홈페이지에서 개발자 도구를 활용하여, 시간표가 노출되는 부분의 iframe 링크를 가져왔다.

def work_alert(): #스케쥴에 따라 작업수행을 위해, 해당 작업을 모두 함수로 묶어줌
    html=requests.get(url)
    #print(html.text)
    soup=BeautifulSoup(html.text, 'html.parser')
#soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong')
#selector 요소를 가져오는 .select() 메소드 중 하나의 요소만 가져오는 selector_one 메소드 활용
    title_list= soup.select('div.info-movie')
    """개발자 도구를 활용하여 영화 제목이 info-movie라는 클래스에 모두 들어가있는 것을 확인하였으므로,
해당 클래스 요소를 가져와서 title_list라는 리스트에 삽입한다."""
    grade19 = soup.select_one('span.ico-grade.grade-19')
    #해당 날짜에 19금 영화가 있다면 1 반환, 없다면 0 반환
    #span.ico-grade.grade-19에 청불 마크가 있음
    if grade19 :
        grade19=grade19.find_parent('div', class_='col-times')
        title=grade19.select_one('div.info-movie>a>strong').text.strip()
     #find_parent는 부모 클래스를 찾는 메소드. col-times라는 클래스에 info-movie와 grade-19 클래스가 들어있다.
        bot.sendMessage(chat_id=914003638, text='해당 일자에는 청불영화가 있습니다'+title)
        sched.pause()
    else :
        bot.sendMessage(chat_id=914003638, text='해당 일자에는 청불영화가 없습니다')

    #실행결과가 이제는 무조건 '없습니다'로만 출력된다. CGV측에서 해당 일자 상영표를 삭제했기 때문.

    
"""for i in title_list:
    print(i.select_one('a>strong').text.strip()) """ #영화 제목은 info-movie 클래스에서 a라는 클래스 -> strong이라는 클래스 내부에 있다.
    #text 메소드 : 가져온 내용에서 태그를 제외하고 '텍스트'만 출력(strong 제외시킴)
    #strip 메소드 : 가져온 내용에서 공백을 제외하고 출력


sched = BlockingScheduler()
#블락킹 스케쥴러 생성 : sched
sched.add_job(work_alert, 'interval', seconds=60)
#work_alert라는 작업을 추가, 30초의 interval로 수행함
sched.start()

