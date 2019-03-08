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

**Use something unique like Playlist_1 or Playlist_Maroon5 etc. in JioSaavn for improved detection by Selenium Webdriver**

Enter the Name of Playlists that you want to export, 

```
all_playlist = ['Playlist-1', 'Playlist-2', 'Playlist-3', 'Enter Playlist Names like this'] 
# Playlist Names in the form of comma seperated list of strings
````

**STEP 3** 

After these changes are made, head to the parent repository where the script is saved, and run this in the terminal

```
python3 main.py [YOUR SPOTIFY ACCOUNT USERNAME]
```
To know how to find your Spotify Username head - [Here](https://community.spotify.com/t5/Accounts/how-do-i-find-my-spotify-user-id/td-p/665532)


**STEP 4**

If you like this repository, give it a Star 🌟. New features, suggestions and contributions are always welcomed 😀.
