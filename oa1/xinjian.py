#***********************************************************************
'''
简介：新建事务模块
2020-06-03
'''
from selenium import  webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
from ip_xiugai import get_ip
#************************************************************************
class Insert_Business(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get(ip)
        time.sleep(5)
        self.driver.find_element_by_id('tbx_UserName').send_keys('adm')
        self.driver.find_element_by_id('tbx_Password').send_keys('adm')
        self.driver.find_element_by_id('ibtLogin').click()
        time.sleep(5)
#======================================================================================
    # 新建事务
    # 正常新建费用报销单
    def test_case1(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        #进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()
    # 正常新建费用报销单  加附件
    def test_case2(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")
        time.sleep(6)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert2 = self.a.text
        self.assertEqual(assert2, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()

    # 必填项未填写保存
    ###################################主题未填写
    def test_case31(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('')#测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
    ###################################报销日期未填写
    def test_case32(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')  # 测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
    ###################################单据附件张数未填写
    def test_case33(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')  # 测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
    ###################################第一行费用项目未填写
    def test_case34(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')  # 测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('')#住宿
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
    ###################################第一行费用金额未填写
    def test_case35(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')  # 测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')#住宿
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('20.3')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
    ###################################总金额未填写
    def test_case36(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(5)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0001')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('测试报告')  # 测试报告
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[4] / input').send_keys('2020-06-30')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[1] / tbody / tr[2] / td[6] / input').send_keys('2')
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('住宿')  # 住宿
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('20.3')
        self.driver.find_element_by_xpath(
            '/ html / body / form / ol / li / table[2] / tbody / tr[6] / td[3] / input').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('住宿报销单')
        self.driver.find_element_by_id('save').click()
        time.sleep(1)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
#======================================================================================
    # 新建立项申请单
    # 正常新建立项申请单
    def test_case4(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0005')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('项目1主题')#主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[2]/input').send_keys('项目1立项')#项目名称
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/textarea').send_keys('项目1内容')  # 项目内容
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/input').send_keys('cb')  # 项目责任人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('20000')  # 预计开支金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('2020-06-05')  # 预计完成日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1备注')#备注
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()
    # 新建立项申请单必填项未填写  主题未填写
    def test_case41(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0005')
        time.sleep(2)
        self.driver.find_element_by_id('subject').send_keys('')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[2]/input').send_keys('项目1立项')  # 项目名称
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/textarea').send_keys('项目1内容')  # 项目内容
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/input').send_keys('cb')  # 项目责任人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('20000')  # 预计开支金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('2020-06-05')  # 预计完成日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1备注')  # 备注
        self.driver.find_element_by_id('save').click()
        time.sleep(2)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
#=========================================================================================
    # 新建请假申请单
    # 正常新建请假申请单
    def test_case5(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0002')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('请假单')#主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('测试工程师')#职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('2')  # 请假天数
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/textarea').send_keys('年假')  # 请假原因
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('备注：请年假2天')  # 备注
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('2020-06-05')  # 起始日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[6]/input').send_keys('2020-06-08')  # 结束日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1备注')#备注
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()
    # 新建请假申请单必填项未填写 主题未填写
    def test_case51(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0002')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('测试工程师')  # 职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('2')  # 请假天数
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/textarea').send_keys('年假')  # 请假原因
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('备注：请年假2天')  # 备注
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('2020-06-05')  # 起始日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[6]/input').send_keys('2020-06-08')  # 结束日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1备注')  # 备注
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert4 = self.a.text
        self.assertEqual(assert4, '!', msg='主题未填写提示不成功')
# =========================================================================================
    # 新建预算审批单
    # 正常新建预算审批单
    def test_case6(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0004')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('预算审批单')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('工程预算')  # 费用科目
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[8]/input').send_keys('2020-06-05')  # 申请日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('项目1')  # 事由或项目
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/input').send_keys('10000')  # 申请金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('20000')  # 本月预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('30000')  # 累计预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[2]/input').send_keys('10000')  # 本月剩余预算
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[4]/input').send_keys('10000')  # 累计使用金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[5]/textarea').send_keys('无')  # 预算外原因说明
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/select')).select_by_value('是')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[7]/td[2]/input').send_keys('项目1')  # 项目第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[7]/td[3]/input').send_keys('5000')  # 项目第一行金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[11]/td[3]/input').send_keys('5000')  # 总金额
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1 预算审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()
    # 新建预算审批单必填项未填写  主题未填写
    def test_case61(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0004')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('工程预算')  # 费用科目
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[8]/input').send_keys('2020-06-05')  # 申请日期
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('项目1')  # 事由或项目
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[1]').send_keys('10000')  # 申请金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('20000')  # 本月预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('30000')  # 累计预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[2]/input').send_keys('10000')  # 本月剩余预算
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[4]/input').send_keys('10000')  # 累计使用金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[5]/textarea').send_keys('无')  # 预算外原因说明
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/select')).select_by_value('是')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[7]/td[2]/input').send_keys('项目1')  # 项目第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[7]/td[3]/input').send_keys('5000')  # 项目第一行金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[11]/td[3]/input').send_keys('5000')  # 总金额
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目1 预算审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert61 = self.a.text
        self.assertEqual(assert61, '!', msg='主题未填写提示不成功')
# =========================================================================================
    # 新建招待审批单
    # 正常新建招待审批单
    def test_case7(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0003')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('招待审批单')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('下新公司')  # 来访单位
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('2020-06-05')  # 接待时间
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('接待客户')  # 事由或项目
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/select')).select_by_value('商务') #接待类型
        time.sleep(3)
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/select')).select_by_value('A类') #接待级别
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('如家')  # 接待酒店
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[2]/input').send_keys('20000')  # 本月预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[4]/input').send_keys('30000')  # 累计预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[6]/td[2]/input').send_keys('10000')  # 本月剩余预算
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[6]/td[4]/input').send_keys('10000')  # 累计使用金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[8]/td[2]/input').send_keys('陈博')  # 来访客人 第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[8]/td[3]/input').send_keys('无')  # 来访客人 第一行 职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[13]/td[2]/input').send_keys('cb')  # 陪同客人 第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[13]/td[3]/input').send_keys('无')  # 陪同客人 第一行 职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[15]/td[3]/input').send_keys('3000')  # 消费金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[21]/td[2]/input').send_keys('20000')  # 消费金额合计
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目招待审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()

    # 新建招待审批单必填项未填写 主题未填写
    def test_case71(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0003')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[6]/input').send_keys('下新公司')  # 来访单位
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('2020-06-05')  # 接待时间
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('接待客户')  # 事由或项目
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/select')).select_by_value('商务')  # 接待类型
        time.sleep(3)
        Select(self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/select')).select_by_value('A类')  # 接待级别
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[4]/input').send_keys('如家')  # 接待酒店
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[2]/input').send_keys('20000')  # 本月预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[5]/td[4]/input').send_keys('30000')  # 累计预算金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[6]/td[2]/input').send_keys('10000')  # 本月剩余预算
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[6]/td[4]/input').send_keys('10000')  # 累计使用金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[8]/td[2]/input').send_keys('陈博')  # 来访客人 第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[8]/td[3]/input').send_keys('无')  # 来访客人 第一行 职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[13]/td[2]/input').send_keys('cb')  # 陪同客人 第一行
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[13]/td[3]/input').send_keys('无')  # 陪同客人 第一行 职务
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[15]/td[3]/input').send_keys('3000')  # 消费金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[21]/td[2]/input').send_keys('20000')  # 消费金额合计
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目招待审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert61 = self.a.text
        self.assertEqual(assert61, '!', msg='主题未填写提示不成功')

# =========================================================================================
    # 新建支付审批单
    # 正常新建支付审批单
    def test_case8(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0006')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('支付审批单')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[2]/input').send_keys('项目2')  # 项目名称
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[4]/input').send_keys('0002')  # 立项编号
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('ZZ公司')  # 请款单位或个人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('项目2')  # 经办人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/input').send_keys('1000')  # 本期申请拔款金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/input').send_keys('2000')  # 合计拔款金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[6]/input').send_keys('3000')  # 立项总金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/textarea').send_keys('项目2已完成90%')  # 项目进度情况及费用金额
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目招待审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.switch_to.alert
        assert4 = self.a.text
        self.assertEqual(assert4, '成功：当前事务创建成功！', msg='创建事务未成功')
        self.a.accept()
    # 新建支付审批单必填项未填写
    def test_case81(self):
        self.driver.find_element_by_xpath(' / html / body / div[2] / div / div[2] / div[1] / ul[6] / li[1]').click()
        time.sleep(3)
        # 进入新建事务页面
        self.driver.switch_to.frame('tab_OaAffairPost_ifm')
        time.sleep(3)
        Select(self.driver.find_element_by_xpath('//*[@id="kind"]')).select_by_value('0006')
        time.sleep(3)
        self.driver.find_element_by_id('subject').send_keys('支付审批单')  # 主题
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[2]/input').send_keys('项目2')  # 项目名称
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[1]/td[4]/input').send_keys('0002')  # 立项编号
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('ZZ公司')  # 请款单位或个人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('项目2')  # 经办人
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/input').send_keys('1000')  # 本期申请拔款金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[4]/input').send_keys('2000')  # 合计拔款金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[3]/td[6]/input').send_keys('3000')  # 立项总金额
        self.driver.find_element_by_xpath(
            '/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/textarea').send_keys('项目2已完成90%')  # 项目进度情况及费用金额
        self.driver.find_element_by_xpath(
            '//*[@id="url"]').send_keys('项目招待审批单')  # 备注
        self.driver.find_element_by_xpath(
            '//*[@id="upLocFile"]').send_keys(r"C:\Users\Administrator\Desktop\123.xlsx")  # 附件
        time.sleep(10)
        self.driver.find_element_by_id('save').click()
        time.sleep(3)
        self.a = self.driver.find_element_by_xpath('/ html / body / div / div')
        assert61 = self.a.text
        self.assertEqual(assert61, '!', msg='主题未填写提示不成功')
    # def tearDown(self):
    #     time.sleep(10)
    #     self.driver.quit()
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
if __name__ == '__main__':
    ip = get_ip()
    suite=unittest.TestSuite()
    suite.addTest(Insert_Business('test_case8'))
    runner=unittest.TextTestRunner()
    runner.run(suite)