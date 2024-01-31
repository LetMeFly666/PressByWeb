<!--
 * @Author: LetMeFly
 * @Date: 2024-01-30 21:02:09
 * @LastEditors: LetMeFly
 * @LastEditTime: 2024-01-31 21:50:46
-->
# PressByWeb(Remote Keyboard)

通过网页在电脑上按下快捷键。

> [!TIP]
>
> 电脑在卧室放歌人在客厅吃饭，想“下一曲”又懒得动，怎么用手机**简单**地控制一下电脑呢？通过访问电脑(服务器)提供的网页来向电脑发送快捷键吧！

+ 仓库地址：[Github@LetMeFly666/PressByWeb](https://github.com/LetMeFly666/PressByWeb)
+ 在线文档：[PressByWeb.LetMeFly.XYZ](https://pressbyweb.letmefly.xyz/)

## 配置方法

1. 下载本仓库到本地
2. 电脑上安装好```Python```，安装好```flask```库
3. （可选）在```main.py```同级的目录新建```mySecrets.py```，修改其中内容为```PASSWORD = '访问密码'```
4. 执行命令```python main.py```（可以看到提示：```Running on http://192.168.1.2:82```）
5. 关闭电脑防火墙（不推荐）**或**新增82端口的tcp入栈规则（详情请见[如何开启单个端口以供Web应用访问(以82端口为例)](https://leetcode.letmefly.xyz/2024/01/31/Other-Windows-FireWall-Open1PortForWebserver-WhyFailed/)）
6. 手机连接到电脑的统一网络下（同一wifi、同一校园网、热点共享 等均可），访问第```4.```步中显示的地址，看到“输入密码的提示”即为配置成功

![输入密码](https://github.com/LetMeFly666/PressByWeb/assets/56995506/e3e7ecce-c264-43ea-b253-b0581d98da11)

## 使用方法

在“输入密码”界面输入你设置的密码（若进行了[配置方法](#配置方法)中的第三步则为“访问密码”，否则为“123”）

在电脑端将会看到界面如下：

![电脑端](https://github.com/LetMeFly666/PressByWeb/assets/56995506/a5f0b586-547c-4e3a-a84b-ff72ab908e27)

在手机端将会看到界面如下：

![手机端](https://github.com/LetMeFly666/PressByWeb/assets/56995506/1944c19c-3217-4c73-88b9-c5b34bcf2f30)

其中```快捷键```标题下的5个按钮为很多音乐软件常用的快捷键，单击一下即可将快捷键发送到后端执行。

其中```组合键```标题下的24个按钮为常用的按钮，依次单击，选择好后点击“发送按钮”，即可将按键组合发送到后端执行。

## Acknowledge

+ 感谢[ChatGPT](https://chat.openai.com/share/2271834f-3a12-4bdc-89ee-a78e2c1faa7b)的帮助（虽然到最后GPT开始瞎扯了）。
+ 感谢[@Tisfy](https://github.com/Tisfy)的[按键功能建议#1](https://github.com/LetMeFly666/PressByWeb/issues/1)

## TODO

+ Make 1 video to BiliBili
