import requests
response = requests.get('http://example.com')
response
response.ok
response.status_code
response.headers
print response.headers
response.text
response.content
response.headers['content-type']
dir(response)
response.links
response.reason
resp = requests.get('http://httpbin.org/get')
resp.text
resp.headers['content-type']
resp.json()
