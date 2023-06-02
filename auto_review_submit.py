import requests
#Requestes are needed for HTTP GET/PUT/POST/DELETE/HEAD

#Function takes data necessary for posting a review and generates HTTP PUT based on it
def add_review(url, headers, data):
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    return response

#Main function puts data into HTTP Put. Here the review is for banana juice (id 6)
def main():
    url = 'http://localhost:3000/rest/products/6/reviews'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MiwidXNl>
    }
    data = {
        'message': 'KOMENTARZ PREZENTACYJNY BAW',
        'author': 'jim@juice-sh.op'
    }

    try:
        response = add_review(url, headers, data)

        if response.ok:
            print('Review Success')
        else:
            print('Review Fail', response.text)

    except requests.exceptions.HTTPError as e:
        print('HTTP error:', e)

    except requests.exceptions.RequestException as e:
        print('Request error:', e)

if __name__ == '__main__':
    main()


