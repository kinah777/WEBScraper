# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import html
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, unquote, urlparse

BRAVE_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Brave/1.90.124'
)

HEADERS = {
    'User-Agent': BRAVE_USER_AGENT
}


def extract_redirect_target(url):
    parsed = urlparse(url)
    if parsed.netloc.endswith('facebook.com') and parsed.path == '/l.php':
        query = parse_qs(parsed.query)
        if 'u' in query:
            return unquote(query['u'][0])
    return None


def fetch_html(url, session=None, max_redirects=5):
    session = session or requests.Session()
    direct_target = extract_redirect_target(url)
    if direct_target and direct_target != url:
        url = direct_target

    for _ in range(max_redirects):
        response = session.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        redirect_script = soup.find('script', string=re.compile(r'document\.location\.replace|window\.location\.href|location\.replace'))
        if redirect_script and redirect_script.string:
            match = re.search(r'["\'](https?://[^"\']+)["\']', redirect_script.string)
            if match:
                url = html.unescape(match.group(1))
                continue

        return soup, response

    raise RuntimeError('Too many redirects while resolving URL')


def scrape():
    url = (
        'https://l.facebook.com/l.php?u=https%3A%2F%2Fstarlink.com%2Faccount%2Fservice-line%2FAST-2293597-46342-54%3F'
        'selectedDevice%3Dut01000000-00000000-0060d786%26page%3D0%26limit%3D5%26fbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExQ3ZtRFMxZ3VMeENkdmtwQ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR76Uh3e4C-cNmoCQ2oZxxAj9qdIiRCIsuZg_ZABlT1S-eovJNmlxAAuiLoA0A_aem_YWdncwCjOHup56qgx0veSiTN-Bsh%26brid%3DYWdncwGWfb0jThlfAln8tzQv4WsD&h=AUCZ8qv32qec0hTmElncvA3VOsLJX7_u9nwc5sLmEyIIS3NwxJRHlYqYJ3ZlihcCEspFtAVUNNMAab4yQiHvWMeSFbxVOp0V3PBtq_qVsvjAA_Bx3VoDQaBvhebhcc-ETps4gg'
    )

    soup, response = fetch_html(url)
    print(f'Fetched URL: {response.url} (status {response.status_code})')

    title_element = soup.select_one('h1')
    paragraph_element = soup.select_one('p')
    link_element = soup.select_one('a[href]')

    if title_element:
        print('Title:', title_element.get_text(strip=True))
    else:
        print('Title: not found')

    if paragraph_element:
        print('Text:', paragraph_element.get_text(strip=True))
    else:
        print('Text: not found')

    if link_element:
        print('Link:', link_element.get('href'))
    else:
        print('Link: not found')


if __name__ == '__main__':
    scrape()
