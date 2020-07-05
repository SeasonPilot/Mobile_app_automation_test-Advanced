# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/7/5 12:44
# 文件名：20190522.py
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
caps["chromedriverExecutableDir"] = "D:\Chromedriver\chromedriver_win32"

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(20)
# 打印上下文
print(driver.contexts)

driver.find_element_by_xpath('//*[@text="交易"]').click()
time.sleep(3)

# driver.find_element_by_accessibility_id('基金开户').click()

# 获得所有可用于自动化的上下文
print(driver.contexts)
# 获取运行Appium的当前上下文  （Get the current context in which Appium is running）
print(driver.current_context)
# 切换context  (切换到webvierw)
driver.switch_to.context(driver.contexts[1])
print(driver.current_context)
time.sleep(3)

# 点击A股开户
driver.find_element_by_css_selector(".trade_home_agu_3ki .trade_home_info_3aI").click()

time.sleep(5)

# 检索会话可用的所有窗口句柄的列表（仅Web上下文） Retrieve the list of all window handles available to the session (Web context only)
print(driver.window_handles)
# 切换窗口
driver.switch_to.window(driver.window_handles[1])


# 点击中信证券立即开户  只有图片的Class可以定位
driver.find_element_by_css_selector(".open_more_plusImg_rAz").click()


# 检索会话可用的所有窗口句柄的列表（仅Web上下文） Retrieve the list of all window handles available to the session (Web context only)
print(driver.window_handles)

# 切换窗口
driver.switch_to.window(driver.window_handles[2])

# 输入手机号  原生ID定位
driver.find_element_by_id("mobile").send_keys("185987654")
time.sleep(5)

# 清除之前的输入
driver.find_element_by_id("mobile").clear()

# css id 定位
driver.find_element_by_css_selector("#mobile").send_keys("789456123")
time.sleep(5)

driver.find_element_by_id("validCode").send_keys("156418")