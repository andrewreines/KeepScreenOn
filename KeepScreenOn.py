"""
Does your computer still sleep / log you off even after changing your settings?
Does this break or interrupt a long running process?

Once every 10 seconds, this program simulates a click, followed by either an UP or DOWN keyboard stroke, preventing the above.

Ends after 12 hours (see line 21) or after keyboard interrupt.

When running, be sure to place your cursor in an appropriate area
"""

import pyautogui
import sys
import time

pyautogui.FAILSAFE = False
print('starting KeepScreenOn. Be sure to place your cursor in an appropriate area')

x = 1
try:
    while (True):
        if x == 6 * 60 * 12:
            print('exiting at x= ', x)
            sys.exit()
        else:
            x = x+1

        time.sleep(10)
        pyautogui.click()
        if x % 2 == 0:
            pyautogui.press('up')
        else:
            pyautogui.press('down')

        print('click# ', x)
        #pyautogui.moveTo(x, 600)

except KeyboardInterrupt:
    print('kb interrupt')
    sys.exit()

