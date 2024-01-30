'''
Author: LetMeFly
Date: 2024-01-30 21:07:22
LastEditors: LetMeFly
LastEditTime: 2024-01-30 21:28:49
'''
from flask import Flask, request, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate_keypress', methods=['POST'])
def simulate_keypress():
    # 模拟按下Ctrl+Alt+F5键
    pyautogui.hotkey('ctrl', 'alt', 'f5')
    return '键盘按键模拟成功！'

if __name__ == '__main__':
    app.run(debug=True)
