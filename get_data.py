# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
import time

# ログインページのURL
url = "https://www.vorkers.com/login.php"
# POSTするURL
login_url = "https://www.vorkers.com/login.php/login_check"
# ヘッダー　https://www.ugtop.com/spill.shtmlから現在のブラウザコピペ
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

session = requests.session()

# ヘッダー付きでログイン画面のソース取得
response = session.get(url, headers=headers)

# beautifulSoupでログイン画面情報取得
bs = BeautifulSoup(response.text, 'html.parser')

#ユーザ情報
USERNAME = "fordevelop6960@gmail.com"
PASSWORD = "vFKfwrr2M@ipEL"
TOKEN = bs.find(attrs={'name':'_csrf_token'}).get('value')
# クッキー取得
cookie = response.cookies

# ログイン情報
info = {
    "_username": USERNAME,
    "_password": PASSWORD,
    #"_csrf_token": TOKEN,
    #"_target_path":"https://www.vorkers.com/my_top",
    "_remember_me":1,
    "log_in":"ログイン"
}



def main():
    # アクション付きURLを叩き、htmlを表示
    res = session.post(url, data=info, cookies=cookie, headers=headers)
    res = session.post("https://www.vorkers.com/my_top", data=info, cookies=cookie, headers=headers)
    print(res.text)

def login():
    pass


if __name__ == '__main__':
    main()