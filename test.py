from selenium import webdriver
from login import LoginPage
import time
driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    time.sleep(10)

    login.ingresar_credenciales(
        "locked_out_user",
        "secret_sauce"
    )
    time.sleep(10)
    login.click_login()
    time.sleep(10)
    mensaje = login.obtener_error()

    print("Resultado de la prueba:", mensaje)
    time.sleep(10)
    assert "locked out" in mensaje.lower()

finally:
    driver.quit()
    