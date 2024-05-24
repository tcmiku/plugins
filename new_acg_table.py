import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import os
import json
import time

class git_acg_table:
    """
    用于获取新番表
    为了保障软件效率也为了减轻服务器负担所以指定file来进行本地存储
    """
    def __init__(self,url,file):
        self.url = url
        self.file = file
        json_date = File()

    def git_html(self):
        head = {
            "User-Agent": UserAgent().chrome
        }
        html_date = requests.get(self.url,headers=head)
        self.html_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.html'
        with open(self.html_file,mode='wb') as html:
            html.write(html_date.content)

    def open_html(self):
        file = f'{self.file}{self.html_file}'
        with open(file,mode='r',encoding='utf-8') as html:
            acg_date = html.read()
        self.acg_date = acg_date

    def git_acg_name(self):
        self.open_html()
        week_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        sun_list = []
        mon_list = []
        tue_list = []
        wed_list = []
        thu_list = []
        fri_list = []
        sat_list = []
        soup = BeautifulSoup(self.acg_date, 'html.parser')
        for i in week_list:
            acg_date_i = soup.select(f'.BgmCalendar .{i} .nav')
            for name in acg_date_i:
                if i == 'Sun':
                    sun_list.append(name.get_text())
                elif i == 'Mon':
                    mon_list.append(name.get_text())
                elif i == 'Tue':
                    tue_list.append(name.get_text())
                elif i == 'Wed':
                    wed_list.append(name.get_text())
                elif i == 'Thu':
                    thu_list.append(name.get_text())
                elif i == 'Fri':
                    fri_list.append(name.get_text())
                elif i == 'Sat':
                    sat_list.append(name.get_text())

        self.acg_table = {"Sun": {'name': sun_list, 'img': {}}, "Mon": {'name': mon_list, 'img': {}}, "Tue": {'name': tue_list, 'img': {}},
                     "Wed": {'name': wed_list, 'img': {}}, "Thu": {'name': thu_list, 'img': {}}, "Fri": {'name': fri_list, 'img': {}},
                     "Sat": {'name': sat_list, 'img': {}}}

        return self.acg_table

    def git_acg_img(self):
        self.open_html()
        soup = BeautifulSoup(self.acg_date, 'html.parser')
        week_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i in week_list:
            acg_date_i = soup.select(f'.BgmCalendar .{i} .item')
            for name in acg_date_i:
                img_url = name.select_one('.cover img')['src']
                img_name = re.search(r'\/(\d+).jpg', img_url).group(1)
                self.acg_table[i]['img'][img_name] = img_url

class File:
    def __init__(self):
        self.new_directory_path = "./date_new_acg"
        self.directory_path = "./date_new_acg"
        self.json_file_path = os.path.join(self.directory_path, 'acg_data.json')
        self.data = {
            "Sun": [],
            "Mon": [],
            "Tue": [],
            "Wed": [],
            "Thu": [],
            "Fri": [],
            "Sat": []
        }
        self.check_directory_exists(self.directory_path)

    def check_directory_exists(self, directory_path):
        if os.path.isdir(directory_path):
            print(f"目录 '{directory_path}' 存在.")
            self.create_json_file(self.json_file_path, self.data)
        else:
            print(f"目录 '{directory_path}' 不存在")
            print('初始化:')
            self.create_directory(directory_path)

    def create_directory(self, directory_path):
        try:
            os.makedirs(directory_path)
            print(f"创建目录 '{directory_path}' 成功")
            self.create_json_file(self.json_file_path, self.data)
        except FileExistsError:
            print(f"创建目录 '{directory_path}' 异常，请检查代码")

    def create_json_file(self, file_path, data):
        try:
            if os.path.isfile(self.json_file_path):
                print(f"json文件 '{file_path}' 已存在")
            else:
                print(f"创建json文件 '{file_path}'")
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)
                print(f"创建json文件 '{file_path}' 成功")
        except Exception as e:
            print(f"json文件已存在或创建失败{e}")

class server_acg_table:
    """
    结果存储
    """
    def __init__(self,date,name):
        self.json_file_path = f"./date_new_acg/acg_data.json"
        self.add_acg_name(date,name)
    # 新增食物
    def add_acg_name(self,date,acg_name):
        self.show_all_acg()
        data =self.data
        data[date] = acg_name
        with open(self.json_file_path, 'w', encoding='utf-8') as json_file:  # 打开json文件
            json.dump(data, json_file, ensure_ascii=False, indent=4)  # 写入json文件

    # 显示所有食物
    def show_all_acg(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:  # 打开json文件
            self.data = json.load(json_file)  # 读取json文件


if __name__ == '__main__':
    url = 'https://bgm.tv/calendar'
    file = './'
    acg = git_acg_table(url,file)
    if not os.path.isfile(f'{file}acgtbale.html'):
        acg.git_html()
    week_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i in week_list:
        server_acg_table(i,acg.git_acg_name()[i]['name'])

    #显示当前时间
    print(time.strftime("%Y-%m-%d", time.localtime()))