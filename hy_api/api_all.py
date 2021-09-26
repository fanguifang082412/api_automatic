import sys
sys.path.append(r"C:/Users/Administrator/PycharmProjects/api_automatic")
sys.path.append(r"C:\Users\Administrator\PycharmProjects\api_automatic\venv\Lib\site-packages")
import requests


class HyApi:

    def __init__(self):
        self.login_url = "http://test.gzhyyun.com/index/index/login.html"
        self.recharge_upload_url = "http://test.gzhyyun.com/subsidiary/index/imgupload.html"
        self.card_list_url = "http://test.gzhyyun.com/company/Coupon/card_volume"

    def get_login_url(self, session, username, password, vercode):
        data = {
            "username": username, "password": password, "vercode": vercode
        }
        return session.post(self.login_url, data=data)

    def get_login_add_para(self, session, username, password, vercode, word):
        data = {
            "username": username, "password": password, "vercode": vercode, "word": word
        }
        return session.post(self.login_url, data=data)

    def get_login_lose_para(self, session, username, vercode):
        data = {
            "username": username, "vercode": vercode
        }
        return session.post(self.login_url, data=data)

    def get_login_para_null(self, session):
        return session.post(self.login_url)

    def get_recharge_upload(self, session):
        files = {"file": ("油7.png", open(r"C:\Users\Administrator\Desktop\image\油7.png", "rb"), "image/png")}

        return session.post(self.recharge_upload_url, files=files)

    def get_card_list(self, session):
        return session.post(self.card_list_url)







