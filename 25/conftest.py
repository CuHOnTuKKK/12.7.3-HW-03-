import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chrom.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.implicitly_wait(30)
    pytest.driver.set_window_size(1400, 1000)

    yield

    pytest.driver.quit()