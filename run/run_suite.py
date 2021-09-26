import sys
sys.path.append(r"C:/Users/Administrator/PycharmProjects/api_automatic")

import os
import unittest
import HTMLTestRunner
from script.login import LoginApi

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginApi))
report_path = os.path.abspath("..")+"/report/"
# report_file = open(report_path+"hy_api_report_"+time.strftime("%Y-%m-%d", time.localtime())+".html", "wb")
report_file = open(report_path+"hy_api_report"+".html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="华翼接口测试", description="华翼登录接口测试", verbosity=3)

runner.run(suite)

#第三次提交 2021/9/24
