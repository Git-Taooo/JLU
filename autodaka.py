#encoding:utf-8
from selenium import webdriver
import time
import json
import datetime

def openChrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    options.add_argument('window-size=1600x900') # 指定浏览器分辨率
    options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
    options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
    #options.add_argument('--headless') # 浏览器不提供可视化页面.linux下如果系统不支持可视化不加这条会启动失败
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=options,executable_path='D:\\Anaconda\\chromedriver')
    #driver.set_page_load_timeout(10)
    return driver

def operate_dk(driver,name,pw,msurl):
    url = "https://ehall.jlu.edu.cn"
    driver.get(url)
    elem = driver.find_element_by_id("username")
    elem.send_keys(name)
    elem = driver.find_element_by_id("password")
    elem.send_keys(pw)
    try:
        driver.find_element_by_id("login-submit").click()

    except Exception as e:
        print("")

    url = "https://ehall.jlu.edu.cn/infoplus/form/YJSMRDK/start"
    driver.get(url)
    time.sleep(5)
    elem = driver.find_element_by_id("V1_CTRL40")
    elem.clear()
    elem.send_keys(u"电子信息")
    elem = driver.find_element_by_id("V1_CTRL41")
    elem.send_keys("2020")
    elem = driver.find_element_by_id("V1_CTRL42")
    elem.send_keys(u"中心校区")
    elem = driver.find_element_by_id("V1_CTRL7")
    elem.send_keys(u"文苑6公寓")
    elem = driver.find_element_by_id("V1_CTRL8")
    elem.clear()
    elem.send_keys("417")

    driver.find_element_by_id("V1_CTRL44").click()
    driver.find_element_by_id("V1_CTRL28").click()

    try:
        driver.find_element_by_id("V1_CTRL19").click()
        driver.find_element_by_id("V1_CTRL23").click()
    except Exception as e:
        pass
    try:
        driver.find_element_by_class_name('command_button_content').click()
        time.sleep(5)
        driver.find_element_by_css_selector('.dialog_button.default.fr').click()
        time.sleep(5)
        wxpost("打卡成功！",msurl)
    except Exception as e:
        wxpost("打卡失败！",msurl)

    return


def wxpost(content,msurl):
    time = datetime.datetime.now().strftime('%H')+"时"+datetime.datetime.now().strftime('%M')+"分"+datetime.datetime.now().strftime('%S')+"秒"
    driver.get(msurl+content+time)


if __name__ == '__main__':
    print("这是一个自动健康打卡的程序。")
    driver = openChrome()
    operate_dk(driver, "zhangdx20", "zdx19981006","https://sc.ftqq.com/SCU117990T162e5b67dea4ea8e857cb0c459aff7015f853653461bc.send?text=")
    driver.close()
    driver = openChrome()
    operate_dk(driver,"wangtao20","243613492wt","https://sc.ftqq.com/SCU118073T820da58ecb224bd24232663e608e7d995f85b1b9ce517.send?text=")
    driver.close()
    driver = openChrome()
    operate_dk(driver, "sunxh20", "302614aaaa","https://sc.ftqq.com/SCU118081Tca2319e134c4b8bdbad9cafd534678d55f85b8d718d78.send?text=")
    driver.close()
    driver = openChrome()
    operate_dk(driver, "lengzq20", "lengzhaoqi0409","https://sc.ftqq.com/SCU118073T820da58ecb224bd24232663e608e7d995f85b1b9ce517.send?text=")
    driver.close()

    print("微信打卡成功")