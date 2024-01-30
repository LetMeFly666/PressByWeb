'''
Author: LetMeFly
Date: 2024-01-30 21:07:22
LastEditors: LetMeFly
LastEditTime: 2024-01-30 21:37:33
'''
from flask import Flask, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate_keypress', methods=['POST'])
def simulate_keypress():
    pyautogui.hotkey('ctrl', 'alt', 'f5')
    return '按键成功'

if __name__ == '__main__':
    app.run(debug=True)

