#! bin/bash/python3

from lib.authorize import *
from lib.playlists import *


if __name__ == '__main__':

	spotify_authenticator = Authenticator('testing/configs/config.ini')
	spotify_authenticator.authorize()
	auth_header = spotify_authenticator.generate_header()

	username = 'NLeRoy917'
	wrapped_2019 = 'https://open.spotify.com/playlist/37i9dQZF1Ethb70Ir9WW6o?si=yrv4GDu6SBeUc8PexoZ_HQ'

	playlist_id = get_playlist_id(wrapped_2019)

	tracks = get_tracks(playlist_id,auth_header)

	for track in tracks:
		print(track['name'],'|',track['uri'])
