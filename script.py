import requests
from bs4 import BeautifulSoup
import time
import hashlib
from playsound import playsound

url = 'https://www.reddit.com/avatar/shop/gallery'

def get_avatars():
    headers = {'User-Agent': 'Reddit Avatar Shop Monitor'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    avatars = []
    for item in soup.find_all('div', class_='_imageWrapper_1trdi_61'):
        img = item.find('img', class_='_outfitImage_1trdi_30')
        if img:
            avatars.append(img['src'])
    
    return avatars

def monitor_avatar_shop():
    avatars_hash = hashlib.sha256()
    new_avatars_hash = hashlib.sha256()
    
    avatars = get_avatars()
    for avatar in avatars:
        avatars_hash.update(avatar.encode())

    while True:
        time.sleep(2)  # Refresh every 3 seconds
        new_avatars = get_avatars()

        for avatar in new_avatars:
            new_avatars_hash.update(avatar.encode())

        if avatars_hash.digest() != new_avatars_hash.digest():
            print("Avatar shop updated!")
            playsound('notification.wav')
            new_avatars = list(set(new_avatars) - set(avatars))
            for new_avatar in new_avatars:
                print(f"New avatar added: {new_avatar}")

            avatars = new_avatars
            avatars_hash = new_avatars_hash
            new_avatars_hash = hashlib.sha256()
        else:
            print("Avatar shop not updated.")
            
    
if __name__ == '__main__':
    monitor_avatar_shop()