# escribir webdriver y al colocarse encima se importa el selenium webdriver

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.ie.service import Service


#webdriver.Chrome() #luego selecciono la clase Firefox y lo coloco dentro de un objeto (https://www.selenium.dev/downloads/)
path_variable2 = Service("C:\\geckodriver.exe") #para firefox
#path_variable2 = Service("C:\\IEDriverServer.exe")

driver = webdriver.Firefox(service = path_variable2) #para firefox

#driver = webdriver.ie(service = path_variable2)
driver.get("https://www.youtube.com/watch?v=L9VHL8d_4Z8&t=1327s&ab_channel=Pachi%22FueradeCarril%22")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.get("https://www.youtube.com/watch?v=VTP7Pk9vrzo&t=213s&ab_channel=Pachi%22FueradeCarril%22")
driver.minimize_window()
driver.back()
driver.refresh()

#driver.close()