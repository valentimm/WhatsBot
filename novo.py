from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#options.add_argument(
#   "user-data-dir-C:\\Users\\Matheus\\AppData\\Local\\Google\\Chrome\\User\\Default")
print ("Digite o nome do grupo")
group_name = input()
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com/")

driver.implicitly_wait(20)

chats = driver.find_elements(by="class name", value="zoWT4")
for chat in chats:
    if chat.text == group_name:
        chat.click()

time.sleep(5)

for contatos in driver.find_elements(by="class name", value="zzgSd"):
   # print (contatos.text)

    file = open("teste.txt", "w")
    file.write("Contatos do grupo "+ group_name + ": \n" + contatos.text)
print("Feito!")