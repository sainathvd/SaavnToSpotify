from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys
import json
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
JIO_SAAVN_USERNAME = 'ENTER USERNAME HERE'
JIO_SAAVN_PASSWORD = 'ENTER PASSWORD HERE'

## ENTER NAMES OF THE PLAYLISTS THAT YOU WANT TO EXPORT
all_playlist = ['Playlist-1', 'Playlist-2'] 


# ---------------------------------------------------------------------------------

login_element_field.send_keys(JIO_SAAVN_USERNAME)
password_element_field.send_keys(JIO_SAAVN_PASSWORD)

login_submit_button.click();
driver.implicitly_wait(5)


all_song_names = []
playlists_links = []

for playlist in all_playlist :

	selected_playlist = driver.find_element(By.XPATH, '//a[text()="' + str(playlist) + '"]')
	playlists_links.append(selected_playlist.get_attribute("href"))

for linkOfPlaylist in playlists_links :

	driver.get(linkOfPlaylist)
	driver.implicitly_wait(5);

	song_name = driver.find_elements(By.XPATH,"//span[@class='main']/span[@class='title']")

	for name in song_name :
		all_song_names.append(name.get_attribute('innerText'))

driver.close();

# --------------------------- USER CREDENTIALS SECTION ----------------------------

SPOTIFY_USERNAME = sys.argv[1]
SPOTIFY_PASSWORD = 'ENTER PASSWORD HERE'

# ---------------------------------------------------------------------------------

try :
	token = util.prompt_for_user_token(SPOTIFY_USERNAME)

except:
	print('ERROR ENCOUNTERED !!')

spotify = spotipy.Spotify(auth=token)

all_songs_id_on_spotify = [];

for song in all_song_names :

	results = spotify.search(q=song, limit=1, offset=0, type='track', market=None)
	print(results)

	song_id_dictionary = json.loads(str(results))
	all_songs_id_on_spotify.append(song_id_dictionary['uri'])

print(all_songs_id_on_spotify)



