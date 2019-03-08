from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
import sys
import spotipy
import spotipy.util as util

# ---------------------------------------------------------------------------------

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.jiosaavn.com/login.php?action=login')
login_element_field = driver.find_element_by_id('login_username')
password_element_field = driver.find_element_by_id('login_password')
login_submit_button = driver.find_element_by_id('static-login-btn')

# --------------------------- USER CREDENTIALS SECTION ----------------------------

## ENTER JIO_SAAVN USERNAME AND PASSWORD, CURRENTLY ONLY EMAIL LOGIN SUPPORTED
JIO_SAAVN_USERNAME = 'YOUR JIOSAAVN USERNAME, ENTER HERE'
JIO_SAAVN_PASSWORD = 'YOUR JIOSAAVN PASSWORD, ENTER HERE'

## ENTER NAMES OF THE PLAYLISTS THAT YOU WANT TO EXPORT, GIVE UNIQUE NAME TO YOUR PLAYLISTS
all_playlist = ['Example- Playlist_Maroon5', 'Enter JioSaavn Playlist Names Here'] 


# ----------------------------- JIOSAAVN SECTION BELOW -------------------------------

login_element_field.send_keys(JIO_SAAVN_USERNAME)
password_element_field.send_keys(JIO_SAAVN_PASSWORD)

login_submit_button.click();
driver.implicitly_wait(3)


song_names_inside_playlists = []
playlists_links = []

for playlist in all_playlist :

	selected_playlist = driver.find_element(By.XPATH, '//a[text()="' + str(playlist) + '"]')
	playlists_links.append(selected_playlist.get_attribute("href"))

	song_names_inside_playlists.append([])


index = 0

for linkOfPlaylist in playlists_links :

	driver.get(linkOfPlaylist)
	driver.implicitly_wait(3);

	song_name = driver.find_elements(By.XPATH,"//span[@class='main']/span[@class='title']")

	for name in song_name :
		song_names_inside_playlists[index].append(name.get_attribute('innerText'))

	index = index + 1

driver.close();


# ---------------------------- SPOTIFY SECTION BELOW --------------------------------

SPOTIFY_USERNAME = sys.argv[1]

# please don't misuse these client id and secret, I trust you with these...
# or generate your own from https://developer.spotify.com

try :
	token = util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope='playlist-modify-public', 
		client_id='841ebcf06a0c4564b8c966522fa447bc', client_secret='69ca8085fc5a40fda19b7a16c29b679b', 
		redirect_uri='https://anudishjain.github.io/SaavnToSpotify/')
except:
	os.remove(f".cache-{SPOTIFY_USERNAME}")
	token = util.prompt_for_user_token(SPOTIFY_USERNAME)


spotify = spotipy.Spotify(auth=token)

song_ids_according_to_playlists = [];
index = 0

for playlist in song_names_inside_playlists :

	song_ids_according_to_playlists.append([])

	for song_names in playlist :

		results = spotify.search(q=song_names, limit=1, offset=0, type='track', market=None)
		results = results["tracks"]["items"][0]["id"]
		song_ids_according_to_playlists[index].append(str(results))

	index = index + 1

print(song_ids_according_to_playlists)

# ------------------------------------------------------------------------------------

index = 0

for song_playlist_wise in song_ids_according_to_playlists :

	current_playlist_id = spotify.user_playlist_create(str(SPOTIFY_USERNAME), all_playlist[index], public=True, description='')
	current_playlist_id = str(current_playlist_id["id"])

	song_id = spotify.user_playlist_add_tracks(str(SPOTIFY_USERNAME), current_playlist_id, song_playlist_wise, None)

	index = index + 1






