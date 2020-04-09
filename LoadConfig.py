import json
import PushMessage


def load_config_json():
    try:
        with open("./config.json", "r", encoding="utf-8") as f:
            config_data = json.load(f)
    except IOError:
        PushMessage.push_message("加载配置文件错误！")
    else:
        return config_data
