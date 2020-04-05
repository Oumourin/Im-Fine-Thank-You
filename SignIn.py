import requests
import config


r = requests.get(config.url, cookies=config.cookie)
print(r.text)
# r = requests.post(config.get_mobile_code_url, data=config.phone_number)
# print(r.status_code)
# print(r.text)
