from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup as bs
# import requests
from time import sleep
from warnings import simplefilter
simplefilter("ignore")

URL = "https://mcpedl.com/"

# Initalizing selenium 
user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
options = Options()
options.add_argument(f"user-agent:{user_agent}")
options.add_argument("--window-size=300,1000")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window() 
driver.get(URL)

class GetLinks:
    def bedrockMod(self,query: str):
        self.operator.searchBedrock(query)


    def __init__(self):

        self.operator = _WebScrapping()



class _WebScrapping:
    def searchBedrock(self,query: str):

        search_button = "/html/body/div[1]/div/div/header/div/div/div[1]/button"
        search_bar = "/html/body/div[1]/div/div/div/aside/div/div[2]/form/div/input"

        driver.find_element(by=By.XPATH,value=search_button).click()
        sleep(0.5)
        driver.find_element(by=By.XPATH,value=search_bar).send_keys(query + Keys.ENTER)
        driver.find_element(by=By.XPATH,value=search_button).click()
        sleep(1)
        return self.getFirstResultBedrock(3)


    def getFirstResultBedrock(self,result: int):
        sleep(1)

        # This will make sure that it run the same amount of time specefied in results
        # Remaning can at max be 2
        if result >= 2:
            remaning = 2
        else:
            remaning = 1
        results = []
        i = 1
        while(result > 0):
            for j in range(1,remaning + 1):
                sleep(5)
                title_xpath = rf"/html/body/div[1]/div/div/div/div/div/div[2]/div[{i}]/div[{j}]/div[3]/div[1]/a" # /html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/a # /html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/a
                desc_xpath = rf"/html/body/div[1]/div/div/div/div/div/div[2]/div[{i}]/div[{j}]/div[3]/div[2]" # /html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[2] # /html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[2]
                img_xpath = rf"/html/body/div[1]/div/div/div/div/div/div[2]/div[{i}]/div[{j}]/div[2]/img" # /html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/img # /html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/img
                title = driver.find_element(by=By.XPATH,value=title_xpath).text
                desc = driver.find_element(by=By.XPATH,value=desc_xpath).text
                img_src = driver.find_element(by=By.XPATH,value=img_xpath).get_attribute("src")
                results.append([title,desc,img_src])
                sleep(5)
                result -= 1

            if result >= 2:
                remaning = 2
            else:
                remaning = 1
            i += 1

        print(results)
        return results
                    

    # def scrapBedrock(self):
    #     request = requests.get(URL)
    #     website = bs(request)
    #     print(website.prettify())


if __name__ == "__main__":
    obj = GetLinks()
    obj.bedrockMod("More Tools Mod")
    sleep(1000)
    