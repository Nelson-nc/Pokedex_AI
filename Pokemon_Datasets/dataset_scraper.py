import os
import time
import random
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_dataset(query):
        service = webdriver.ChromeService('drivers/chromedriver.exe')

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in background

        driver = webdriver.Chrome(service=service, options=options)

        try:
                driver.get(f"https://www.google.com/search?sca_esv=763607e259d953c2&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeuYzzFkfneXafNx6OMdA4MQRJc_t_TQjwHYrzlkIauOK_IaFSQcTHs2AgJbmYqOLNlPDT0Hy19TTgd1LyYk-nASP6vwo8-B6loSdTVvF3_GZTcdVGGW23Vv5QDzGwSEW9k88_VoukSq6yQOfA5dBvYDoc8JpoXMA6o9PqbsvZLaqjcfYgw&q={query}&sa=X&ved=2ahUKEwj49oS0zeSRAxWeZ0EAHbzKKnkQtKgLegQIFhAB&biw=1366&bih=607")
                time.sleep(random.uniform(1, 3))

                driver.execute_script("window.scrollTo(0,document.body.ScrollHeight);")

                images = driver.find_elements(By.XPATH, "//img[contains(@class, 'YQ4gaf')]")
                src = [img.get_attribute("src") for img in images]

                count = 0

                for i in range(len(src)):
                        ext = str(src[i]).split(",")[0].split("/")[1].split(";")[0]

                        if ext not in ['png', 'jpg', 'jpeg']:
                                continue

                        urlretrieve(str(src[i]), f"Pokemon_Datasets/datasets/{query}/{query}_({i})_.{ext}")
                        print(f"Saved: Pokemon_Datasets/datasets/{query}/{query}_({i})_.{ext}")

                        count += 1
                        time.sleep(random.uniform(1, 3))
                        
                        if count >= 60:
                                break

        except Exception as e:
                print("Error: ", e)

        finally:
                driver.quit()



if __name__ == '__main__':
        pokemon_name = os.listdir("Pokemon_Datasets/datasets")

        for pokemon in pokemon_name:
                get_dataset(query=pokemon)
