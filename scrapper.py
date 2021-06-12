from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
search_url='https://www.techwithtim.net/'
driver.get(search_url)
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

main = driver.find_element_by_id("main")
articles = main.find_elements_by_tag_name("article")
for article in articles:
    header = article.find_element_by_class_name("entry-meta")
    print(header.text)
    print("\n")

