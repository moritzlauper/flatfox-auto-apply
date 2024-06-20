### README.md

# Flatfox Auto Apply

This script automatically applies to apartment listings on Flatfox by processing emails from Flatfox subscription notifications, extracting the listing URL, and submitting a pre-filled form with your details.

## How It Works

1. Connects to your email account via IMAP and searches for emails from "Flatfox subscription".
2. Extracts the apartment listing URL from the latest email.
3. Uses Selenium to navigate to the listing URL and fill in the application form with predefined details.
4. Logs in to your Flatfox account if required, using credentials provided in the script.
5. Extracts and uses the verification code from the email if two-factor authentication is needed.

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/flatfox_auto_apply.git
    cd flatfox_auto_apply
    ```

2. **Update Email Credentials**:
    Open `flatfox_auto_apply.py` and update the following variables with your email credentials and IMAP server details:
    ```python
    # Email credentials and IMAP server
    username = "youremail@address.com"
    password = "PASSWORD"
    imap_url = "imap.mailprovider.com"
    ```

3. **Update Flatfox Login Details**:
    In the same file, update the Flatfox login details:
    ```python
    # Replace these with your actual Flatfox login details
    driver.find_element(By.ID, "id_name").send_keys("Your Name")
    driver.find_element(By.ID, "id_email").send_keys("youremail@address.com")
    driver.find_element(By.ID, "id_phone_number").send_keys("Your Phone Number")
    email_input.send_keys("youremail@address.com")  # Your Flatfox email
    password_field.send_keys("PASSWORD")  # Your Flatfox password
    ```

4. **Install Dependencies**:
    Install the required Python packages using `pip`:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Script**:
    Execute the script using Python:
    ```sh
    python3 flatfox_auto_apply.py
    ```

6. **Automate** (Optional):
    Automate the script using Google Cloud or another cloud service if desired.

## Troubleshooting

- **ChromeDriver Issues**:
  If the included ChromeDriver doesn't work, it might be outdated. Download the newest one [here](https://googlechromelabs.github.io/chrome-for-testing/) and replace the existing ChromeDriver in the project.

## Notes

- The ChromeDriver executable is already included in the GitHub project. The script is configured to use this local ChromeDriver.
- The script runs in headless mode by default, meaning it won't open a visible browser window. You can change this by modifying the Chrome options in the script.

## Contributing

Feel free to open issues or submit pull requests with improvements and fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Summary of the Script

- **Email Processing**:
  - Connects to the IMAP server using provided credentials.
  - Searches for emails from "Flatfox subscription".
  - Extracts the listing URL from the latest email.

- **Form Submission**:
  - Uses Selenium to open the listing URL.
  - Fills in the form fields with your name, email, and phone number.
  - Unchecks the 'Notify me of similar listings' checkbox if checked.
  - Attempts to click the 'Apply now' button using different XPaths.
  - Logs in to your Flatfox account if required.
  - Extracts the verification code from the email if two-factor authentication is needed.
  - Submits the application form.

- **Loop**:
  - The script runs in an infinite loop, checking for new emails and applying to listings every minute.

This `README.md` should provide clear instructions on setting up and running the script, as well as the necessary points to update with personal credentials and details.
