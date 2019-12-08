#! bin/bash/python3

from lib.authorize import *
from lib.playlists import *
from lib.track_analysis import *


if __name__ == '__main__':

	spotify_authenticator = Authenticator('testing/configs/config.ini')
	spotify_authenticator.authorize()
	auth_header = spotify_authenticator.generate_header()

	username = 'NLeRoy917'
	wrapped_2019 = 'https://open.spotify.com/playlist/37i9dQZF1Ethb70Ir9WW6o?si=yrv4GDu6SBeUc8PexoZ_HQ'

	wrapped_id = get_playlist_id(wrapped_2019)

	tracks = get_tracks(wrapped_id,auth_header)

	for track in tracks:
		analysis = get_track_data(track['id'],auth_header)
		print(track['name'],'|',analysis['loudness'])

	loudness_data = playlist_loudness_analysis(tracks,auth_header)

	print('-='*30)
	for key in loudness_data:
		print(key,':',loudness_data[key])
