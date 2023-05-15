from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

usr = input('Введите логин: ')
pwd = input("Введите пароль: ") + '\n'

driver = webdriver.Chrome('drivers/chromedriver.exe')
driver.get('http://sgo.monrk.ru/authorize/login')
print("Opened Chrome")
sleep(7)

org_box = driver.find_element(By.CLASS_NAME, 'select2-selection__arrow')
org_box.click()
org_box = driver.find_element(By.CLASS_NAME, 'select2-search__field')
org_box.clear()
org_box.send_keys('экг')
sleep(1)
org_box.send_keys(Keys.ENTER)
sleep(4)

username_box = driver.find_element('name', 'loginname')
username_box.clear()
username_box.send_keys(usr)
print("Login entered")
sleep(4)

password_box = driver.find_element('name', 'password')
password_box.clear()
password_box.send_keys(pwd)
print("Password entered")
print("Done")
sleep(7)

mark_box = driver.find_element(By.ID, '11')
mark_box.click()
sleep(5)

form_box = driver.find_element(By.XPATH, '//*[@title="Сформировать"]')
form_box.click()
sleep(3)

marks_avg_text_box = driver.find_elements(By.CLASS_NAME, 'cell-text')
marks_avg_num_box = driver.find_elements(By.CLASS_NAME, 'cell-num')
print('Marks:')
for i in range(len(marks_avg_text_box)):
    print(f"{marks_avg_text_box[i - 1].text}: {marks_avg_num_box[i - 1].text}")
sleep(3)

exit_box = driver.find_element(By.XPATH, '//*[@title="Выход"]')
exit_box.click()
sleep(2)
exit_btn_box = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
exit_btn_box.click()
sleep(5)
print('Exit')
