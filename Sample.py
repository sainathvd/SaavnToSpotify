from selenium import webdriver
import os
import sys
import spotipy
import spotipy.util as util

driver = webdriver.Firefox()
# Add the URL of a public playlist. This change has been done to avoid exposing credentials to the script.
driver.get("https://www.jiosaavn.com/s/playlist/032b3a04e8d31d8fa5534b6ee2319775/Sainath/"
           "SFHfC8PSBlEGSw2I1RxdhQ__?referrer=svn_source%3Dshare&svn_medium=com.whatsapp&utm_source=share&utm_"
           "medium=com.whatsapp")
driver.maximize_window()

song_names_inside_playlist = list()
# index = 0
song_name = driver.find_elements_by_xpath("//*[@class='main']/*[@class='title']/a")
# print(song_name)
for name in song_name:
    # print(name, index)
    song_names_inside_playlist.append(name.text)
    # print(song_names_inside_playlist[index])
    # index = index + 1

# spotify section
SPOTIFY_USERNAME = sys.argv[1]

try:
    token = util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope='playlist-modify-public',
                                       client_id='841ebcf06a0c4564b8c966522fa447bc',
                                       client_secret='69ca8085fc5a40fda19b7a16c29b679b',
                                       redirect_uri='https://anudishjain.github.io/SaavnToSpotify/')
except Exception:
    os.remove(f".cache-{SPOTIFY_USERNAME}")
    token = util.prompt_for_user_token(SPOTIFY_USERNAME)

spotify = spotipy.Spotify(auth=token)

song_id_according_to_spotify = list()

index = 0
for song_name in song_names_inside_playlist:
    results = spotify.search(q=song_name, limit=1, offset=0, type='track', market=None)
    # print(results)
    try:
        song_id = results['tracks']['items'][0]['id']
        print(song_id)
        song_id_according_to_spotify.append(str(song_id))
    except IndexError:
        song_id = song_name + " not found in spotify"
        print(song_id)
