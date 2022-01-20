from selenium import webdriver
import yaml

conf = yaml.safe_load(open('login.yml'))
rpos_login = conf['rpos_user']['login']
rpos_password = conf['rpos_user']['password']

driver = webdriver.Chrome()


def login(url, EPC_USERNAME, username, EPC_PASSWORD, password, EPC_LOGIN_BTN):
    driver.get(url)
    driver.find_element_by_id(EPC_USERNAME).send_keys(username)
    driver.find_element_by_id(EPC_PASSWORD).send_keys(password)
    driver.find_element_by_id(EPC_LOGIN_BTN).click()


login("https://www.jlr.unipart.co.uk/RIM/Login.jsp", "EPC_USERNAME",
      rpos_login, "EPC_PASSWORD", rpos_password, "EPC_LOGIN_BTN")
