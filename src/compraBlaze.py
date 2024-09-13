from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura el servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicia el navegador con el servicio de ChromeDriver
driver = webdriver.Chrome(service=service)

# Abre la página de DemoBlaze
driver.get("https://www.demoblaze.com/")

# Espera hasta que la página esté completamente cargada
driver.implicitly_wait(10)

# 1. Agregar dos productos al carrito
# Agregar el primer producto (ejemplo: Samsung Galaxy S6)
first_product = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
first_product.click()

# Espera a que cargue la página del producto
time.sleep(3)

# Agregar al carrito
add_to_cart_button = driver.find_element(By.XPATH, "//a[text()='Add to cart']")
add_to_cart_button.click()

# Espera para la alerta de confirmación
time.sleep(3)
driver.switch_to.alert.accept()

# Regresar a la página principal
driver.get("https://www.demoblaze.com/")

# Agregar el segundo producto (ejemplo: Sony Xperia Z5)
second_product = driver.find_element(By.LINK_TEXT, "Sony xperia z5")
second_product.click()

# Espera a que cargue la página del producto
time.sleep(3)

# Agregar al carrito
add_to_cart_button = driver.find_element(By.XPATH, "//a[text()='Add to cart']")
add_to_cart_button.click()

# Espera para la alerta de confirmación
time.sleep(3)
driver.switch_to.alert.accept()

# 2. Visualizar el carrito
driver.find_element(By.ID, "cartur").click()

# Espera un par de segundos para ver el carrito
time.sleep(5)

# 3. Completar el formulario de compra
# Hacer clic en "Place Order"
place_order_button = driver.find_element(By.XPATH, "//button[text()='Place Order']")
place_order_button.click()

# Completar el formulario de compra
driver.find_element(By.ID, "name").send_keys("Alexander")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Quito")
driver.find_element(By.ID, "card").send_keys("1234 5678 9123 4567")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2024")
time.sleep(3)

# 4. Finalizar la compra
purchase_button = driver.find_element(By.XPATH, "//button[text()='Purchase']")
purchase_button.click()

# Espera para ver el resultado final
time.sleep(5)

# Cierra el navegador
driver.quit()
