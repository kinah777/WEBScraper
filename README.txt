## Bolante's Starlink Data Usage Scraper HEHEHEHEH

This project extracts daily internet usage data from Sir Val's Starlink account and exports it into a clean CSV file.

Instead of parsing the webpage directly, it uses Starlink’s internal API to retrieve structured JSON data, making the process more accurate and reliable.

---

##  What This Project Does

- Connects to your Starlink account using an authenticated session cookie
- Sends a request to Starlink’s internal usage API
- Retrieves billing cycle data (daily internet usage in GB)
- Filters data by selected month
- Exports results into a CSV file

---

##  How It Works

1. The script calls the Starlink API endpoint:
- Grabs the billing cycle which is actually also the daily internet usage in GB

2. The API returns structured JSON containing:
- Start dates
- Daily usage values

3. The script processes the data by:
- Converting start dates into the needed calendar dates
- Mapping daily usage values to each day
- Filtering by the selected month, starts at the beginning of the month.

4. Finally, it saves the output as a CSV file.
- TA-DAAAAA

---

## Step by Step
1. First what I did was copy the annotated cURL from inspecting the webpage
- Used Chrome DevTools/Network tab/found the Annotated window/“Copy as cURL” to capture the exact request the browser sends to Starlink, including the URL, cookies, and headers.

2. We used the cURL data to recreate the request in Python using "curlconverter.com" and also the requests library, including authentication cookies yum-yumm.

3. The Python script is calling out Starlink’s internal API endpoint that returns usage data in JSON format to parse it.

4. Parsed and Extracted JSON format: Billing cycles, Start dates, Daily usage values, then mapped each usage value to the correct date.

5. Exported them to CSV as output - TA-DA 
