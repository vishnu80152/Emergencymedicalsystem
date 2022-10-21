import requests

res = requests.get('https://ipinfo.io')
data = res.json()


loc = data['loc']

print(loc)
x=open('cord.txt','w')
x.truncate()
x.write(loc)
x.close()
print("process executed")
