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

2. **Update User-specific Information**:
    Open `flatfox_auto_apply.py` and update the following variables at the top of the file:
    ```python
    # User-specific information
    FLATFOX_EMAIL = "youremail@address.com"
    EMAIL_PASSWORD = "PASSWORD"  
    IMAP_URL = "imap.mailprovider.com"
    FLATFOX_PASSWORD = "FLATFOX_PASSWORD"
    PHONE_NUMBER = "0786756543"
    FULL_NAME = "Your name"
    ```

3. **Install Dependencies**:
    Install the required Python packages using `pip`:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Script**:
    Execute the script using Python:
    ```sh
    python3 flatfox_auto_apply.py
    ```

5. **Automate** (Optional):
    Automate the script using Google Cloud or another cloud service if desired.

## Troubleshooting

- **ChromeDriver Issues**:
  If the included ChromeDriver doesn't work, it might be outdated. Download the newest one [here](https://googlechromelabs.github.io/chrome-for-testing/) and replace the existing ChromeDriver in the project.

## Notes

- The ChromeDriver executable is already included in the GitHub project. The script is configured to use this local ChromeDriver.
- The script runs in headless mode by default, meaning it won't open a visible browser window. You can change this by modifying the Chrome options in the script.

## Contributing

Feel free to open issues or submit pull requests with improvements and fixes.
