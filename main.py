from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.jiosaavn.com/login.php?action=login')
login_element_field = driver.find_element_by_id('login_username')
password_element_field = driver.find_element_by_id('login_password')
login_submit_button = driver.find_element_by_id('static-login-btn')

# ---------------------------------------------------------------------------------

# add username, only Email Login currently supported
login_element_field.send_keys("ENTER EMAIL ADDRESS")
#add password
password_element_field.send_keys("ENTER PASSWORD")

login_submit_button.click();
driver.implicitly_wait(2)

# ---------------------------------------------------------------------------------

# add names of the playlists that you want to convert
all_playlist = ['Playlist0', 'Playlist1', 'Playlist2'] 
playlists_links = []

for playlist in all_playlist :

	selected_playlist = driver.find_element(By.XPATH, '//a[text()="' + str(playlist) + '"]')
	playlists_links.append(selected_playlist.get_attribute("href"))

# ----------------------------------------------------------------------------------

all_song_names = []

for linkOfPlaylist in playlists_links :

	driver.get(linkOfPlaylist)
	driver.implicitly_wait(2);

	song_name = driver.find_elements(By.XPATH,"//span[@class='main']/span[@class='title']")

	for name in song_name :
		all_song_names.append(name.get_attribute('innerText'))
