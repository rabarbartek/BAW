#!/bin/bash

# to execute the script, cookie and authorization values need to be provided as an arguments
# example: accessing_paths.sh "language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss; continueCode=84uvtJUxHbh5TqFLiKbueziaEf3ZHa6tWYcR5Sz9UB1ix7SEvUgmhN5tmmIDPh2WCBDIWVH6W" "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTAsInVzZXJuYW1lIjoid3Vyc3Ricm90IiwiZW1haWwiOiJ3dXJzdGJyb3RAanVpY2Utc2gub3AiLCJwYXNzd29yZCI6IjlhZDViMDQ5MmJiZTUyODU4M2UxMjhkMmE4OTQxZGU0Iiwicm9sZSI6ImFkbWluIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IiIsInByb2ZpbGVJbWFnZSI6ImFzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdEFkbWluLnBuZyIsInRvdHBTZWNyZXQiOiJJRlRYRTNTUE9FWVZVUlQyTVJZR0k1MlRLSjRIQzNLSCIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIzLTA1LTE1VDIwOjA0OjQwLjc0MVoiLCJ1cGRhdGVkQXQiOiIyMDIzLTA1LTE1VDIwOjA0OjQwLjc0MVoiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2ODYwMDQ1MTIsImV4cCI6MTY4NjAyMjUxMn0.OmBSS1Ac7meaa9T05HAshjVnnVBwEpgeVZcgfBf5z6UyDbcen8gA2X8vLLXhd_h6oKW6hw0f-MoPMTQQ4JpjbGWsI9as6itGKhBUqguNf9B-RkYSKyzTxb-vHzETv95wO2Cy44l9HEBqfubg1QrzntDsQKYuwrTgzM5NIFI9_lQ"

base_url='http://localhost:3000'
cookie_value=$1 # first script argument - Cookie header value
authorization_value=$2 # second script argument - JWT value (Authorization header)

# defining URLs table
urls=(
    '/#/score-board' # Score Board
    '/#/privacy-security/privacy-policy' # Privacy Policy
    '/ftp/acquisitions.md' # Condifential Document
    '/metrics' # Exposed Metrics
    '/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm' # Outdated Allowlist
    '/.well-known/security.txt' # Security Policy
)

# loop sending requests
for url in "${urls[@]}"; do
    full_url="$base_url$url"
    echo "Response from $full_url:"
    curl -s -k -X GET -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' \
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Accept-Encoding: gzip, deflate' \
        -H "Authorization: $authorization_value" \
        -H "Connection: close" \
        -H "Cookie: $cookie_value" \
        -H 'Upgrade-Insecure-Requests: 1' \
        -H 'Sec-Fetch-Dest: document' \
        -H 'Sec-Fetch-Mode: navigate' \
        -H 'Sec-Fetch-Site: none' \
        -H 'Sec-Fetch-User: ?1' \
        "$full_url"
    echo
done