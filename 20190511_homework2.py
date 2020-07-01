# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/6/29 21:27
# 文件名：20190511_homework2.py
# 开发工具：PyCharm
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["deviceName"] = "sanxing"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["platformName"] = "Android"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)
driver.find_element_by_id("com.xueqiu.android:id/image_cancel").click()
driver.find_element_by_xpath("//*[contains(@resource-id,'appbar')]//*[@text='基金']").click()

time.sleep(2)
rect = driver.get_window_rect()
actions = TouchAction(driver)
def swipe():
    for i in range(5):
        actions.press(x=rect['width'] * 0.8, y=rect['height'] * 0.8)\
            .move_to(x=rect['width'] * 0.2,y=rect['height'] * 0.2)\
            .release()\
            .perform()                                                                 # 忘记写x=， y= 了

def left_swipe():
    actions.press(x=rect['width'] * 0.8, y=rect['height'] * 0.5)\
        .move_to(x=rect['width'] * 0, y=rect['height'] * 0.5)\
        .release()\
        .perform()

swipe()
for i in range(7):
    left_swipe()
    swipe()


driver.quit()
