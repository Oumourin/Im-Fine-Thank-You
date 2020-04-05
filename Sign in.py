import requests
import config


r = requests.get(config.url, cookies=config.cookie)
print(r.text)
