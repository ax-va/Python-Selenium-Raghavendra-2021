# Code like below does not work:
"""
element = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")

from selenium.webdriver import ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()
"""
