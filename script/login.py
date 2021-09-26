import sys
sys.path.append(r"C:/Users/Administrator/PycharmProjects/api_automatic")
sys.path.append(r"C:\Users\Administrator\PycharmProjects\api_automatic\venv\Lib\site-packages")

import json
import os
import unittest
from parameterized import parameterized
import requests
import HTMLTestRunner
from config.logging_config import logging_config
from hy_api.api_all import HyApi
import logging
logging_config()


def get_login_data():
    with open("../data/login_api.json", encoding="UTF-8") as f:
        list = []
        data = json.load(f)
        for i in data.values():
            list.append((i.get("username"), i.get("password"), i.get("code"), i.get("login_info")))

        return list


def get_login_addd_param():
    with open("../data/login_api_add_param.json", encoding="UTF-8") as f:
        list = []
        data = json.load(f)
        for i in data.values():
            list.append((i.get("username"), i.get("password"), i.get("code"), i.get("login_info"), i.get("word")))

        return list


def get_login_lose_param():
    with open("../data/login_api_add_param.json", encoding="UTF-8") as f:
        list = []
        data = json.load(f)
        for i in data.values():
            list.append((i.get("username"), i.get("code"), i.get("login_info")))

        return list


class LoginApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        cls.hy_api = HyApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.session.close()

    def tearDown(self) -> None:
        pass

    @parameterized.expand(get_login_data())
    def test_login(self, username, password, code, login_info):
        logging.info("开始执行登录测试")
        response = self.hy_api.get_login_url(self.session, username, password, code)
        # self.assertEqual(200, response.status_code)
        self.assertIn(login_info, response.json().get("msg"))

    @parameterized.expand(get_login_addd_param())
    def test_login_add_param(self, username, password, code, login_info, word):
        logging.info("开始执行登录多参测试")
        response = self.hy_api.get_login_add_para(self.session, username, password, code, word)
        # self.assertEqual(200, response.status_code)
        self.assertIn(login_info, response.json().get("msg"))

    @parameterized.expand(get_login_lose_param())
    def test_login_lose_param(self, username, code, login_info):
        logging.info("开始执行登录少参测试")
        response = self.hy_api.get_login_lose_para(self.session, username, code)
        # self.assertEqual(200, response.status_code)
        self.assertIn(login_info, response.json().get("msg"))

    def test_login_param_null(self):
        logging.info("开始执行登录参数为空测试")
        response = self.hy_api.get_login_para_null(self.session)
        # self.assertEqual(200, response.status_code)
        self.assertIn("该用户不存在", response.json().get("msg"))




