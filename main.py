'''
Author: LetMeFly
Date: 2024-01-30 21:07:22
LastEditors: LetMeFly
LastEditTime: 2024-01-30 23:16:03
'''
from flask import Flask, request, render_template
from functools import wraps
import pyautogui
try:
    import mySecrets
    PASSWORD = mySecrets.PASSWORD
except:
    PASSWORD = '123'



app = Flask(__name__)

# 定义键盘组合与操作的映射关系
keyboard_mapping = {
    "Ctrl+Alt+F5": ("ctrl", "alt", "f5"),
    "Ctrl+Alt+→": ("ctrl", "alt", "right"),
    "Ctrl+Alt+←": ("ctrl", "alt", "left"),
    "Ctrl+Alt+↑": ("ctrl", "alt", "up"),
    "Ctrl+Alt+↓": ("ctrl", "alt", "down")
}


def authChecker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thisKey = request.cookies.get('key')
        print(thisKey)
        if thisKey != PASSWORD:
            return """<body><input id="keyInput" type="text" placeholder="Enter key value" onkeydown="if(event.keyCode === 13) { document.cookie = 'key=' + this.value + ';path=/;expires=' + new Date(new Date().getTime() + 86400000 * 365 * 20).toUTCString(); location.reload(); }" value=""><button onclick="document.cookie = 'key=' + document.getElementById('keyInput').value + ';path=/;expires=' + new Date(new Date().getTime() + 86400000 * 365 * 20).toUTCString(); location.reload();">设置 Cookie 并刷新</button><script>document.getElementById('keyInput').value = (document.cookie.match('(^|;) ?key=([^;]*)(;|$)') || [])[2] || '';</script></body>"""
        return func(*args, **kwargs)
    return wrapper


@app.route('/')
@authChecker
def index():
    return render_template('index.html', keyboard_mapping=keyboard_mapping)


@app.route('/simulate_keypress', methods=['POST'])
@authChecker
def simulate_keypress():
    key_combination = request.json.get('key')
    if key_combination in keyboard_mapping:
        key_sequence = keyboard_mapping[key_combination]
        pyautogui.hotkey(*key_sequence)  # 解包键序列
        return '快捷键按键成功'
    else:
        return '未知的键盘组合'


@app.route('/simulate_keysequence', methods=['POST'])
@authChecker
def simulate_keysequence():
    keys = request.json.get('keys')
    pyautogui.hotkey(*keys)  # 解包键序列
    return '按键序列成功模拟'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='82', debug=True)
