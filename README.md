# SaavnToSpotify
### Export your 🎶 Playlists from JioSaavn to Spotify 🤩

Uses Selenium WebDriver and Spotipy Python3 Module

This python script uses **Firefox Driver** for Selenium Webdriver

### How to Get Started ?

**STEP 1**

Download the repository, and ensure that **selenium** and **spotipy** modules are installed, 

for selenium,
```
sudo apt-get install python-pip
sudo pip3 install selenium
```
for spotipy,
```
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
```

**STEP 2** 

Under the **User Credentials Section** in the Python Script (main.py), 

Enter the JioSaavn Username and Password

```
JIO_SAAVN_USERNAME = 'ENTER EMAIL'
JIO_SAAVN_PASSWORD = 'ENTER PASSWORD'
```
**Note - Please don't use playlist name merely as 'Playlist'. Be unique and fancy with your playlists name 😎**

**Use something unique like Playlist-1 or Playlist_Maroon5 etc. in JioSaavn for improved detection by Selenium Webdriver**

Enter the Name of Playlists that you want to export, 

```
all_playlist = ['Playlist-1', 'Enter Playlist Names like this'] 
# Playlist Names in the form of comma seperated list of strings
````

**STEP 3** 

After these changes are made, head to the parent repository where the script is saved, and run this in the terminal

```
python3 main.py [YOUR SPOTIFY ACCOUNT USERNAME]
```
To know how to find your Spotify Username head - [Here](https://community.spotify.com/t5/Accounts/how-do-i-find-my-spotify-user-id/td-p/665532)

**STEP 4**

After the script starts running, once the Selenium Driver window closes you will be asked to allow the application to give Rights to Use your Spotify Account, after you do this you will be redirected back to a page like **https://anudishjain.github.io/SaavnToSpotify/?code=[blablabla....]**

**Copy the redirected URL and paste it back into the Terminal and hit Enter** and **VOILA 🥳, you have your exported playlists, verify [here](https://open.spotify.com/collection/playlists)**


**STEP 5**

If you like this repository, give it a Star 🌟. New features, suggestions and contributions are always welcome 😀.
