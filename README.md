# Flatfox Auto Apply

This script automatically applies to apartment listings on Flatfox.

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/flatfox_auto_apply.git
    cd flatfox_auto_apply
    ```

2. **Update Email Credentials**:
    Open `flatfox_auto_apply.py` and update the following variables with your Flatfox credentials and application details:
    ```python
    username = "your_username"
    password = "your_password"
    apartment_url = "https://flatfox.ch/en/listing/apartment-id/"
    application_message = "Hello, I am very interested in this apartment. Please consider my application. Thank you!"
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
