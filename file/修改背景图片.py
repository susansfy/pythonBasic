#regedit--HKEY_CURRENT_USER --Control panel--desktop--walpapper 背景图片地址

import  win32api
import  win32con
import  win32gui

def setWallPaper(path):
    #打印注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control panel\\desktop",
                                    0,win32con.KEY_SET_VALUE)
    #SPIF_SENDWININICHANGE 立即生效
    win32gui.SystemParamtersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)


    #修改注册表中的wallpaperStyle的值为6
    win32api.RegSetValueEx(reg_key,"wallpaperStyle",0,win32con.REG_SZ,6)



setWallPaper(r"c:\e.jpg")
