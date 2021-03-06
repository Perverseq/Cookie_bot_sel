from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(".\\chromedriver.exe")
driver.get("http://orteil.dashnet.org/cookieclicker/")


def click():
    cookie = driver.find_element_by_id("bigCookie")
    cookie.click()


def buy_upgrades():
    try:
        upgrade = driver.find_element_by_xpath("//*[@class='crate upgrade enabled' and contains (@id, 'upgrade0')]")
        upgrade.click()
    except NoSuchElementException:
        pass


def buy_cursors():
    try:
        cursor = driver.find_element_by_xpath('//*[@class="product unlocked enabled" and contains (@id, "product0")]')
        cursor.click()
    except NoSuchElementException:
        pass


def buy_grandmas():
    try:
        grandma = driver.find_element_by_xpath('//*[@class="product unlocked enabled" and contains (@id, "product1")]')
        grandma.click()
    except NoSuchElementException:
        pass


def main():
    for _ in range(1, 1500):
        click()
        buy_cursors()
        buy_grandmas()
        buy_upgrades()
    driver.close()


if __name__ == "__main__":
        main()
