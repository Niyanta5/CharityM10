import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome webdriver
s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)

# Enter the URL
browser.get("https://www.charitiesnys.com/RegistrySearch/search_charities.jsp")

# Identify the EIN input element and send keys
ein_input = browser.find_element(
    By.XPATH,
    '//*[@id="header"]/div[2]/div/table/tbody/tr/td[2]/div/div/font/font/font/font/font/font/table/tbody/tr[4]/td/form/table/tbody/tr[2]/td[2]/input[1]',
)
ein_input.send_keys("0")

# Click the search button
search_button = browser.find_element(
    By.XPATH,
    '//*[@id="header"]/div[2]/div/table/tbody/tr/td[2]/div/div/font/font/font/font/font/font/table/tbody/tr[4]/td/form/table/tbody/tr[10]/td/input[1]',
)
search_button.click()

# Allow time for the page to load
time.sleep(4)

# Identify the table to scrape
table = browser.find_element(By.CSS_SELECTOR, "table.Bordered")

# Create an empty list to store data
data = []

# Loop through each row in the table

for i in range(1, 6):
    page = browser.find_element(
        By.XPATH,
        "/html/body/div[2]/div/table/tbody/tr/td[3]/div/div/span[2]/a[" + str(i) + "]",
    )

    for row in table.find_elements(By.CSS_SELECTOR, "tr"):
        cols = [cell.text for cell in row.find_elements(By.CSS_SELECTOR, "td")]
        data.append(cols)

# Update column names
column_names = [
    "Organization Name",
    "NY Reg #",
    "EIN",
    "Registrant Type",
    "City",
    "State",
]

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)
# converting data frame to csv and saving it locally
df.to_csv("charities_data.csv", index=False)
