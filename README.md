<div align="center">
  <h1>RasCon Ver.1.2.1</h1>
  <p>蓝牙连接Nintendo Switch，并可通过网页控制和使用脚本与amiibo</p>
  <p>基于开源项目  <a href="https://github.com/mart1nro/joycontrol">joycontrol</a></p>
  <p>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/forks/SkyoKen/RasCon_NS.svg" alt="forks"></a>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/stars/SkyoKen/RasCon_NS.svg" alt="stars"></a>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/license/SkyoKen/RasCon_NS.svg" alt="license"></a>
  </p>
  <p>
  <a href="README.md">中文</a> | 
  <a href="README_JP.md">日本語</a> | 
  <a href="README_EN.md">ENGLISH</a>
</p>
</div>

## 界面
<br/>
<img src="image.png">
<br/>

## 运行环境 
* python 3.7.3
* bluetoothd 5.50
* apache2 2.4.38  
* flask 1.0.2 

raspi3b+（rasbian）下成功运行

## 初次使用
1.需要将joycontrol项目的joycontrol文件夹复制到该项目目录下
```
sudo git clone https://github.com/SkyoKen/RasCon_NS.git

sudo git clone https://github.com/mart1nro/joycontrol.git

sudo cp -r joycontrol/joycontrol RasCon_NS/
```
2.安装所需要的库
```
sudo apt install python3-dbus libhidapi-hidraw0 apache2

sudo pip3 install dbus-python flask hid aioconsole crc8
```

## 快速运行
1．打开终端，运行命令
```
sudo python3 web.py
```
2．浏览器打开 树莓派ip地址:5000 （网页操作界面）

3．switch的手柄界面,进入手柄搜索模式

4．打开另一个终端，运行命令
```
sudo python3 run.py
```
5．连接上后，即可用网页进行操作

## 参考用脚本
https://github.com/SkyoKen/RasCon_NS/releases

## 可能遇到的问题

### Q：找不到hci0
A：确认hci0是否存在，运行命令`hciconfig`

（无法正常使用的话换个系统也许就好了，我树莓派用ubuntu18.04和ubuntu mate都无法启动hci0

## 参考
万恶之源 [Switch-Fightstick](https://github.com/progmem/Switch-Fightstick)

蓝牙模拟ns手柄（可模拟amiibo） [joycontrol](https://github.com/mart1nro/joycontrol)

蓝牙模拟ns手柄实现剑盾自动化 [poke_auto_joy](https://github.com/xxwsL/poke_auto_joy)

小白也能写的自动化脚本 [EasyCon（伊机控）](https://github.com/nukieberry/PokemonTycoon)



