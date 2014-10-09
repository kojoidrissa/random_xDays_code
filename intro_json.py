print(str.upper("Nine lines of code with stock Python 3"))
import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:5]:
    print(video['title']['$t'])

print()
print("Six lines of code with additional 'requests' library")
#shorter version, using request external library
import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])