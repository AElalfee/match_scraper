
# Matches Scraper

A web scraper designed to extract football match details from the Yallakora website based on a user-defined date. The extracted data is then stored in a CSV file for easy access and analysis. This tool is particularly useful for football enthusiasts, analysts, and developers who need to gather match information efficiently.

## Features

- **Date-based Scraping**: Users can specify a date to fetch the football match details.
- **Comprehensive Data Extraction**: Extracts various details such as match date, time, teams, and scores.
- **CSV Storage**: Saves the scraped data into a well-structured CSV file for further use.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AElalfee/match_scraper.git
   ```

   ```bash
   cd match_scraper
    ```

2. Install the required Python libraries:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Run the scraper script:

    ```bash
    python3 main.py
    ```

2. Write the desired date:

    ```bash
    Please enter the date in the format of (MM/DD/YYYY):
    19/05/2025
    ```

3. Write the filename to save the data in:

    ```bash
    Please enter the name of the file you want to save the data in ['filename.csv']:
    matches.csv
    ```

4. Look for the csv file in the directory.

## Notes

- Ensure that the Yallakora website's structure has not changed, as this may affect the scraper's ability to extract data.