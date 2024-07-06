from selenium import webdriver
from bs4 import BeautifulSoup
import time

def download_html(NCT):
    try:
        # Setup WebDriver (assuming ChromeDriver is installed and in PATH)
        driver = webdriver.Chrome()

        # Navigate to the webpage
        driver.get(f"https://clinicaltrials.gov/study/{NCT}")

        # Adjust the wait time as necessary.
        time.sleep(1) 

        # Get the fully rendered page source
        html_content = driver.page_source

        # Use BeautifulSoup to prettify the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        pretty_html = soup.prettify()

        # Save the prettified content to a file
        with open(f"{NCT}.html", "w", encoding="utf-8") as file:
            file.write(pretty_html)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        driver.quit()

# download_html('NCT03003143')
