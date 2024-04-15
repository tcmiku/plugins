import json
import feedparser
from datetime import timezone,datetime

class mikanani_get:
    """
    用于获取mikanani中的rss并存储到file中的mikanani.json
    首次实例化时应调用其中git_rss的方法来获取rss数据
    为了保障软件效率也为了减轻服务器负担所以指定file来进行本地存储
    url : mikanani的rss订阅链接
    file : 文件存储位置
    """
    def __init__(self,url,file):
        self.url = url
        self.file = f'{file}mikanani.json'

    #发送网络请求rss
    def git_rss(self):
        self.rss = feedparser.parse(self.url)
        self.__server_rss()

    # 获取rss更新日期
    def git_date(self):
        self.read_rss()
        time_date = self.dates['headers']['date']
        time_format = "%a, %d %b %Y %H:%M:%S %Z"
        gmt_datetime = datetime.strptime(time_date, time_format)
        return gmt_datetime

    #使用该方法可以获取到mikanani提供的rss中更新的番剧名称以及下载链接返回一个带编号的字典names
    def git_acg_name(self):
        self.read_rss()
        names = {"name":{},"down_url":{}}
        i = 1
        acgs = self.dates['entries']
        for acg in acgs:
            names["name"][i] = acg['id']
            names["down_url"][i] = acg['links'][2]['href']
            i+=1
        return names

    #存储rss到本地json
    def __server_rss(self):
        with open(self.file,mode='w',encoding='utf-8') as date:
            date.write(json.dumps(self.rss))

    #读取json
    def read_rss(self):
        with open(self.file,mode='r',encoding='utf-8') as date:
            dates = json.load(date)
        self.dates = dates

if __name__ == '__main__':
    url = 'https://mikanani.me/RSS/MyBangumi?token=QfPawIhoeTWwgYjPRe66xg%3d%3d'
    file = './'
    json_rss = mikanani_get(url,file)
    # 首次使用应获取一遍rss数据
    # json_rss.git_rss()
    print(json_rss.git_date())
    print(json_rss.git_acg_name())