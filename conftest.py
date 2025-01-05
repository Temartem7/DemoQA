import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver(request):
    # Get the 'headless' flag from pytest command-line options (default is False)
    headless = request.config.getoption("--headless")
    # Setup Chrome options
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")  # Run headless mode if flag is passed
        #chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU in headless mode
        #chrome_options.add_argument("--no-sandbox")  # Optional: For Linux-based environments

    # Setup Chrome driver with the options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # Maximize window if not headless
    if not headless:
        driver.maximize_window()
    yield driver  # Yield the driver to your tests
    driver.quit()  # Cleanup after test completes

def pytest_addoption(parser):
    # Define the 'headless' command-line option
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )
