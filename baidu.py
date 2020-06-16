from selenium import  webdriver
import unittest
import time
class baidu_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://www.baidu.com')
        time.sleep(5)
    def test_case1(self):
        self.driver.find_element_by_id('kw').send_keys('迪丽热巴')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        a=self.driver.title
        self.assertEqual(a,'迪丽热巴_百度搜索',msg="页面没打开")
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()

    # suite=unittest.TestSuite()
    # suite.addTest(baidu_test("test_case1"))
    # rrr=unittest.TextTestRunner()
    # rrr.run(suite)