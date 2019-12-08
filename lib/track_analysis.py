from lib.authorize import *
from lib.playlists import *
from configparser import SafeConfigParser
import numpy as np

def get_track_data(track_id,auth_header):

	response = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(track_id),
                            headers=auth_header)

	return_package = json.loads(response.text)

	#print(return_package)

	analysis = return_package

	return analysis

def playlist_loudness_analysis(tracks,auth_header):

	loudness_store = []

	for track in tracks:
		analysis = get_track_data(track['id'],auth_header)
		loudness_store.append(analysis['loudness'])

	loudness_data = {'average':None,
					 'median':None,
					 'std':None}

	loudness_data['average'] = np.average(loudness_store)
	loudness_data['median'] = np.median(loudness_store)
	loudness_data['std'] = np.std(loudness_store)

	return loudness_data

def key_distribution(tracks,auth_header):

	key_store = []

	for track in tracks:
		analysis = get_track_data(track['id'],auth_header)
		key_store.append(analysis['key'])

	
	for key in key_store:
		pass

	return





	return loudness_data

if __name__ == '__main__':

	spotify_authenticator = Authenticator('testing/configs/config.ini')
	spotify_authenticator.authorize()
	auth_header = spotify_authenticator.generate_header()

	username = 'NLeRoy917'
	wrapped_2019 = 'https://open.spotify.com/playlist/37i9dQZF1Ethb70Ir9WW6o?si=yrv4GDu6SBeUc8PexoZ_HQ'

	playlist_id = get_playlist_id(wrapped_2019)

	tracks = get_tracks(playlist_id,auth_header)

	for track in tracks:
		analysis = get_track_data(track['id'],auth_header)
		print(track['name'],'|',analysis['loudness'])


