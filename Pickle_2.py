import pickle
import requests
import json

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=b90ad3248c7f4d9cbd8991c9131950b3").text

data_dict = json.loads(data)        #It will parse 
art = data_dict['articles']         #It will fetch the aricles key value 

# with open ("Topheadlines.pkl","wb")as w:
#     i=1
#     for article in art:
#         inputt = f"{i} {article['title']}"        #It will fetch the aricles dict having the title dict
#         pickle.dump(inputt,w)
#         i+=1
with open ("Topheadlines.pkl","rb") as r:
    for line in "Topheadlines.txt":
    # for i in range(1,21): 
        print(pickle.load(r))
