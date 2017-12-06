import urllib.request
from bs4 import BeautifulSoup

def crawel():
    url = "https://www.naver.com"
    html = urllib.request.Request(url)
    data = urllib.request.urlopen(html).read()
    parsing = BeautifulSoup(data,'html.parser')
    count = parsing.findAll('a',attrs={'class':'tnb_link tnb_cate'}) # 속성 지정
    print(count) # array 형식의 정보 출력
    return str(len(count))


def router(app):
    app.add_url_rule('/','endpoint',crawel)