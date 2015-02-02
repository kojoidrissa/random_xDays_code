import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:5]:
    view_count = int(video['yt$statistics']['viewCount']) #converts viewCount into an int
    print(video['title']['$t'], "with", '{:,}'.format(view_count), "views") #second 1/2 formats the int with thousands separators



'''print()
print("NEW CODE STARTS HERE!!!")
print('''This is showing me the results from the "data = response.json"; the type and length of each
    element in "data['feed']['entry']" ''')
#this shows me the various data catagories stored in each YouTube Entry listing
f = open("youTube_data.txt", "a")

for i in data['feed']['entry']:
    # for key in i:
    #     print (key, )
    # print (i['yt$statistics']['viewCount'])
    f.write(str(type(i)) + " " + str(len(i)) + " " + i['title']['$t'] + "\n" + str(i) + "\n" + "\n")
    print (len(i), i['title']['$t'])
#Looks like I'm after ['title']['$t'] and ['yt$statistics']
'''
f.close()