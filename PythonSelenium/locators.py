#from selenium.webdriver.common.by import By
#y usar
#element = driver.find_element(By.NAME, "element_name")
#igual para tener la misma versión que en el curso, puse en la terminal la versión de pycharm con estos comandos:
#1. Run pip uninstall selenium==4.0.0 in PyCharm Terminal
#2. Then run pip install selenium==3.141.0 in PyCharm Terminal
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/#/practice-project")
#driver.maximize_window()
driver.find_element_by_name("name").send_keys("Giannina")
driver.find_element_by_name("email").send_keys("giannisarappa@gmail.com")
driver.find_element_by_name("agreeTerms").click()

