import os
import json
import random


class WhatToEat:
    def __init__(self):
        self.new_directory_path = "./date_food"
        self.directory_path = "./date_food"
        self.json_file_path = os.path.join(self.directory_path, 'food_data.json')
        self.data = {
            'food_name': []
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
            print(f"json文件已存在或创建失败")

    # 新增食物
    def add_food(self, food_name):
        self.show_all_food()
        data =self.data
        if food_name in data['food_name']:
            print(f"食物 '{food_name}' 已存在")
            return
        else:
            data['food_name'].append(food_name)
            with open(self.json_file_path, 'w', encoding='utf-8') as json_file:  # 打开json文件
                json.dump(data, json_file, ensure_ascii=False, indent=4)  # 写入json文件
            print(f"新增食物 '{food_name}' 成功")

    # 显示所有食物
    def show_all_food(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:  # 打开json文件
            self.data = json.load(json_file)  # 读取json文件
        print(f"所有食物: {self.data['food_name']}")

    #随机选择食物
    def random_select_food(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:  # 打开json文件
            self.data = json.load(json_file)  # 读取json文件
        if len(self.data['food_name']) == 0:
            print("没有食物")
            return
        else:
            random_index = random.randint(0, len(self.data['food_name']) - 1)
            print(f"随机选择食物: {self.data['food_name'][random_index]}")
            return self.data['food_name'][random_index]


if __name__ == '__main__':
    wte = WhatToEat()
    i = 1
    while i<=1000:
        wte.random_select_food()
        i += 1
