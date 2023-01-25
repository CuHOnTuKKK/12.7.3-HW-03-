#  Для запуска теста введи в терминале -  python -m pytest -v --driver Chrome --driver-path chrom.exe tests_rt.py

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from Conf import *

driver = webdriver.Chrome(executable_path="chrome.exe")

# TASK-01 .Вход по номеру телефона.


def test_auth_tel():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == email


# TASK-02 .Вход по email


def test_auth_email():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == email


# TASK-03. Вход по логину


def test_auth_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(login)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == email


# TASK-04. Вход по лицевому счету


def test_auth_account_number():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
        account_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == email


# TASK-05. Попытка входа через почту с невалидным паролем


def test_invalid_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(inv_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


# TASK-06. Попытка входа через невалидную почту и валидный пароль


def test_invalid_email():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(inv_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


# TASK-07. Попытка входа через невалидную почту и невалидный пароль


def test_invalid_email_invalid_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(inv_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(inv_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


# TASK-08. Попытка входа через почту с пустыми полями


def test_void_email_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(void_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(void_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


# TASK-09. Регистрация пользователя в пароле менее 8 символов (7)


def test_lesser_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(lesser_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        lesser_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'


# TASK-10.Регистрация пользователя в пароле больше 20 символов (21)


def test_bigger_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(bigger_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        bigger_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не более 20 символов'


# TASK-11. Регистрация пользователя в пароле кириллические символы


def test_cyrillic_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(cyrillic_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        cyrillic_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать только латинские буквы'


# TASK-12.Регистрация пользователя в пароле нет заглавной буквы


def test_no_caps_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_caps_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_caps_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы одну заглавную букву'


# TASK-13.Регистрация пользователя в пароле нет цифры или спецсимвола


def test_no_numbers_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_numbers_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_numbers_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'


# TASK-14.  Авторизация по номеру телефона, с незаполненым полем Мобильный телефон


def test_void_phone():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(void_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите номер телефона'


# TASK-15.  Авторизация по почте, с пустым полем Электронная почта


def test_void_email():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(void_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите адрес, указанный при регистрации'

# TASK-16 Переход по ссылке авторизации пользователя с помощью VK.

def test_try_auth_with_vk():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, 'oidc_vk'))).click()

    assert driver.current_url.__contains__('oauth.vk.com')
    driver.quit()

# TASK-17 Переход по ссылке авторизации пользователя с помощью OК.


def test_try_auth_with_ok():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, 'oidc_ok'))).click()

    assert driver.current_url.__contains__('connect.ok.ru')
    driver.quit()

# TASK-18 Переход по ссылке авторизации пользователя с помощью Mail.ru.

def test_try_auth_with_mail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, 'oidc_mail'))).click()

    assert driver.current_url.__contains__('connect.mail.ru')
    driver.quit()

# TASK-19 Переход по ссылке авторизации пользователя с помощью Google.

def test_try_auth_with_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, 'oidc_google'))).click()

    assert driver.current_url.__contains__('accounts.google.com')
    driver.quit()

# TASK-20 Переход по ссылке авторизации пользователя с помощью Yandex.

def test_try_auth_with_yandex():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, 'oidc_ya'))).click()

    assert driver.current_url.__contains__('oauth.yandex.ru')
    driver.quit()

driver.close()