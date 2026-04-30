import os
import io
import shutil
import time
import requests

RULE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/"
REJECT_RULES = {
    "Advertising": RULE_URL + "Advertising/Advertising.list",
    "Advertising_Domain": RULE_URL + "Advertising/Advertising_Domain.list",
    "Privacy": RULE_URL + "Privacy/Privacy.list",
    "Privacy_Domain": RULE_URL + "Privacy/Privacy_Domain.list"
}
PROXY_RULES = {
    "GlobalMedia": RULE_URL + "GlobalMedia/GlobalMedia.list",
    "GlobalMedia_Domain": RULE_URL + "GlobalMedia/GlobalMedia_Domain.list",
    "Global": RULE_URL + "Global/Global.list",
    "Global_Domain": RULE_URL + "Global/Global_Domain.list",
    "Proxy": RULE_URL + "Proxy/Proxy.list",
    "Proxy_Domain": RULE_URL + "Proxy/Proxy_Domain.list"
}
DIRECT_RULES = {
    "ChinaMax": RULE_URL + "ChinaMax/ChinaMax.list",
    "ChinaMax_Domain": RULE_URL + "ChinaMax/ChinaMax_Domain.list"
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def load_file(rules_dict, file_dir):
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    for key in rules_dict:
        response = requests.get(rules_dict[key], headers=HEADER)
        if response.status_code == 200:
            with open(f"./{file_dir}/{key}.list", "wb") as f:
                with response, io.BytesIO(response.content) as stream:
                    shutil.copyfileobj(stream, f)
            time.sleep(1)

def remove():
    for d in ["Direct_Rule", "Proxy_Rule", "Reject_Rule"]:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"移除 {d} 文件夹")

if __name__ == '__main__':
    os.chdir("./rule")
    remove()
    load_file(REJECT_RULES, "Reject_Rule")
    load_file(PROXY_RULES, "Proxy_Rule")
    load_file(DIRECT_RULES, "Direct_Rule")
