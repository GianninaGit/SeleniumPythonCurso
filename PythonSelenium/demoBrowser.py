# escribir webdriver y al colocarse encima se importa el selenium webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#webdriver.Chrome() #luego selecciono la clase Chrome y lo coloco dentro de un objeto
path_variable = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service = path_variable)


#browser expone un archivo ejecutalbe que debemos invocar en el (),
# ir a selenium.dev/downloads/ y abajo browsers

#get method to git url on browser:
driver.get("https://www.youtube.com/watch?v=L9VHL8d_4Z8&t=1327s&ab_channel=Pachi%22FueradeCarril%22")
driver.maximize_window()

print(driver.title)
print(driver.current_url) #sirve para chequear hackeos si redirige a otra pag
driver.get("https://www.youtube.com/watch?v=VTP7Pk9vrzo&t=213s&ab_channel=Pachi%22FueradeCarril%22")
driver.minimize_window()
driver.back()
driver.refresh()


#para detener la ejecución, se hace debug.Se pone un break despues de minimizar.
#apretando a la izq para que aparezca el boton rojo. y en vez de play, apretar el bichito
#entonces esto hace que vaya paso por paso y se pueda apretar step over para ir paso por paso
driver.close() #cierra la pag invocada con el get
#driver.quit() cierra las ventanas que quedan abiertas cuando se clickea algo y se abre una ventana nueva

