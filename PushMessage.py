import requests
import json


push_base_url = "https://sc.ftqq.com/"
sc_key = "SCU63598T8dbcd2527aefac9c980e6625bd2e92235d99de5fb42e6"


def push_message(text="Error"):
    get_push_url = push_base_url + sc_key + ".send?" + "text=" + str(text)
    requests.get(get_push_url)

