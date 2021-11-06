import requests
from bs4 import BeautifulSoup as bs

def wownero():
    try:
        r = requests.get("https://suchwow.xyz/").text
        soup = bs(r,"lxml")
        
        latest_meme_img_url = soup.find('img', alt="Placeholder image")['src']
        URL = "https://suchwow.xyz" + latest_meme_img_url.replace(".thumbnail", "")
        latest_meme_img_name = soup.find("p",class_="title is-4").text.replace("\n","")
        latest_meme_img_date = soup.find("time", datetime="2016-1-1").text
        latest_meme_img_tips = soup.find(class_="content").find('strong').text
        data = {}
        data['url'] = URL #Can be used as public group also
        data['name'] = latest_meme_img_name
        data['date'] = latest_meme_img_date
        data['tips'] = latest_meme_img_tips
        print(data)
        return data
    except Exception as e:
        print("Error")
        return {"status":False,"error":e}
        
        
wownero()