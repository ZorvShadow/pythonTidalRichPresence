#Currently not used
#Just for testing

import tidalapi

session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()

print(session.search("IGOR",models=[tidalapi.Album],limit=50,offset=0))