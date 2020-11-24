"""
author: DuanMing
email: dmneil7o@icloud.com
wechat: LivPzs
"""

from pynput.keyboard import Key, Controller, Listener


keyboard = Controller()
my_stack = 0   # 栈标志
key_map = {"h": Key.left, "j": Key.down, "k": Key.up, "l": Key.right}


def on_press(key):
    global my_stack
    if key == Key.esc:
        my_stack = 1
    elif hasattr(key, 'char') and my_stack == 1 and key.char in key_map:
        keyboard.press(Key.backspace)
        keyboard.press(key_map[key.char]) 


def on_release(key):
    global my_stack
    if key == Key.esc:
        my_stack = 0


# 创建监听
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

