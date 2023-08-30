import csv
import os
import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By


def extract_tbl():
    print("extracting data from facetview_results")
    driver = webdriver.Firefox()
    driver.get(
        " http://co2cars.apps.eea.europa.eu/?source=%7B%22track_total_hits%22%3Atrue%2C%22query%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22constant_score%22%3A%7B%22filter%22%3A%7B%22bool%22%3A%7B%22must%22%3A%5B%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22year%22%3A2022%7D%7D%5D%7D%7D%2C%7B%22bool%22%3A%7B%22should%22%3A%5B%7B%22term%22%3A%7B%22scStatus%22%3A%22Provisional%22%7D%7D%5D%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22display_type%22%3A%22tabular%22%7D")
    driver.implicitly_wait(10)

    all_records = []
    tot_records = 20  # records you want to extract (10000)
    current_records = 0

    while current_records < tot_records:
        table = driver.find_element(By.ID, 'facetview_results')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text for cell in cells]
            if len(row_data) == 0:
                element = driver.find_element(By.CLASS_NAME, "facetview_increment")
                driver.execute_script("arguments[0].click();", element)
                current_records = current_records + 10
                print("processed records: " + str(current_records))
                print("next button clicked")
            else:
                print(row_data)
                all_records.append(row_data)

        time.sleep(5)
    write_csv(all_records)
    print("process completed successfully")


def write_csv(all_records):
    print("started creating csv")
    headers = ['Pool', 'Manufacturer name (OEM ...', 'Version', 'Make', 'Commercial name', 'Specific CO2 E...',
               'Specific CO2 E...',
               'Wheel base...', 'Axle width...', 'Axle width...', 'Fuel type', 'Fuel mode', 'Engine capacity...',
               'Engine power...',
               'Electric energy consumption...', 'Electric range...', 'Fuel consumption']

    file_path = "C:\\Users\\radia\\OneDrive\\Bureau\\outputco2.csv"  # CSV path

    #os.remove(file_path) # Remove if file exists
    file_exists = os.path.exists(file_path)
    mode = 'a' if file_exists else 'w'
    with open(file_path, mode=mode, newline='') as file:
        writer = csv.writer(file)
        # write the header row
        writer.writerow(headers)

        # Write the rest of the data rows
        for row in all_records:
            writer.writerow(
                [row[3], row[5], row[10], row[11], row[12], row[18], row[19], row[20], row[21], row[22], row[23]
                    , row[24], row[25], row[26], row[27], row[28], row[35]])

        print("CSV file has been created successfully!")


extract_tbl()
#schedule.every(15).days.do(extract_tbl)

#while True:
  #  schedule.run_pending()
  #  time.sleep(1
