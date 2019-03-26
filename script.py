import os
import sys
import spotipy
import logging
import spotipy.util as util
import more_itertools
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    driver = webdriver.Firefox()
except WebDriverException:
    logger.critical("WebDriver exception has been caught")
else:
    logger.info("WebDriver has been initiated")

    # Add the URL of a public playlist. This change has been done to avoid exposing credentials to the script.
try:
    driver.get('https://www.jiosaavn.com/s/playlist/032b3a04e8d31d8fa5534b6ee2319775/Sainath/'
               'SFHfC8PSBlEGSw2I1RxdhQ__?referrer=svn_source%3Dshare&svn_medium=com.whatsapp&utm_source=share&utm_'
               'medium=com.whatsapp')
    driver.maximize_window()
except TimeoutError:
    logger.critical("Website Timeout ! Please check your internet connection.")

logger.info("Website opened")

song_names_inside_playlist = list()
try:
    playlist_name = driver.find_element_by_xpath("//*[@class = 'page-title ellip']").text
    song_name = driver.find_elements_by_xpath("//*[@class='main']/*[@class='title']/a")
except NoSuchElementException:
    logger.critical("Element not found exception")

# Addding Saavn songs to a list
for name in song_name:
    song_names_inside_playlist.append(name.text)

logger.info("Saavn song names collected")

try:
    driver.close()
except WebDriverException:
    logger.critical("Issue in closing webdriver connection")
else:
    logger.info("Webdriver instance closed successfully !")

logger.info("Spotify code execution started")
# spotify secttion
SPOTIFY_USERNAME = sys.argv[ 1 ]
try:
    token = util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope='playlist-modify-public',
                                       client_id='841ebcf06a0c4564b8c966522fa447bc',
                                       client_secret='69ca8085fc5a40fda19b7a16c29b679b',
                                       redirect_uri='https://anudishjain.github.io/SaavnToSpotify/')
except Exception:
    os.remove(f".cache-{SPOTIFY_USERNAME}")
    token = util.prompt_for_user_token(SPOTIFY_USERNAME)
else:
    logger.info("Authenticated successfully with Spotify API")

spotify = spotipy.Spotify(auth=token)
song_id_according_to_spotify = list()

for song_name in song_names_inside_playlist:
    results = spotify.search(q=song_name, limit=1, offset=0, type='track', market=None)
    try:
        song_id = results[ 'tracks' ][ 'items' ][ 0 ][ 'id' ]
        song_id_according_to_spotify.append(str(song_id))
    except IndexError:
        logger.warning(f"%s not found in Spotify", song_name)

# Split the song id list into lists of 100 song ids per list
song_id_according_to_spotify = more_itertools.chunked(song_id_according_to_spotify, 100)
logger.info("Script started adding songs to spotify playlist")

# code to add songs to spotify playlist
current_playlist_id = spotify.user_playlist_create(str(SPOTIFY_USERNAME), playlist_name)
logger.info(f"%s playlist created in spotify", playlist_name)
current_playlist_id = str(current_playlist_id[ 'id' ])
for song_id in song_id_according_to_spotify:
    spotify.user_playlist_add_tracks(str(SPOTIFY_USERNAME), current_playlist_id, song_id)

logger.info("All the songs added to playlist. Thanks for using the script !")
