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
		print(track['name'],'|',analysis['loudness'],'|',int_to_key(analysis['key']),'|',int_to_mode(analysis['mode']),'|',analysis['tempo'])

	loudness_data = loudness_analysis(tracks,auth_header,show_plot=True)
	key_data, mode_data = key_analysis(tracks,auth_header)
	tempo_data = tempo_analysis(tracks,auth_header,show_plot=True)

	print(loudness_data)
	print(key_data)
	print(mode_data)
	print(tempo_data)
