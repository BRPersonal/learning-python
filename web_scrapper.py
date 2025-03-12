import requests
from bs4 import BeautifulSoup


def scrape_t20i_runs(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing the player stats
        table = soup.find('table', class_='table cb-col-100 cb-plyr-thead')

        if table:
            # Find all rows in the table
            rows = table.find_all('tr')

            # Look for the T20I row
            for row in rows:
                cols = row.find_all('td')
                if cols and cols[0].text.strip() == 'T20':
                    # The runs are in the fourth column (index 3)
                    t20i_runs = cols[3].text.strip()
                    return t20i_runs

        print("Couldn't find T20I stats in the table.")
        return None
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


# URL of Virat Kohli's profile
url = "https://www.cricbuzz.com/profiles/1413/virat-kohli"

# Scrape T20I runs
t20i_runs = scrape_t20i_runs(url)

if t20i_runs:
    print(f"Virat Kohli's T20I overall runs: {t20i_runs}")
else:
    print("Failed to scrape T20I runs.")