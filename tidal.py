#Currently not used

import tidalapi

session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()
album = session.album(109485854)
tracks = album.tracks()
for track in tracks:
    print(track.name)