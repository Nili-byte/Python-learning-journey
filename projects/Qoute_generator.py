import requests
import json


def getqoute():
    url = "https://zenquotes.io/api/random"

    reponse = requests.get(url)
    data = reponse.json()
    return data[0]["q"],data[0]["a"]

def save(Qoute , author):
    with open ("qoute.txt","a") as txt:
        txt.write(f"{Qoute}--->{author}")


def display(Qoute , author):
    print("-"*30)
    print(f"{Qoute}")
    print(f"{author}")
    print("-"*30)


a = getqoute()
print(a)







