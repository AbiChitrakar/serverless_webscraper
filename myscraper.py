import requests
from bs4 import BeautifulSoup
import json

def scrape_website():
    url = 'https://www.gadgetbytenepal.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []
    items = soup.find_all('div', class_='td-module-thumb')

    # Loop through and get only the first 7 items
    for idx, item in enumerate(items[:7]):  # Limit to the first 7 items
        link_tag = item.find('a', href=True)
        title = link_tag['title']
        link = link_tag['href']
        img_tag = item.find('img', class_='entry-thumb')
        image_url = img_tag['src']

        data.append({
            'title': title,
            'link_to_the_page': link,
            'image_url': image_url
        })

    return data

if __name__ == "__main__":
    scraped_data = scrape_website()
    print(json.dumps(scraped_data, indent=2))
