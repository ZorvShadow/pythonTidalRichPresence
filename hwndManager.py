from logging import error
import time
import wmi
import win32gui
import win32process

hwndList= []

        
def findTidalPIDs():
    f = wmi.WMI()
            
    pidList = []
    
    print("Fetching all Tidal PIDs...")

    for process in f.Win32_Process():        
        if process.Name == "TIDAL.exe":
            pidList.append(process.ProcessID)
    if pidList:
      print("Tidal PIDs found: ", pidList)
      time.sleep(0.5)
      return pidList
    else:
      print("Tidal.exe was not found, exiting program...")
      time.sleep(1)
      raise Exception('Tidal.exe was not found')

        
def get_hwnds_for_pid (pid):
  def callback (hwnd, hwnds):
    if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
      _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
      if found_pid == pid:
        hwnds.append (hwnd)
    return True
    
  hwnds = []
  win32gui.EnumWindows (callback, hwnds)
  return hwnds

def get_hwndTidal():
    print("Trying to get HWND from Tidal...")
    for x in findTidalPIDs():
        if get_hwnds_for_pid(x):
            strings = [str(integer) for integer in get_hwnds_for_pid(x)]
            hwndString = "".join(strings)
            print("Tidal HWND found: ", hwndString)
            return hwndString


            

        
