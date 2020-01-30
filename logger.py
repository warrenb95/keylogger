from pynput.keyboard import Key, Listener
from collections import defaultdict
import json

keyCount = defaultdict(int)

def onKeyPress(key):
    if key == Key.pause:
        saveData()
        return False

    keyCount[str(key)] += 1

def saveData():
    with open('keylogs.json') as dataFile:
        try:
            oldData = json.load(dataFile)

            for key, value in oldData.items():
                keyCount[key] += value
        except:
            print('keylogs.json is empty')

    with open('keylogs.json', 'w') as dataFile:
        json.dump(keyCount, dataFile, indent = 4)

    print('Key Logger is exiting...')
    exit()

with Listener(on_press = onKeyPress) as listener:
    listener.join()
