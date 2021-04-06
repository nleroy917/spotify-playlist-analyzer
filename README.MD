# Archived Repo for Historical Purposes
This code was the gensis of my site [spottydata.com](https://www.spottydata.com/). I am keeping it here for historical purposes, but the project has long since progressed to a more advanced web-app version that can be found [here](https://github.com/NLeRoy917/spottydata).

# Spotify Wrapped Analysis
---
The purpose of this code is to provide the groundwork for a potential website that can analyze someones spotify-wrapped playlist and provide analytics on all of the songs/music

It can be run locally on your machine to analyze your own playlists, however. Currently, the script is only supported on Linux and MacOSX.

1.  Git clone this repo onto your system

2.  Run the setup.sh script to download the gecko driver and set up the directories: 
	**For Linux**:
	```./setup.sh```
	**for MacOSX**:
	```sh setup.sh```

3.  Fill out the config file accordingly with your username and password
	Yes, I gave you access to the client secret . . . please be nice with it

4.  The script will automatically search your playlists for the Top Songs 2019 playlist... Make sure you have already had Spotify generate this data for you and you are following the playlist (I assume you are if you are reading this documentation). If you wish to view this data for any of your other playlists, you can change the hard coded playlist name in the main script on **line 22**.

5.  Run the main script:
	```python main.py```

---
Known/Potential Issues:
* Setup Script uses python to find correct downlaod file... If your system uses python3, change ```python``` command call on **lines 22 and 24** to ```python3```
* Script has it hard coded in to look for the wrapped playlist... If you wish to analyze this data for any other playlist, it must be hard coded in.

