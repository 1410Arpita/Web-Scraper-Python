
### scrape.py (Python Web Scraping Script)

```python
import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract specific information (example: extract all links)
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
