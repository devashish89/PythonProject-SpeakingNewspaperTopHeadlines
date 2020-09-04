def getTopNHeadlines(n):
    import requests
    import json

    url = "http://newsapi.org/v2/top-headlines?country=in"

    payload = {}
    headers = {
      'X-Api-Key': 'e5457f56dd674ec1a0087edafba9b107',
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    # print(response.text.encode('utf8'))

    num_articles=0
    py_dict = json.loads(response.text.encode('utf8'))

    if py_dict["totalResults"]>=n:
        num_articles = n
    else:
        num_articles = py_dict["totalResults"]

    lst = list()
    counter=1
    for article in py_dict["articles"]:
        lst.append((counter,article["title"]))
        counter+=1
        if(counter>num_articles):
            break

    return lst
