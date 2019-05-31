# 导模块
from appium import webdriver

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

driver.find_elements_by_id()
driver.quit()
