# coding = utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import os

'''加载所有测试用例'''
def load_all_case():
    case_path = os.path.join(os.getcwd(),'../case')
    discover = unittest.defaultTestLoader.discover(case_path, '*testcase.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    with open('../report/report.html', 'wb') as file:
        runner = HTMLTestRunner(stream=file,
                                verbosity=2,
                                title='shop商场自动化测试报告',
                                description='自动化测试报告',
                                tester='jijianfeng')
        runner.run(load_all_case())
