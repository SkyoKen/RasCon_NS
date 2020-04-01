<div align="center">
  <h1>RasCon Ver.1.0</h1>
  <p>Bluetooth経由でNintendo Switchに接続して、Webページからの制御とスクリプトの利用を可能にします。。</p>
  <p>オープンソースプロジェクト<a href="https://github.com/mart1nro/joycontrol">joycontrol</a>に基づいて</p>
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

## 画面
<br/>
<img src="image.png">
<br/>

## 環境
* python 3.7.3
* bluetoothd 5.50
* apache2 2.4.38  
* flask 1.0.2 

raspi3b +（rasbian）で正常に実行されます。

## 使用する前に
1.joycontrolプロジェクトのjoycontrolフォルダーをこのプロジェクトディレクトリにコピーする必要があります。
```
sudo git clone https://github.com/SkyoKen/RasCon_NS.git

sudo git clone https://github.com/mart1nro/joycontrol.git

sudo cp -r joycontrol/joycontrol RasCon_NS/
```
2.joycontrolフォルダ中のcontroller_state.pyの設定を編集
```
sudo nano RasCon_NS/joycontrol/controller_state.py
```
约18行の`self.l_stick_state = self.r_stick_state = None`の下にjoyconの初期設定を削除
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
下のコードを追加
```python
         self.l_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
         self.r_stick_state = StickState(0x07FF, 0x07FF, calibration = _StickCalibration(0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF, 0x07FF))
```
## 実行
1．ターミナルを開き、コマンドを実行します
```
sudo python3 web.py
```
2．ブラウザを使用して、Raspberry PiのIPアドレス：5000（E.g 192.168.1.100:5000）を開きます

3．[コントローラー]-> [持ちかた順番を変える]をクリックします

4．他のターミナルを開き、コマンドを実行します
```
sudo python3 run.py
```
5．接続後、ウェブページを操作できます

## 参考用スクリプト
https://github.com/SkyoKen/RasCon_NS/releases

## Possible problems

### Q：No module named 'dbus'

A： `sudo pip3 install dbus-python`を実行します

### Q：hci0 device not found
A：hci0が存在するかどうかを確認、`hciconfig`を実行します

（正常に動作しない場合...別のシステムに変更した後に動作する可能性があります。 Raspberry Piがubuntu18.04とubuntu mateでhci0を起動できないことがありました...

## 参考
万恶之源 [Switch-Fightstick](https://github.com/progmem/Switch-Fightstick)

蓝牙模拟ns手柄 [joycontrol](https://github.com/mart1nro/joycontrol)

蓝牙模拟ns手柄实现剑盾自动化 [poke_auto_joy](https://github.com/xxwsL/poke_auto_joy)

小白也能写的自动化脚本 [EasyCon（伊机控）](https://github.com/nukieberry/PokemonTycoon)



