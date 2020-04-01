<div align="center">
  <h1>RasCon Ver.1.1</h1>
  <p>蓝牙连接Nintendo Switch，并可通过网页控制和使用脚本</p>
  <p>基于开源项目  <a href="https://github.com/mart1nro/joycontrol">joycontrol</a></p>
  <p>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/forks/SkyoKen/RasCon_NS.svg" alt="forks"></a>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/stars/SkyoKen/RasCon_NS.svg" alt="stars"></a>
  <a href="https://github.com/SkyoKen/RasCon_NS"><img src="https://img.shields.io/github/license/SkyoKen/RasCon_NS.svg" alt="license"></a>
  </p>
  <p>
  <a href="https://github.com/SkyoKen/RasCon_NS/blob/master/README.md">中文</a> | 
  <a href="https://github.com/SkyoKen/RasCon_NS/blob/master/README_JP.md">日本語</a> | 
  <a href="https://github.com/SkyoKen/RasCon_NS/blob/master/README_EN.md">ENGLISH</a>
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
2.修改joycontrol中的controller_state.py的设定
```
sudo nano RasCon_NS/joycontrol/controller_state.py
```
将约18行的`self.l_stick_state = self.r_stick_state = None`之后关于joycon的初期设定

```python
         if controller in (Controller.PRO_CONTROLLER, Controller.JOYCON_L):
             # load calibration data from memory
             calibration = None
             if spi_flash is not None:
                 calibration_data = spi_flash.get_user_l_stick_calibration()
                 if calibration_data is None:
                     calibration_data = spi_flash.get_factory_l_stick_calibration()
                 calibration = LeftStickCalibration.from_bytes(calibration_data)
             self.l_stick_state = StickState(calibration=calibration)
         # create right stick state
         if controller in (Controller.PRO_CONTROLLER, Controller.JOYCON_R):
             # load calibration data from memory
             calibration = None
             if spi_flash is not None:
                 calibration_data = spi_flash.get_user_r_stick_calibration()
                 if calibration_data is None:
                     calibration_data = spi_flash.get_factory_r_stick_calibration()
                 calibration = RightStickCalibration.from_bytes(calibration_data)
             self.r_stick_state = StickState(calibration=calibration)
```
改为

```python
         self.l_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
         self.r_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
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

### Q：python3的dbus库不存在

A： 运行`sudo pip3 install dbus-python`

### Q：找不到hci0
A：确认hci0是否存在，运行命令`hciconfig`

（无法正常使用的话换个系统也许就好了，我树莓派用ubuntu18.04和ubuntu mate都无法启动hci0

## 参考
万恶之源 [Switch-Fightstick](https://github.com/progmem/Switch-Fightstick)

蓝牙模拟ns手柄 [joycontrol](https://github.com/mart1nro/joycontrol)

蓝牙模拟ns手柄实现剑盾自动化 [poke_auto_joy](https://github.com/xxwsL/poke_auto_joy)

小白也能写的自动化脚本 [EasyCon（伊机控）](https://github.com/nukieberry/PokemonTycoon)



