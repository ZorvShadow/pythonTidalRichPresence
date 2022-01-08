
#Currently not working 07/01/2022

import tidalapi

session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()
album = session.album(16909093)
tracks = album.tracks()
for track in tracks:
    print(track.name)