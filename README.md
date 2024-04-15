# CharityNYC Data Scraping and S3 Upload

This project scrapes data from the New York State Charities Registry website using Selenium, organizes the scraped data into a DataFrame using Pandas, and uploads the data to an AWS S3 bucket.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.x
- Selenium
- Pandas
- AWS CLI
- Webdriver Manager

You can install the required Python packages using pip:


## Setup

1. Clone this repository to your local machine:

`git clone https://github.com/your-username/your-repository.git`

2. Navigate to the project directory:


3. Ensure you have configured your AWS CLI with the necessary credentials:


4. Run the Python script to scrape the data and upload it to S3:


## Files

- `scrape_and_upload.py`: Python script to scrape data from the CharityNYC website and upload it to S3.
- `README.md`: This file, providing an overview of the project and setup instructions.

## License

This project is licensed under the [MIT License](LICENSE).
