import requests
import random
from bs4 import BeautifulSoup
import json
import PushMessage


# 登录页面URL
get_url = "http://39.98.190.134:81/Report/Reported"

# 登录请求URL
sign_up_url = "http://39.98.190.134:81/Account/Login"

# 申请短信验证码URL
mobile_phone_code_url = "http://39.98.190.134:81/Account/GetLoginMobileCode"

# 提交日常数据URL
post_daily_data_url = "http://39.98.190.134:81/Report"

# 打卡结果获取URL
get_checkin_result_url = "http://39.98.190.134:81/Report/Success"

# 伪造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# r = requests.get(get_url, headers=headers, cookies=my_cookies)

# 获取一个随机体温值
get_random = random.randint(355, 365)
get_my_temperature = get_random / 10.0

# Json解析
with open("config.json", 'r', encoding='utf-8') as f:
    config_data = json.load(f)
my_cookies = config_data['cookies']
my_daily_data = config_data['data']
my_daily_data['Temperature'] = str(get_my_temperature)

# 获取连接
request = requests.request('GET', get_url, cookies=my_cookies, headers=headers)

# 提交数据
post = requests.request('POST', post_daily_data_url, data=my_daily_data, cookies=my_cookies)

# 获取结果
result_request = requests.request('GET', get_checkin_result_url, cookies=my_cookies, headers=headers)
soup = BeautifulSoup(result_request.content, 'lxml')
result_string = soup.find('h2').text
if result_string == '打卡成功':
    PushMessage.push_message("今日签到成功！")
else:
    PushMessage.push_message("今日签到失败！")
