# 戴尔 Latitude E7480 macOS Big Sur 11 / Monterey 12.0 (OpenCore引导)

<div style="align: center">
<img src="https://user-images.githubusercontent.com/66028151/130625664-655722d1-5936-4fd5-bc4c-4fb8c9720aab.png">
</div>
 
## 语言 / Lanuage
简体中文(当前语言)

[English](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README.md)

 
## 引导 & 硬件信息

<details>  
<summary><strong>OC引导版本</strong></summary>
</br>
OpenCore 0.7.0 / 0.7.1 / 0.7.2
</details>

<details>  
<summary><strong>硬件信息</strong></summary>
</br>

| Model           | Dell Latitude E7480                        |
|:----------------|:-------------------------------------------|
| 处理器           | Intel Core i7-7700U                        |
| 图形卡           | 集成显卡：Intel HD Graphics 620           |
| 内存条           | 8GB 2133MHz DDR4 * 2                       |
| 显示器           | 13" 2K (2560x1440) 触摸屏                   |
| 硬盘             | 闪迪 1T M.2 NVMe SSD                        |
| 无线网卡/蓝牙     | 博通 BCM94360Z4                        |
| 摄像头           | 1920x1080 FHD Webcam                       |
| 指纹读取          | 有但不适用于macOS                           |
| 声卡             | 瑞昱 ALC256                             |
| 键盘             | 背光键盘                           |
| 触摸板           | ALPS 触摸板                              |
| SD读卡器         | 瑞昱 RTS525A 读卡器        |

使用小贴士: 
* 对于苹果 macOS 12 Monterey, DW1820A网卡兼容性不那么好，主要是蓝牙驱动，导致隔空投送、接力等服务无法使用，于是换了张BCM9460Z4的网卡，目前无任何不兼容的问题！
* 强烈建议在进入系统以后使用[USBMap](https://github.com/corpnewt/USBMap) 工具进行USB定制！
* 如果你进行了硬件更改（比如网卡更换），同样也建议你使用[USBMap](https://github.com/corpnewt/USBMap) 工具重新进行USB定制！
* 进入系统后，建议重新生成对应机型序列号（需要经过官网查询无效方可使用）！
* 不要开启查找我的Mac功能！
</details>

## 工作状态

<details>  
<summary><strong>可用功能</strong></summary>
</br>

- [x] 显卡Intel HD 620 Graphics的正常驱动（包含双硬解码、GPU加速）
- [x] 所有的USB端口都正常工作 (注意：Type-C接口不适用热插拔！要使用Type-C接口请关机接上后再启动！)
- [x] 内置摄像头
- [x] Wifi 使用[AirportBrcmFixup](https://github.com/acidanthera/AirportBrcmFixup)成功稳定驱动（2.4GHz/5G）
- [x] 蓝牙 使用[BrcmFirmareData and BrcmPatchRAM3](https://github.com/acidanthera/BrcmPatchRAM)驱动（macOS仅需使用其中的BlueToolfixup，配置文件都已经设置好）
- [x] 关机/ 重启/ 睡眠/ 唤醒 (包含 Fn + insert 键睡眠和合盖睡眠)
- [x] 扬声器和耳机插孔
- [x] Intel 有线网络
- [x] 苹果商店和iCloud账户服务，不要开启查找我的Mac功能！
- [x] (不一定可用，和你的账户也有关系) iMessage 和 Facetime 
- [x] miniDP 和 HDMI （支持音频输入）
- [x] 键盘和触摸屏(触摸屏支持部分手势)
- [x] 隔空投送、接力、随航、隔空播放（隔空播放仅限macOS 12）
- [x] SD读卡器使用 [RealtekCardReader](https://github.com/0xFireWolf/RealtekCardReader) 和 [RealtekCardReaderFriend](https://github.com/0xFireWolf/RealtekCardReaderFriend) 驱动，使得SD读卡器原生化。

</details>

<details>  
<summary><strong>不可用功能</strong></summary>
</br>

- [ ] 触摸板不支持多手势。

</details>

## 对于Intle无线网卡

你既可以在windows下操作，也可以在macOS下操作。

### 准备工作
<details>  
<summary><strong>编辑Config.plist的工具: ProperTree</strong></summary>
</br>

* 下载工具: [ProperTree](https://github.com/corpnewt/ProperTree)
* 解压: 将下载的文件解压到桌面
* 运行 ProperTree

  * Windows下: 运行 ProperTree.bat
  * macOS下: 运行 ProperTree.command

</details>


### 下载和安装驱动
<details>  
<summary><strong>下载链接</strong></summary>
</br>

- WiFi 使用 [AirportItlwm](https://github.com/OpenIntelWireless/itlwm)驱动，注意对应系统版本。
- Bluetooth 使用 [IntelBluetoothFirmware and IntelBluetoothInjector](https://github.com/OpenIntelWireless/IntelBluetoothFirmware)驱动，同样注意对应系统版本。

</details>

<details>  
<summary><strong>安装 </strong></summary>
</br>

- 在目录 `\EFI\OC\Kexts\`下, 移除以下文件

  * `BrcmBluetoothInjector.kext`
  * `BrcmFirmwareData.kext`
  * `BrcmPatchRAM3.kext`
  * `BlueToolfixup.kext`(macOS12 不需要移除)

- 解压并复制下载的驱动到目录`\EFI\OC\Kexts\`

  * `AirportItlwm.kext`
  * `IntelBluetoothFirmware.kext`
  * `IntelBluetoothInjector.kext` 
  * 对于12系统可能会有其他的驱动，按照驱动网址的说明来

- 运行 ProperTree
- 挂载EFI盘
- 在软件的菜单栏, 选择 `Files` -> `OC snapshot` -> 选择文件夹 `\EFI\OC`
- 保存文件
- 重启或者安装系统然后享受吧!

</details>

## 引用
* [Acidanthera](https://github.com/Acidanthera) 的 OC包和主要的驱动
* [daliansky](https://github.com/daliansky) 的很棒的SSDTs在 [OC-little](https://github.com/daliansky/OC-little)
* [Dortania](https://dortania.github.io/)的OC安装教程
