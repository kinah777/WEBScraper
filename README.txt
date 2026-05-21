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