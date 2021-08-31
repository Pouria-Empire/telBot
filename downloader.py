#In the name of God
#challenge 1
from bs4 import BeautifulSoup
import requests
import wget
import re
def get_url(inputted):
    response = requests.get(inputted)
    response_text = response.text

    soup = BeautifulSoup(response_text,"html.parser")

    parsed_links = soup.find_all(name="li",class_="menu-item-link link")

    link = None
    for parse in parsed_links:
        if(str(parse).__contains__("720")):
            link = parse
    else:
        for parse in parsed_links:
            if(str(parse).__contains__("360")):
                link = parse
        else:
            link = parsed_links[0]

    pattern = "href=\"(.+)\" "
    parsed_link = re.findall(pattern, str(link))
    url_parsed = parsed_link[0]
    # https://aspb28.cdn.asset.aparat.com/aparat-video/43e7fe91c8620d3228129a5da875976435717954-360p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjFjM2U5MGVhYTAzZWRkNDQ3ZThhZmM2MWIyNDMwMzBmIiwiZXhwIjoxNjI5NTc2MTM5LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.DQZPl19b2nI5gCIIEi8VcFzszZ6_tAS_C1Je-98_kUk
    file_name = re.findall("/aparat-video/(.+).mp4", url_parsed)
    path = '/home/pouria/Desktop/test'

    def bar_custom(current, total, width=80):
        print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

    wget.download(url_parsed,bar=bar_custom,out=path)
    
    return path + "/" + file_name + ".mp4"
