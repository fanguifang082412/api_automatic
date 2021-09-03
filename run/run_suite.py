import os
import time
import unittest
import HTMLTestRunner
from script.login import LoginApi

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginApi))
report_path = os.path.abspath("..")+"/report/"
report_file = open(report_path+"hy_api_report_"+time.strftime("%Y-%m-%d", time.localtime())+".html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="华翼接口测试", description="华翼登录接口测试", verbosity=3)

runner.run(suite)
