import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import sys
import requests
from spotipy.oauth2 import SpotifyClientCredentials

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
release_year= int(date.split("-")[0])

# Replace with your own client ID and client secret from Spotify Developer Dashboard
client_id = 'Your-CLIENT-ID'
client_secret = 'YOUR-CLIENT-SECRET'


billboardsite= 'https://www.billboard.com/charts/hot-100/' + date
response= requests.get(billboardsite)
billboard_webpage =response.text
soup= BeautifulSoup(billboard_webpage, "html.parser")

song= soup.find_all('h3', id="title-of-a-story")
songs=[]
# song1= song[5].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0]
if song[5].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1]!='Additional Awards':
    for i in range(6, 402, 4):
        songs.append(song[i].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0])
else:
    for i in range(5,402,4):
        songs.append(song[i].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0])
    # print(song[i].getText())
print(songs)
# print(billboard_webpage)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def find_spotify_id(track_name, release_year):
    # Search for track by name
    results = sp.search(q=track_name, type='track', limit=10)

    # Filter tracks by release date (year)
    tracks = results['tracks']['items']
    for track in tracks:
        track_release_year = int(track['album']['release_date'][:4])  # Extract year from release_date
        if track_release_year >= release_year:
            spotify_id = track['id']
            return spotify_id

    return None


spotify_ids=[]
for i in songs:
    spotify_id = find_spotify_id(i, release_year)
    if spotify_id:
        track_id= 'spotify:track:' + spotify_id
        spotify_ids.append(track_id)
        # print(f"Spotify ID of '{i}' is: {spotify_id}")
    else:
        continue
        # print(f"Could not find Spotify ID for '{i}'")

print(spotify_ids)


redirect_uri = 'http://example.com'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-modify-private playlist-modify-public'))


def create_spotify_playlist(playlist_name, track_ids):

  user_id = sp.me()['id']
  playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
  playlist_id = playlist['id']


  sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)

  print(f"Playlist '{playlist_name}' created successfully!")


# Example usage
playlist_name = f'Billboard of {date}'


create_spotify_playlist(playlist_name, spotify_ids)






client_id = 'Your-CLIENT-ID'
client_secret = 'YOUR-CLIENT-SECRET'
# SPOTIPY_REDIRECT_URI= "example.com"
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
# import sys
# import requests
#
#
# # sp = spotipy.Spotify(
# #     auth_manager=SpotifyOAuth(
# #         scope="playlist-modify-private",
# #         redirect_uri="http://example.com",
# #         client_id=CLIENT_ID,
# #         client_secret=CLIENT_SECRET,
# #         show_dialog=True,
# #         cache_path="token.txt",
# #         username='31qvpn7rfopfsdougbj3bcts4wki',
# #     )
# # )
# # user_id = sp.current_user()["id"]
#
# # date= input("Which year do you want to travel to? Enter the date in YYYY-MM-DD format: ")
#
# billboardsite= 'https://www.billboard.com/charts/hot-100/2016-07-09'
# response= requests.get(billboardsite)
# billboard_webpage =response.text
# soup= BeautifulSoup(billboard_webpage, "html.parser")
#
# song= soup.find_all('h3', id="title-of-a-story")
# songs=[]
# song1= song[5].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0]
# print(song1)
# if song1=='Additional Awards':
#     flag=True
# else:
#     flag=False
# if flag==True and song[6].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0]=='Songwriter(s):':
#     for i in range(5, 402, 4):
#         songs.append(song[i].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0])
# else:
#     for i in range(6,402,4):
#         songs.append(song[i].getText().split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0])
#     # print(song[i].getText())
#
# print(songs)
# # print(billboard_webpage)
# #
# #
# # # date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# # print(date.split('-')[0])
