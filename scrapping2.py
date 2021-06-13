#ActionChains & Automating Cookie Clicker
"""
We will be working on ActionChains like Drag and drop, Double Click, Long Press 
It will be clicking the cookies automatically and clicking the cursor from the selected number of cookies earned.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://orteil.dashnet.org/cookieclicker")
cookies = driver.find_element_by_id("bigCookie")
cookies_count = driver.find_element_by_id("cookies")



driver.implicitly_wait(10)
actions = ActionChains(driver)
actions.click(cookies)
cursor = driver.find_element_by_id("productPrice0")

for i in range(50000):
    actions.perform()
    value = cookies_count.text.split(" ")[0]
    value = int(value)
    price = int(driver.find_element_by_id("productPrice0").text)

    if price <= value:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(cursor)
        upgrade_actions.click()
        upgrade_actions.perform()    




