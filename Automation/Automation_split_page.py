import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.service import service
from zipfile import ZipFile
import os

location=os.getcwd()

preferences= {"download.default_directory":location}
#ops=webdriver.ChromeOptions()
#ops.add_experimental_option("prefs",preferences)

#ser_obj=service("C://Users//Hp//PycharmProjects//newpythonProject//venv//Scripts//chromedriver.exe")
#driver=webdriver.chrome(service=ser_obj,options=ops)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",preferences)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)
wait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[Exception])

#accessing webpage
driver.get("https://www.docsumo.com/")
driver.maximize_window()

#browser actions
act=ActionChains(driver)

tools=driver.find_element(By.XPATH,"//div[@class='nav-dropdown-text'][normalize-space()='Tools']")
split=driver.find_element(By.XPATH,"//div[contains(text(),'Split PDF by Page')]")

act.move_to_element(tools).move_to_element(split).click().perform()

# upload file
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(r"C:\Users\Hp\Downloads\pdfsample\pdfsample\pdfsample_1_4.pdf")

#ExplicitWait=wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
#ExplicitWait.click()
time.sleep(5)


wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='review-popup']/iframe")))
frame_split=driver.find_element(By.XPATH,"//*[@id='review-popup']/iframe")
driver.switch_to.frame(frame_split)
time.sleep(5)
expected_pages=int(driver.find_element(By.XPATH,"//div[@class='f2b2c']").get_attribute("innerText"))
expected1=int(expected_pages)
print("expected",expected_pages)
time.sleep(5)
driver.find_element(By.XPATH,"//button[contains(text(),'Split by page range')]").click()
split_all_pages=driver.find_element(By.XPATH,"//div[text()='Split all pages']")
driver.execute_script("arguments[0].click();", split_all_pages)



ExplicitWait_button=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_3CxWl']/button")))
driver.execute_script("arguments[0].click();", ExplicitWait_button)

#download

print(location)

time.sleep(10)
with ZipFile("pdfsample_1_4.zip", 'r') as zip_ext:
    # Extracting specific file in the zip
    # into a specific location.
    zip_ext.extractall(location)

time.sleep(10)

#driver.find_element(By.ID,"downloadpdf-text").click()
lst = os.listdir("pdfsample_1_4") # your directory path
number_files = len(lst)
print("actual",number_files)

if number_files==expected1:
    print("actual pages are equal to expected files ")

assert number_files==expected1
print("True")