
from selenium import webdriver
import requests
import time
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class test:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get('https://om.qq.com/userAuth/index')
        self.driver.find_element_by_xpath('//div[@class="other-type"]').click()
        email = self.driver.find_element_by_xpath('//input[@class="email-input error"]').send_keys(
            "2551513277@qq.com")
        password = self.driver.find_element_by_xpath('//input[@placeholder="密码"]')
        password.send_keys("123456lkj")
        self.driver.find_element_by_xpath('//button[@class="btnLogin btn btn-primary"]').click()
        time.sleep(5)
        self.driver.switch_to_frame("tcaptcha_iframe")
        slidebg_url = self.driver.find_element_by_xpath('//img[@id="slideBg"]'
                                                   ).get_attribute('src')
        slideblock_url = self.driver.find_element_by_xpath('//img[@id="slideBlock"]'
                                                   ).get_attribute('src')
        self.left = int(self.driver.find_element_by_xpath('//img[@id="slideBlock"]'
                                                   ).get_attribute('style').split(';')[3].split(':')[1][:-2])

        slidebg = requests.get(slidebg_url).content
        slideblock = requests.get(slideblock_url).content
        for key, value in {'slidebg.png': slidebg, 'slideblock.png': slideblock}.items():
            with open(key, 'wb') as f:
                f.write(value)

    def FindPic(self, target, template):
        """
        找出图像中最佳匹配位置
        :param target: 目标即背景图
        :param template: 模板即需要找到的图
        :return: 返回最佳匹配及其最差匹配和对应的坐标
        """
        target_rgb = cv2.imread(target)
        target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
        template_rgb = cv2.imread(template, 0)
        res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
        value = cv2.minMaxLoc(res)
        a, b, c, d = value
        if abs(a) > abs(b):
            return c
        else:
            return d

    def crack_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tc-drag-thumb")))
        ActionChains(self.driver).click_and_hold(slider).perform()

        for track in self.tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.5)
        for back_tracks in self.tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        ActionChains(self.driver).move_by_offset(xoffset=-4, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=4, yoffset=0).perform()
        time.sleep(0.5)

        ActionChains(self.driver).release().perform()

    def get_tracks(self, distance):
        print(distance)
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3 / 5  # 减速阀值
        while current < distance:
            if current < mid:
                a = 2  # 加速度为+2
            else:
                a = -3  # 加速度-3
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        self.tracks = {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def run(self):
        distance = self.FindPic('slidebg.png', 'slideblock.png')[0]
        distance = (distance-self.left+25)*0.5
        self.get_tracks(distance)
        self.crack_slider()


if __name__ == '__main__':

    test1 = test()
    test1.run()










