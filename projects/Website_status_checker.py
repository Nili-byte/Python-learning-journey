import requests


usr = input("Enter yur urls separted by commas) : ")


cleanrul = [url.strip() for url in usr.split(",")]



requirment = []
for url in  cleanrul:
    if not url.startswith("https"):
        url = ("https://")+url
    
    requirment.append(url)


for url in requirment:
    try:
        reponse = requests.get(url , timeout=3)
        if reponse.status_code == 200:
            print(f"Working Fine {url} --> {reponse.elapsed.total_seconds()}")

        else:
            print(f"Something wrong {url} --> {reponse.elapsed.total_seconds()}")



    except:
            requests.RequestException
            print(f"ERROR --> {url}")



        










   



