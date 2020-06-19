from selenium import  webdriver
import unittest
import time
from ip_xiugai import get_ip
from selenium.webdriver.support.select import Select
#************************************************************************
class Denglu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get(ip)
        time.sleep(5)
    def test_case1(self):#正常登录
        self.driver.find_element_by_id('tbx_UserName').send_keys('adm')
        self.driver.find_element_by_id('tbx_Password').send_keys('adm')
        self.driver.find_element_by_id('ibtLogin').click()
        time.sleep(5)
        assert1=self.driver.title
        self.assertEqual(assert1,'[未注册试用版]网络办公自动化软件 [WebOA 19.12.7278.20211 5用户] [2019-12-31到期]',msg='未登录成功')
    def test_case2(self):#用户名错误登录
        self.driver.find_element_by_id('tbx_UserName').send_keys('adm1')
        self.driver.find_element_by_id('tbx_Password').send_keys('adm')
        self.driver.find_element_by_id('ibtLogin').click()
        time.sleep(5)
        self.a=self.driver.switch_to.alert
        assert2=self.a.text
        self.assertEqual(assert2, '失败：用户账号或密码错误！', msg='用户名错误提示异常')
    def test_case3(self):#密码错误登录
        self.driver.find_element_by_id('tbx_UserName').send_keys('adm')
        self.driver.find_element_by_id('tbx_Password').send_keys('adm1')
        self.driver.find_element_by_id('ibtLogin').click()
        time.sleep(5)
        self.a = self.driver.switch_to.alert
        assert3 = self.a.text
        self.assertEqual(assert3, '失败：用户账号或密码错误！', msg='用户名错误提示异常')
        self.a.accept()
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    ip = get_ip()
    time.sleep(5)
    suite = unittest.TestSuite()
    suite.addTest(Denglu('test_case1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)