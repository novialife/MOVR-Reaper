import random
import warnings
import keyboard
from selenium import webdriver
import time
import base64

from selenium.webdriver import ActionChains

from solver import PuzzleSolver

warnings.filterwarnings("ignore")


def wait_for_f8():
    while True:
        if keyboard.is_pressed("f8"):
            return


def change_window(windows, nr):
    driver.switch_to.window(windows[nr])


def close_window(windows, nr):
    driver.switch_to.window(windows[nr])
    driver.execute_script("window.close();")
    windows.pop(nr)
    return windows


def tryAgainCaptcha():
    driver.find_elements_by_xpath("//*[@id='__next']/div/section/div[2]/div/div/div[2]/div[2]/div/div[1]")[
        0].screenshot(
        "captcha.png")


def getCaptcha():
    # Clicks the "I am human" button
    driver.find_elements_by_xpath(
        "/html/body[@class='antialiased overflow-x-hidden text-gray-100']/div[@id='__next']/div[@class='flex flex-col "
        "min-h-screen ']/section[@class='flex flex-col items-center w-full']/div[@class='mt-4']/div["
        "@class='scaptcha-container']/div/div[@class='scaptcha-anchor-container scaptcha-anchor-element']/button["
        "@class='scaptcha-anchor-checkbox scaptcha-anchor-checkbox-default scaptcha-anchor-element']")[0].click()
    time.sleep(5)
    # Saves the captcha as image
    driver.find_elements_by_xpath("//*[@id='__next']/div/section/div[2]/div/div/div[2]/div[2]/div/div[1]")[
        0].screenshot(
        "captcha.png")


def getCaptchaPiece():
    c = driver.find_elements_by_xpath("//*[@id='__next']/div/section/div[2]/div/div/div[2]/div[2]/div/div[2]")[
        0].value_of_css_property("background-image")
    c = c[27:]
    c = c[:len(c) - 2]
    c = bytes(c, 'utf-8')
    with open("piece.png", "wb") as fh:
        fh.write(base64.decodebytes(c))


def solveCaptcha():
    attempts = 0
    while checkCheckbox() is False:
        # time.sleep(random.randint(1, 10))
        if attempts == 0:
            getCaptcha()
        else:
            tryAgainCaptcha()

        getCaptchaPiece()
        solver = PuzzleSolver("piece.png", "captcha.png")
        try:
            distance = solver.get_position()
            dragSlider(distance)
        except:
            pass
        attempts += 1


def checkCheckbox():
    checkbox = driver.find_elements_by_xpath("//*[@id='__next']/div/section/div[2]/div/div/div/button")[0]
    return checkbox.get_attribute("class") == "scaptcha-anchor-checkbox false scaptcha-anchor-element"


def dragSlider(distance):
    slider = driver.find_elements_by_xpath(
        "//*[@id='__next']/div/section/div[2]/div/div/div[2]/div[2]/div/div[3]/div[5]")
    ac = ActionChains(driver)
    ac.move_to_element(slider[0])
    ac.click_and_hold(slider[0])
    xoffset = 0
    while xoffset < distance:
        xmove = random.randint(10, 50)
        ymove = random.randint(-1, 1)
        ac.move_by_offset(xmove, ymove)
        xoffset += xmove
    ac.release()
    ac.perform()

    time.sleep(3)


def importMMWallet():
    wait_for_f8()
    # driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/div/button").click()
    # time.sleep(1)
    # driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button").click()
    # time.sleep(1)
    # driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]").click()
    # time.sleep(1)
    driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/form/div[4]/div[1]/div/input").send_keys('entry asset tip drum green month one meat initial kick jealous elite')
    time.sleep(1)
    driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/form/div[4]/div[1]/div/input").send_keys('hejhej123')
    time.sleep(1)
    driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/form/div[4]/div[1]/div/input").send_keys('hejhej123')
    time.sleep(1)
    driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/form/div[7]/div").click()
    time.sleep(1)
    driver.find_elements_by_xpath("//*[@id='app-content']/div/div[2]/div/div/form/button").click()


pass


def main():
    global driver
    options = webdriver.ChromeOptions()
    options.add_extension('extension_10_8_1_0.crx')
    driver = webdriver.Chrome("C:/Users/merva/Desktop/chromedriver.exe", options=options)
    # try:
    #     driver = webdriver.Chrome("C:/Users/merva/Desktop/chromedriver.exe", options=options)
    # except:
    #     pass
    time.sleep(5)
    importMMWallet()
    driver.execute_script("window.open('https://movr.supply');")

    windows = driver.window_handles
    windows = close_window(windows, 1)

    change_window(windows, 1)
    solveCaptcha()
    print("Success!!")
    driver.quit()
    quit()


main()
