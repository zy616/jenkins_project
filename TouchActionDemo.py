from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
# 相关的启动参数
# 平台，大小写无所谓
desired_caps['platformName'] = 'Android'
# 搭载操作系统版本
desired_caps['platformVersion'] = '5.1'
# 设备名，可以随便写但是不能不写(Android),ios必须准确填写
desired_caps['deviceName'] = '192.168.56.101:5555'
#包名
desired_caps['appPackage'] = 'com.android.settings'
# 界面名
desired_caps['appActivity'] = '.Settings'
# 获取driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

ele = driver.find_element_by_xpath("//*[@text='More']")

# 轻敲
TouchAction(driver).tap(ele).perform()

# TouchAction(driver).press(ele).release().perform()
# 长按不论时间长短
# TouchAction(driver).long_press(ele).perform()


driver.network_connection
# 发送键到设备
driver.press_keycode(1)


# 操作手机通知栏

