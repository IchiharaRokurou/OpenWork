# -*- coding: utf-8 -*-

import sys
import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
import 
pip install selenium
pip install chromedriver-binary==104.0.5112.79
"""

# ログインページのURL
url = "https://www.vorkers.com/login.php"
top_url = "https://www.vorkers.com/my_top"

# Webドライバ
driver = webdriver.Chrome()
driver.get(url) 

# ユーザ情報
USERNAME = "fordevelop6960@gmail.com"
PASSWORD = "vFKfwrr2M@ipEL"


def main():
    # URLを叩き、htmlを表示    
    driver.get(url) 
    time.sleep(1)
    login()
    search(["株式会社学研"])
    
    

# ログイン
def login():
    # メールとパスワードを入力
    mail = driver.find_element("name","_username") 
    password = driver.find_element("name","_password") 
    
    # クリア
    mail.clear()
    password.clear()
    # フォーム入力
    mail.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    # エンター
    mail.submit()



def search(name:str=""):
    """
    オープンワークで企業名検索する関数
    Args:
        name (str, optional): 検索したい名前. Defaults to "".
    """
    # トップページに戻ってから
    back_to_mypage()
    search_box = driver.find_element("name","src_str")
    # 検索    
    search_box.send_keys(name)
    search_box.submit()


# マイページ戻る
def back_to_mypage():
    driver.get(top_url) 
    time.sleep(1)


if __name__ == '__main__':
    main()