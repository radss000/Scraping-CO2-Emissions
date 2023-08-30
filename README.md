# Scraping-CO2-Emissions

Technical Documentation: CO2 Emission Data Scraping Script

Overview
This document provides an in-depth explanation of the Python script used for scraping CO2 emission data from a specific webpage. The script uses the Selenium library to automate web browsing and data extraction. The extracted data is then saved into a CSV file. The script's behavior, structure, data extraction process, and scheduling are described in detail below.

Script Description
The script is designed to scrape CO2 emission data from a webpage containing tabular information. It automates web browsing through the Firefox browser using the Selenium library. The extracted data is saved to a CSV file for further analysis.

Script Components
Imports: The script imports required libraries, including csv, os, time, schedule, and webdriver from Selenium.

extract_tbl() Function: This function performs the data extraction process. It opens the Firefox browser and navigates to the provided URL. An implicit wait ensures the page loads completely.

Data Extraction Loop: Inside the loop, the script finds the table with the ID "facetview_results" and iterates through rows and cells. It extracts data from each cell, appending it to the all_records list. If a row is empty, the script clicks the "next" button to load more records.

write_csv() Function: This function writes the extracted data to a CSV file. It defines headers and specifies the file path. It appends data to an existing file or creates a new file as needed.

Script Execution: The extract_tbl() function is called to start data extraction. The script schedules this function to run every 15 days using the schedule library. An infinite loop ensures scheduled tasks are executed, with a 1-second interval between executions.

Data Collection Details
Each page contains 10 records.
The script sets tot_records to 120, indicating a desire to extract 120 records. The script keeps scraping until it reaches this limit.
The data extracted includes various attributes related to CO2 emissions, such as pool, manufacturer name, version, make, commercial name, specific CO2 emissions, wheelbase, axle width, fuel type, fuel mode, engine capacity, engine power, electric energy consumption, electric range, and fuel consumption.

Web Scraping API for CO2 Emission Data Extraction:

Usage
Start the API
Open a terminal and navigate to the directory containing the script.

Run the following command to start the API:
python script_name.py
The API will run on http://localhost:5000 by default.

API Endpoints
POST /extract
Description: Initiates the data extraction process.
Payload: JSON object with tot_records (total records to extract) and frequency (frequency in days) fields.

Example Request:
sh
curl -X POST -H "Content-Type: application/json" -d '{"tot_records": 120, "frequency": 15}' http://localhost:5000/extract
Response: JSON response with a success message or error details.

Components
extract_tbl(): Function in p1.
Extracted data is stored in a list all_records.
The CSV file path is specified in the file_path variable.
start_extraction(): Flask route function to start data extraction based on provided parameters.
It retrieves JSON data from the request, including tot_records and frequency.
It runs the extract_tbl() function in a loop with the specified frequency.
The extracted data is written to a CSV file using write_csv().

Conclusion
This API allows you to automate the process of extracting CO2 emission data from a web source and store it in a CSV file. By scheduling the extraction process at a specified frequency, you can keep your data up-to-date without manual intervention.





Here’s an example result in a csv: 




Description of the page & filters present: The page includes filters such as "Status" (with options: Final, Provisional), "Registration year" (ranging from 2013 to 2022), "Country," "Pool," "Manufacturer name," "Commercial name," "Mass in running order (kg)," and "Specific CO2 Emissions in g/km (WLTP)." These filters allow users to refine their data search based on specific criteria.

Registration year: The term "registration year" on the car website generally refers to the year when a vehicle was first registered and legally allowed to be operated on the road. It is not necessarily the same as the year of manufacture. The registration year is typically indicated on the vehicle registration documents and serves as an official record of when the vehicle became roadworthy.

Calculus for storage: 

Total Number of Records: 66,731,364
Frequency: 96 times per year
Records per Execution: 695,118
Storage per Execution: 145,608 KB

To scrape all the records from 2017 to 2022) there are nearly 66731364  records. 
Lets set the frequency at 2 times a week, so 8 times a month & 96 times per year.
You need to scrape 695118 records.
Knowing that for 635519 records scraped we have 133124 ko of space used.
For 695118 we will need 145608 ko for every time the script will be executed.
So for complete scraping of the records registrated from 2017 to 2022, we will need 13878404 ko (=13,878404 go)

Solutions for storage & pricing: 

Amazon S3 is a widely used object storage service with high availability and scalability. Pricing varies depending on factors like storage amount, data transfer, and request rates. The costis around $0.023 per GB per month for standard storage in the US-East region.

Google Cloud Storage: Costs can vary depending on storage class, location, and access frequency. standard storage is around $0.020 per GB per month in the US.

Microsoft Azure Blob Storage: The pricing can differ based on storage tier, access frequency, and data transfer. General-purpose v2 storage in the US is around $0.0184 per GB per month.

Mechanism for not scraping the same element twice: The script ensures that the same element is not written twice in the final CSV file through the following steps:

Duplicate ID Handling Mechanism:

Loading the Last Processed ID:

The script utilizes the load_last_id function to retrieve the last processed ID from the JSON file (last_id.json).
If the file exists, the stored last processed ID is read. If the file doesn't exist, a default value of 0 is used.
Handling Duplicate IDs:

As the script iterates through rows on the web page, it extracts the record's ID from the first cell of each row.
It then compares the extracted ID with the last processed ID to determine if the record has already been processed.
If the extracted ID is greater than the last processed ID, the script adds the record's data to the all_records list and updates the last_processed_id variable to the new ID.
This ensures that only new records (with IDs higher than the last processed ID) are considered.
Saving the Last Processed ID:

After processing all the records, the script utilizes the save_last_id function to save the maximum ID from the processed set as the last processed ID.
This step ensures that subsequent runs of the script will begin processing from the point where the last run left off, effectively skipping already processed records.
Writing to CSV:

Once all records have been processed and stored in the all_records list, the script writes this data to a CSV file using the write_csv function



Writing to CSV:

Once all the necessary records are collected in the list, the script writes this data to a CSV file. It creates the CSV file if it does not exist or appends to it if it already exists. The header row and the data rows are written using the CSV writer.

What’s remaining (Jay) ? =>  This is a base mechanism that need further ameliorations by making sure it works as expected with the programmation of frequency of the scraping (2 times a week) with Linux & implementation of error handling that can happen during the scraping process


To planify the frequency to run the script, use Linux.





