# -*- coding: utf-8 -*-

import sys
import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import re 


"""
import 
pip install selenium
pip install chromedriver-binary==104.0.5112.79
"""

# ログインページのURL
url = "https://www.vorkers.com/login.php"
top_url = "https://www.vorkers.com/my_top"
base_url = "https://www.vorkers.com"

# Webドライバ
driver = webdriver.Chrome()
driver.get(url) 

# ユーザ情報
USERNAME = "fordevelop6960@gmail.com"
PASSWORD = "vFKfwrr2M@ipEL"


def main():
    # URLを叩き、htmlを表示    
    driver.get(url) 
    time.sleep(0.5)
    login()
    search(["株式会社学研"])
    get_search_results()
    
    

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


# 検索結果取得
def get_search_results():
    results = driver.find_elements(By.CLASS_NAME,"searchCompanyName")
    pattern = r'<div>(.*?)</div>'
    a_tags = []
    # 各要素から名前のaダグのみ取得
    for result in results:
        content = result.get_attribute('innerHTML').replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
        text = re.match(pattern, content)
        # aタグからurlと名前取得
        text = re.match(r'<div>.*<ahref="(.*?)">(.*?)</a>.*?', text.group())
        if text:
            a_tags.append(text.groups())
    # 各ページ移動
    for a_tag in a_tags:
        comp_url, name = a_tag
        print(name)
        driver.get(base_url + comp_url)
        get_info(base_url + comp_url)
        break
        time.sleep(0.5)


# 情報取得
def get_info(comp_url):
    # スコア辞書取得
    scores = get_scores()
    review_num = get_review_nums()
    jump2review(comp_url.replace('company', 'company_answer'))
    
    
def get_scores():
    scores = driver.find_element(By.CLASS_NAME,'scoreList-8')
    # <li> ~ </li>に分解
    contents = scores.get_attribute('innerHTML').replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '').split('</li>')
    score_dict = dict()
    # 各liのデータ取得
    pattern = r'<li.*?><dl>(.*?)</dl>'
    for content in contents:
        result = re.match(pattern, content)
        # スコアと点数を取得
        if result:
            table_name, score = re.match(r'.*?<dt.*?>(.*?)</dt><dd.*?>(.*?)</dd>.*?', result.group()).groups()
            print(table_name, score)
            score_dict[table_name] = score
    return score_dict


# 口コミ数取得
def get_review_nums():
    review = driver.find_element(By.XPATH, '//h2[contains(text(),"カテゴリ")]')
    content = review.get_attribute('innerHTML').replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    pattern = r'.*<span>(.*?)</span>.*'
    result = re.match(pattern, content)
    return result.group(1)


# 口コミへ
def jump2review(review_url):
    driver.get(review_url)
    for no in range(1, 10 + 1):
        get_each_review_data(review_url + '&q_no={}'.format(no))
        break
        time.sleep(1)
    
# 各口コミ
def get_each_review_data(review_url):
    driver.get(review_url)
    review_num = driver.find_element(By.XPATH, "//a[@href='{}']".format(review_url.replace(base_url, '')))
    content = review_num.get_attribute('innerHTML').replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    print(content)
    pattern = r'<span.*?>(.*?)<span.*?>（(.*?)件）</span></span>'
    result = re.match(pattern, content)
    review_dict = dict()
    if result:
        review_name, num = result.groups()
        review_dict[review_name] = num
    
# マイページ戻る
def back_to_mypage():
    driver.get(top_url) 
    time.sleep(0.5)


if __name__ == '__main__':
    main()