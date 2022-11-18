from requests import post

response = post('http://localhost:8080/links', json=[
    'https://www.formula1.com/en/results.html/2022/races.html',
    'https://www.formula1.com/en/results.html/2022/races/1125/saudi-arabia/race-result.html'
    ])

print(response.status_code)
print(response.json())