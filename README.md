# Reddit Avatar (NFT) Shop Monitor
This python script monitors the avatar shop on reddit (https://www.reddit.com/avatar/shop/gallery) and sends a sound notification when new avatars are added.
This is helpful because the previous Reddit Avatar releases have all been stealth drops (at random times) so this script gives an edge for users to be instantly notified when the website changes.
The script mainly utilizies the `requests` and `beautifulsoup4` ibraries.

# Installation
To install the required libraries, run the following command in a terminal or command prompt:
```
pip install requests beautifulsoup4 hashlib playsound
```
# Usage
To run the script, open a terminal or command prompt and navigate to the directory containing the script. Then, run the following command:
```
python script.py
```
The script will run indefinitely, monitoring the avatar shop and playing a notification sound when new avatars are added. You can stop the script at any time by pressing Ctrl+C.

# Configuration
By default, the script refreshes the avatar shop every 2 seconds. You can adjust the refresh interval by changing the value of the "time.sleep()" function in the "monitor_avatar_shop()" function.

The script plays a sound file named "notification.wav" when new avatars are added. You can replace this file with your own sound file or modify the script to play a different sound file by changing the argument of the "playsound()" function in the "monitor_avatar_shop()" function.
