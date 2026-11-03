import pytest
from pathlib import Path
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")

        if driver:
            carpeta = Path("capturas")
            carpeta.mkdir(exist_ok=True)

            nombre = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo = carpeta / f"error_{nombre}.png"

            driver.save_screenshot(str(archivo))

            print(f"Captura guardada en: {archivo}")