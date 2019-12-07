#! bin/bash/python3

from lib.authorize import *


if __name__ == '__main__':

	playlist_URI = 'spotify:playlist:7iGY7WPiTvvSTr6ZgO3rR2'
	playlist_share_link = 'https://open.spotify.com/playlist/7iGY7WPiTvvSTr6ZgO3rR2?si=iDvebMC4Q8Kderz6HyegOA'

	spotify_authenticator = Authenticator('testing/configs/config.ini')
	spotify_authenticator.authorize()
	auth_header = spotify_authenticator.generate_header()

	username = 'NLeRoy917'
	response = requests.get('https://api.spotify.com/v1/users/{}/playlists'.format(username),
                            headers=auth_header)

	playlists = json.loads(response.text)

	for item in playlists['items']:

		if item['owner']['display_name'].lower() == username.lower():
			print(item['name'])
			for thing in item:
				print('\t',thing,item[thing])
			print()
			print()