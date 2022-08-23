from ewmh.ewmh import EWMH

ewmh = EWMH()

win = ewmh.getActiveWindow()
if win:
    print(win.get_wm_class())
