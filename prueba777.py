import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # CASO 1: Login exitoso
    driver.get("https://www.saucedemo.com/")

    usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    usuario.send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))
    print("Login exitoso")
    time.sleep(10)
    # CASO 2: Agregar producto
    boton = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton.click()
    time.sleep(10)
    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    print("Productos en el carrito:", badge.text)
finally:
    driver.quit()