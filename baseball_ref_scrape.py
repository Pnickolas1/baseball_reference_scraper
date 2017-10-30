import platform
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
import requests
versionCode = platform.python_version()
print ("Python version ", versionCode)


url = "https://unsplash.com"

driver = webdriver.Firefox(executable_path=r'geckodriver')

driver.get(url)

#scroll page and wait 5 seconds

driver.execute_script("window.scrollTo(0,1000);")

time.sleep(5)


driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)
image_elements = driver.find_elements_by_css_selector("#gridMulti img")
i = 0

for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1