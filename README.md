# Selenium4-Raghavendra-2021

The use of Selenium and Python is demonstrated by examples and tests based on Sujay Raghavendra's book "Python Testing with Selenium: Learn to Implement Different Testing Techniques Using the Selenium WebDriver" published by Apress in 2021. The book examples have been modified and also updated for Selenium 4. They end with an introduction to unittest and writing a Google search test using Page Object Model / Page Object Pattern.

You can see the examples in the 'examples' directory and the tests themselves in the 'tests' one. In 'utils/highlighter.py', the Highlighter class is written for highlighting HTML elements by changing the element style locally. In 'utils/screenshoter.py', the Screenshoter class encapsulates taking screenshots to make this task easier. Additionally, in the 'pom' folder, Page Object Model is represented in a very simple form. Then that model is inherited to describe the Google search action in browser.

The webdrivers containing in the project may be out of date, in which case you need to update them or download them in a different way than suggested here. It's worth noting that the paths of Firefox binaries are hardcoded and may differ from the paths on your system. You can check that in LOCATIONS in 'utils/locations.py'.

Verified with versions: python 3.8+, selenium 4.8.2, webdriver-manager 3.8.5, PyAutoGUI 0.9.53, Pillow 9.4.0. 

## Selenium Documentation 

https://www.selenium.dev/documentation/

## Unittest Documentation

https://docs.python.org/3/library/unittest.html
