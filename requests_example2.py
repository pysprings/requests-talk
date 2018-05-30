import requests

# Hello World
response = requests.get('http://example.com')

print(response.headers)
print(response.text)
print(response.encoding)

response = requests.get('http://httpbin.org/get')
print(response.json())

# Posting Data
response = requests.post('http://httpbin.org/post', json={'foo':'bar', 42:106})
print(response.json())

# Modifying Headers
response = requests.get('http://httpbin.org/get', headers={'user-agent': 'Mozilla/5.0'})
response.json()
