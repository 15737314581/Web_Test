# coding = utf-8
# coding = utf-8
import unittest
from vip_02web.case.testcaseLogin import LoginTestCase,SearchTestCase
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    class_list = [LoginTestCase,SearchTestCase]
    name_list = []
    test_name_list = []
    suite = unittest.TestSuite()
    for i in class_list:
        name_list.extend(dir(i))
        # print(name_list)
        for j in name_list:
            if j.startswith('test'):
                test_name_list.append(j)
        new_test_name_list = sorted(test_name_list, key=lambda x: len(x), reverse=True)
        for m in new_test_name_list:
            suite.addTest(i(m))
        name_list = []
        test_name_list = []

    with open('./report/report.html','wb') as file:
        runner = HTMLTestRunner(stream=file,
                                    verbosity=2,
                                    title='shop商场自动化测试报告',
                                    description='登录功能自动化测试报告',
                                    tester='jijianfeng')

        # 执行器执行测试套件
        runner.run(suite)




