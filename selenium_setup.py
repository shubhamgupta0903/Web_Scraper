# selenium_setup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode

    # Path to your chromedriver executable
    service = Service('/path/to/your/chromedriver')

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver
