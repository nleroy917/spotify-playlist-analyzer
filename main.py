#! bin/bash/python

from lib.authorize import *
from lib.playlists import *
from lib.track_analysis import *
import sys

if __name__ == '__main__':

	spotify_authenticator = Authenticator('testing/configs/config.ini')
	spotify_authenticator.authorize()
	auth_header = spotify_authenticator.generate_header()

	username = spotify_authenticator.username
	
	playlists = get_playlists(username,auth_header)

	found = 0

	for playlist in playlists:
		# print(playlist['name'],'|',playlist['id'])
		if 'Top Songs 2019' in playlist['name']:
			found = 1
			wrapped_id = playlist['id']
			break

	if not found:
		print('Spotify Wrapped 2019 PLaylist not found! Please ensure you are following this playlist!')
		sys.exit(0)

	tracks = get_tracks(wrapped_id,auth_header)

	for track in tracks:
		analysis = get_track_data(track['id'],auth_header)
		print(track['name'],'|',analysis['loudness'],'|',int_to_key(analysis['key']),'|',int_to_mode(analysis['mode']),'|',analysis['tempo'])

	loudness_data = loudness_analysis(tracks,auth_header,show_plot=True)
	key_data, mode_data = key_analysis(tracks,auth_header,show_plot=True)
	tempo_data = tempo_analysis(tracks,auth_header,show_plot=True)

	print(loudness_data)
	print(key_data)
	print(mode_data)
	print(tempo_data)
