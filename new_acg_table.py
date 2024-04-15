import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
class git_acg_table:
    """
    用于获取新番表
    为了保障软件效率也为了减轻服务器负担所以指定file来进行本地存储

    """
    def __init__(self,url,file):
        self.url = url
        self.file = file

    def git_html(self):
        head = {
            "User-Agent": UserAgent().chrome
        }
        html_date = requests.get(self.url,headers=head)
        with open('./acgtbale.html',mode='wb') as html:
            html.write(html_date.content)

    def open_html(self):
        file = f'{self.file}acgtbale.html'
        with open(file,mode='r',encoding='utf-8') as html:
            acg_date = html.read()
        self.acg_date = acg_date

    def git_acg_name(self):
        self.open_html()
        sun_list = []
        mon_list = []
        tue_list = []
        wed_list = []
        thu_list = []
        fri_list = []
        sat_list = []
        soup = BeautifulSoup(self.acg_date, 'html.parser')
        acg_date_Sun = soup.select('.BgmCalendar .Sun .nav')
        acg_date_Mon = soup.select('.BgmCalendar .Mon .nav')
        acg_date_Tue = soup.select('.BgmCalendar .Tue .nav')
        acg_date_Wed = soup.select('.BgmCalendar .Wed .nav')
        acg_date_Thu = soup.select('.BgmCalendar .Thu .nav')
        acg_date_Fri = soup.select('.BgmCalendar .Fri .nav')
        acg_date_Sat = soup.select('.BgmCalendar .Sat .nav')
        for name in acg_date_Sun:
            sun_list.append(name.get_text())
        for name in acg_date_Mon:
            mon_list.append(name.get_text())
        for name in acg_date_Tue:
            tue_list.append(name.get_text())
        for name in acg_date_Wed:
            wed_list.append(name.get_text())
        for name in acg_date_Thu:
            thu_list.append(name.get_text())
        for name in acg_date_Fri:
            fri_list.append(name.get_text())
        for name in acg_date_Sat:
            sat_list.append(name.get_text())
        acg_table = {"Sun": {'name': {}, 'img': {}}, "Mon": {'name': {}, 'img': {}}, "Tue": {'name': {}, 'img': {}},
                     "Wed": {'name': {}, 'img': {}}, "Thu": {'name': {}, 'img': {}}, "Fri": {'name': {}, 'img': {}},
                     "Sat": {'name': {}, 'img': {}}}

if __name__ == '__main__':
    url = 'https://bgm.tv/calendar'
    file = './'
    acg = git_acg_table(url,file)
    # acg.git_html()
    acg.git_acg_name()