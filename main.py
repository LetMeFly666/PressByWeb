'''
Author: LetMeFly
Date: 2024-01-30 21:07:22
LastEditors: LetMeFly
LastEditTime: 2024-01-30 22:28:00
'''
from flask import Flask, request, render_template
import pyautogui

app = Flask(__name__)

# 定义键盘组合与操作的映射关系
keyboard_mapping = {
    "Ctrl+Alt+F5": ("ctrl", "alt", "f5"),
    "Ctrl+Alt+→": ("ctrl", "alt", "right"),
    "Ctrl+Alt+←": ("ctrl", "alt", "left"),
    "Ctrl+Alt+↑": ("ctrl", "alt", "up"),
    "Ctrl+Alt+↓": ("ctrl", "alt", "down")
}

@app.route('/')
def index():
    return render_template('index.html', keyboard_mapping=keyboard_mapping)

@app.route('/simulate_keypress', methods=['POST'])
def simulate_keypress():
    key_combination = request.json.get('key')
    if key_combination in keyboard_mapping:
        key_sequence = keyboard_mapping[key_combination]
        pyautogui.hotkey(*key_sequence)  # 解包键序列
        return '快捷键按键成功'
    else:
        return '未知的键盘组合'

@app.route('/simulate_keysequence', methods=['POST'])
def simulate_keysequence():
    keys = request.json.get('keys')
    pyautogui.hotkey(*keys)  # 解包键序列
    return '按键序列成功模拟'

if __name__ == '__main__':
    app.run(debug=True)
