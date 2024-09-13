import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import os

# Asegúrate de que el directorio de reports exista
reports_dir = 'reports'
os.makedirs(reports_dir, exist_ok=True)

# Configuración para escritura de log en reporte
logging.basicConfig(
    filename='reports/test_execution.log',  # Ruta del archivo de log
    level=logging.INFO,  # Nivel de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
)

@pytest.fixture(scope="function")
def setup():
    # Configura el servicio de ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)
    logging.info("Navegador abierto y página de DemoBlaze cargada.")
    yield driver
    driver.quit()
    logging.info("Navegador cerrado.")


def test_compra(setup):
    driver = setup

    logging.info("Inicio del test de compra.")
    # 1. Agregar dos productos al carrito
    # Se agrega el primer producto Samsung Galaxy S6
    logging.info("Se agrega primer producto al carrito.")
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    logging.info("Primer producto agregado al carrito.")

    driver.get("https://www.demoblaze.com/")

    # Agregar el segundo producto  Sony Xperia Z5
    logging.info("Se agrega segundo producto al carrito.")
    driver.find_element(By.LINK_TEXT, "Sony xperia z5").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    logging.info("Segundo producto agregado al carrito.")

    # 2. Visualizar el carrito
    logging.info("Se visualizando el carrito.")
    driver.find_element(By.ID, "cartur").click()
    time.sleep(3)

    # 3. Completar el formulario de compra
    logging.info("Se completa el formulario de compra.")
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
    driver.find_element(By.ID, "name").send_keys("Alexander")
    driver.find_element(By.ID, "country").send_keys("Ecuador")
    driver.find_element(By.ID, "city").send_keys("Quito")
    driver.find_element(By.ID, "card").send_keys("1234 5678 9123 4567")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2024")
    time.sleep(2)

    # 4. Finalizar la compra
    logging.info("Se finalizando la compra.")
    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
    time.sleep(5)

    # Verificar que el pedido fue completado
    confirmation_message = driver.find_element(By.XPATH, "//h2[text()='Thank you for your purchase!']").text
    logging.info("Confirmación de compra: %s", confirmation_message)
    assert "Thank you for your purchase!" in confirmation_message
    logging.info("Prueba de compra completada con éxito!.")
