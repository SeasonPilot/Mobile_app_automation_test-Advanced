# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/6/29 22:16
# 文件名：pytest_20190511_homework3.py
# 开发工具：PyCharm
from appium import webdriver
import pytest

class TestXueqiulogin:

    @classmethod
    def setup_class(cls):
        caps = {}
        caps["deviceName"] = "sanxing"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["platformName"] = "Android"
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        cls.driver.find_element_by_id("com.xueqiu.android:id/image_cancel").click()
        cls.driver.find_element_by_xpath("//*[contains(@resource-id,'appbar')]//*[@text='基金']")

    def setup_method(self):
        caps = {}
        caps["deviceName"] = "sanxing"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["platformName"] = "Android"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'appbar')]//*[@text='基金']")
        # 点击我的
        self.driver.find_element_by_id('com.xueqiu.android:id/user_profile_icon').click()
        # 点击登录
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_login').click()        # 忘记写 .click()  了

    def teardown_method(self):
        self.driver.quit()

    def test_wechat(self):
        self.driver.find_element_by_xpath('//*[@text="微信登录"]').click()           # "微信登录“  第二个”写成了中文的所以报错

    def test_phone(self):
        self.driver.find_element_by_xpath('//*[@text="手机及其他登录"]').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/register_phone_number').send_keys("15869472513")
        self.driver.find_element_by_id('com.xueqiu.android:id/register_code').send_keys('fajklojfklda')
        self.driver.find_element_by_id('com.xueqiu.android:id/button_next').click()

    def test_mail(self):
        self.driver.find_element_by_xpath('//*[@text="手机及其他登录"]').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_login_with_account').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/login_account').send_keys('fajsljfas')
        self.driver.find_element_by_id('com.xueqiu.android:id/login_password').send_keys('25252jk')
