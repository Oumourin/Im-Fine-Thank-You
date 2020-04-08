import requests
import json


push_base_url = "https://sc.ftqq.com/"


def push_message(text="Error"):
    with open("config.json", 'r', encoding='utf-8') as f:
        get_config = json.load(f)
    get_server = get_config['Server']
    get_sc_key = get_server['SCKEY']
    get_push_url = push_base_url + get_sc_key + ".send?" + "text=" + str(text)
    requests.get(get_push_url)

