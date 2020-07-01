# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/1 21:21
# 文件名：Stock account opening.py
# 开发工具：PyCharm

from appium import webdriver
import pytest
import time

caps = {}

caps["deviceName"] = "mumu"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["platformName"] = "Android"
caps["autoGrantPermissions"] = "true"
caps["noReset"] = "true"
# 不加 automationName 会报错
caps["automationName"] = "UiAutomator1"


driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(20)

driver.find_element_by_xpath('//*[@text="交易"]').click()
time.sleep(3)
driver.find_element_by_accessibility_id('A股开户').click()
# 点击立即开户
driver.find_element_by_xpath('//*[@content-desc="雪球"]/android.view.View').click()
# 输入手机号
driver.find_element_by_id('mobile').send_keys('15657189865')
# 输入验证码
driver.find_element_by_id('validCode').send_keys('fa4564654')
# 立即开户
driver.find_element_by_accessibility_id('立即开户').click()
