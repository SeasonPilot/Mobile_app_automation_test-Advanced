# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/1 21:20
# 文件名：20190517_Fund account opening.py
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

driver.find_element_by_accessibility_id('基金开户').click()
