import hwndManager
import time
import win32gui
from pypresence import Presence

TidalPid = hwndManager.findTidalPIDs()[0]

print("TidalPid = ",TidalPid)

hwnd = hwndManager.get_hwndTidal()

rpc = Presence("927718553837256784")
rpc.connect()


while True:

    time.sleep(0.5)

    windowName = win32gui.GetWindowText(hwnd)

    if windowName != "TIDAL":
             
        textList=windowName.split("-")
        trackName=textList[0]
        artistName=textList[1][1:]

        rpc.update(pid=TidalPid, state="by: " + artistName, details="Track: " + trackName, large_image="tidal")

        print("Track: ", trackName)
        print("by:    ", artistName)
    else:
        rpc.clear(pid=TidalPid)
        print("No music is currently playing")
 