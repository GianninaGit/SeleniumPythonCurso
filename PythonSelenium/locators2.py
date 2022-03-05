#from selenium.webdriver.common.by import By
#y usar
#element = driver.find_element(By.NAME, "element_name")
#igual para tener la misma versión que en el curso, puse en la terminal la versión de pycharm con estos comandos:
#1. Run pip uninstall selenium==4.0.0 in PyCharm Terminal
#2. Then run pip install selenium==3.141.0 in PyCharm Terminal
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://sso.teachable.com/secure/9521/identity/login")

#WebLocators as XPATH and CSS, can be built from any object in the web page, no dependen de las propiedades definidas por los devs.
#CSS tagname[atributo="valor"] -> Esto buscarlo en inspect element: input[name='name']
     #Luego ir a Console, borrar con el botón redondo, y tipear $("aca poner lo de arriba en comillas") para chequear que está bien mapeado
driver.find_element_by_css_selector("input[id='email']").send_keys("avon.gianni@gmail.com")
driver.find_element_by_name("password").send_keys("kkkkkkk")
driver.find_element_by_id("remember_me").click()

#XPATH //tagname[@attribute='value'], en Console buscarlo con $x("//tagname[@attribute='value']")
driver.find_element_by_xpath("//*[@type='submit']").click()

#CLASS cada clase se separa con un espacio, usar solo uno entre "". Chequear que el texto de éxito aparece en pantalla:
print(driver.find_element_by_class_name("auth-flash-error").text)  #Para ver si está bien mapeado, en chrome CSS: chropath div[class*="bodySmall"]
                                                        #ver abajo "1 element matching"
