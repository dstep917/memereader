import requests
import requests.auth


f = open("links.txt","w")

base = "https://oauth.reddit.com/"
heads = {'User-Agent': 'MyAsspp'}
client_auth = requests.auth.HTTPBasicAuth('_78B_s-gBLEX3w', 'k5PkuDHiO_XaquAJnlcXK32VIIs')
post_data = {"grant_type": "password", "username": "its4thecatlol", "password": "XXX"}

r = requests.post("https://www.reddit.com/api/v1/access_token", auth = client_auth, data = post_data, headers = heads)

token = r.json()['access_token']

heads["Authorization"] = "bearer " + token

##r = requests.get("https://oauth.reddit.com/api/v1/me", headers=heads)
r.json()

r = requests.get(base + "r/adviceanimals/hot?limit=10&g=US", headers = heads)

memes = r.json()['data']['children']

memes_list = []

for i in range(2,len(memes)):
    memes_list.append(memes[i]['data']['url'])

for i in memes_list:
    f.write(i + "\n")

f.close()
