#Currently not used
#Just for testing

import tidalapi
import webbrowser

session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple(function=webbrowser.open)

def searchTrack(searchquerry):

    artists = ""

    trackDict = session.search(searchquerry,models=[tidalapi.media.Track],limit=50,offset=0)

    track=trackDict.get("top_hit")

    print(track.name)
    print(len(track.artists))
    #for x in track.artists:
       # print(x.name)
searchTrack("edamame")  

