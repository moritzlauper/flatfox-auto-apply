import imaplib
import email
import re
from bs4 import BeautifulSoup
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def is_link_processed(link):
    if os.path.exists("processed_links.txt"):
        with open("processed_links.txt", "r") as file:
            processed_links = file.read().splitlines()
        if link in processed_links:
            return True
    return False

# Function to mark a link as processed
def mark_link_processed(link):
    with open("processed_links.txt", "a") as file:
        file.write(link + "\n")

def process_email_and_submit_form():
    # Email credentials and IMAP server
    username = "moritz.lauper@hispeed.ch"
    password = "PASSWORD"  # Replace with your actual password
    imap_url = "imap.hispeed.ch"

    # Connect to the IMAP server and select the inbox
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)
    mail.select("inbox")

    # Search for the specific email
    status, messages = mail.search(None, 'FROM', '"Flatfox subscription"')

    # Fetch the latest email
    messages = messages[0].split()
    latest_email_id = messages[-1]
    res, msg = mail.fetch(latest_email_id, "(RFC822)")
    phrase = "One new listing matches your search:"
    found = False
    url = None

    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    # Find the phrase and subsequent link
                    if "One new listing matches your search:" in soup.get_text():
                        anchor = soup.find(string=re.compile("One new listing matches your search:")).find_next('a')
                        if anchor and anchor.has_attr('href'):
                            url = anchor['href']
                            print("Found URL:", url)

    # Close the connection
    mail.logout()
    

    if url and not is_link_processed(url):

        # Set up the Selenium WebDriver
        s = Service('./chromedriver')

        driver = webdriver.Chrome(service=s)

        # Open the URL extracted from the email
        driver.get(url)

        time.sleep(2)
        # Fill in the form fields
        driver.find_element(By.ID, "id_name").send_keys("Moritz Lauper")
        driver.find_element(By.ID, "id_email").send_keys("moritz.lauper@hispeed.ch")
        driver.find_element(By.ID, "id_phone_number").send_keys("0786756543")

        # Check or uncheck the 'Notify me of similar listings' checkbox
        checkbox = driver.find_element(By.ID, "id_create_subscription")
        if checkbox.is_selected():
            checkbox.click()  # Uncheck if already checked

        xpaths = [
            "/html/body/div[4]/div[4]/div/div[2]/form/div/div/button",
            "/html/body/div[4]/div[3]/div/div[2]/form/div/div/button",
            "/html/body/div[4]/div[3]/div/div[2]/form/div/div[1]/button"
        ]

        # Function to try clicking a button with different XPaths
        def click_button_with_xpaths(driver, xpaths):
            for xpath in xpaths:
                try:
                    wait = WebDriverWait(driver, 5)
                    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                    button.click()
                    print("Button clicked using XPath:", xpath)
                    return True  # Button was clicked successfully
                except NoSuchElementException:
                    pass  # Try the next XPath
                except Exception as e:
                    print("An error occurred:", e)
                    pass  # Try the next XPath

            print("Button not found with any of the provided XPaths")
            return False  # Button was not found

        # Attempt to click the button
        click_button_with_xpaths(driver, xpaths)

        time.sleep(2)

        # Wait for the next page to load and the email input to be present
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.ID, "id_email")))

        # Fill in the email address
        email_input.clear()  # Clear any pre-filled value
        email_input.send_keys("moritz.lauper@hispeed.ch")  # Replace with the actual email

        # Locate and click the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next']")
        submit_button.click()

        # Wait for the password field to be visible
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_password"))
        )

        # Fill in the password
        password_field.send_keys("Flatfox_2024")  # Replace with your password

        # Locate and click the Log In button
        log_in_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in']")
        log_in_button.click()

        time.sleep(10)

        # Connect to the IMAP server and select the inbox
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(username, password)
        mail.select("inbox")

        # Search for the specific email with the subject "Your Flatfox account: Access from a new device"
        status, messages = mail.search(None, '(SUBJECT "Your Flatfox account: Access from a new device")')

        # Fetch the latest email
        messages = messages[0].split()
        latest_email_id = messages[-1]
        res, msg = mail.fetch(latest_email_id, "(RFC822)")

        verification_code = None

        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            match = re.search(r'Your Flatfox login code is: (\d+)', body)
                            if match:
                                verification_code = match.group(1)
                                break
                else:
                    body = msg.get_payload(decode=True).decode()
                    match = re.search(r'Your Flatfox login code is: (\d+)', body)
                    if match:
                        verification_code = match.group(1)

        if verification_code:
            print("Verification code:", verification_code)
        else:
            print("No verification code found.")


        # Wait for the verification code input field to be visible
        wait = WebDriverWait(driver, 10)

        verification_input = wait.until(EC.visibility_of_element_located((By.ID, "f1")))

        # Fill in the verification code
        verification_input.send_keys(verification_code)

        # Locate and click the Next/Submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next']")
        submit_button.click()

        time.sleep(2)

        mark_link_processed(url)

        # Close the browser
        driver.quit()

while True:
    try:
        process_email_and_submit_form()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Wait for one minute before repeating
        time.sleep(60)
