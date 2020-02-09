import requests

def location_info():
    return requests.get("http://ip-api.com/json/").json()

if __name__=="__main__":
    print(location_info())

d = location_info()
print()
print("IP:", d.get('query'), d.get('country'))
