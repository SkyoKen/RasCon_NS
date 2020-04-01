<div align="center">
  <h1>RasCon Ver.1.0</h1>
  <p>Connect to Nintendo Switch over Bluetooth, to enable control and script from the web.</p>
  <p>Based on open source projects  <a href="https://github.com/mart1nro/joycontrol">joycontrol</a></p>
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

## ScreenShot
<br/>
<img src="image.png">
<br/>

## Environment
* python 3.7.3
* bluetoothd 5.50
* apache2 2.4.38  
* flask 1.0.2 

Successfully run under raspi3b + (rasbian)

## Before use
1.Need to copy the joycontrol folder of the jotcontrol project to this project directory
```
sudo git clone https://github.com/SkyoKen/RasCon_NS.git

sudo git clone https://github.com/mart1nro/joycontrol.git

sudo cp -r joycontrol/joycontrol RasCon_NS/
```
2.Need to change `controller_state.py`
```
sudo nano RasCon_NS/joycontrol/controller_state.py
```
Change the code
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
to
```python
         self.l_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
         self.r_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
```
## Run
1．Open one terminal, and run the command
```
sudo python3 web.py
```
2．Use browser opens Raspberry Pi IP address: 5000 (E.g 192.168.1.100:5000)

3．Click Controllers -> Change grip/Order

4．Open the other terminal, and run the command
```
sudo python3 run.py
```
5．After connected, you can use the webpage to operate

## For reference script
https://github.com/SkyoKen/RasCon_NS/releases

## Possible problems

### Q：No module named 'dbus'

A：Run `sudo pip3 install dbus-python`

### Q：hci0 device not found
A：Check if hci0 exists，run `hciconfig`

（If it doesn't work properly ... Maybe it works after changing to another system. My Raspberry Pi can't start hci0 with ubuntu18.04 and ubuntu mate ...

## Referrence
万恶之源 [Switch-Fightstick](https://github.com/progmem/Switch-Fightstick)

蓝牙模拟ns手柄 [joycontrol](https://github.com/mart1nro/joycontrol)

蓝牙模拟ns手柄实现剑盾自动化 [poke_auto_joy](https://github.com/xxwsL/poke_auto_joy)

小白也能写的自动化脚本 [EasyCon（伊机控）](https://github.com/nukieberry/PokemonTycoon)



