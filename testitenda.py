import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    opciones = Options()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")
    navegador = webdriver.Chrome(options=opciones)
    yield navegador
    navegador.quit()

def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.ingresar_credenciales(
        "locked_out_user",
        "secret_sauce"
    )
    login.click_login()

    assert "locked out" in login.obtener_error().lower()


def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.ingresar_credenciales(
        "standard_user",
        "secret_sauce"
    )
    login.click_login()
    time.sleep(10)
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    #assert "pagina_incorrecta" in driver.current_url

    assert "inventory.html" in driver.current_url


def test_agregar_carrito(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.ingresar_credenciales(
        "standard_user",
        "secret_sauce"
    )
    login.click_login()
    time.sleep(10)
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton.click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "1"