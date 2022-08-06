# Changelog / 更新日志

## V0.8.2.1

### 发布时间 ： 2021.07.22

#### 添加功能 :

1. 雷电3支持（不完全支持）

Tip: Type-C 口有两个控制器：雷电3控制器和USB控制器，在此更新之前，USB控制器已经完全支持（包括热插拔），但是没有雷电3支持。本次更新仅修复了雷电3的识别，但并不能实现热插拔。如果你需要使用雷电3，请注意一下2点：

- 在启动电脑之前请插入雷电3设备（如果已经启动请关机插入后再开机）
- **不支持**热插拔

#### 文件变化:

1. 注入雷电3控制器信息

-------------------------------------------------------


## V0.8.2.0

### 发布时间： 2021.07.05

#### 添加功能 :

1. 更新OC版本至0.8.2并更新了驱动
2. 支持 MacOS 13 Ventura 
3. 将`USBPorts.kext`替换为`USBMap.kext`以改善USB口的性能

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.8.2
2. `USBPorts.kext` -> `USBMap.kext`
3. 更新驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.6	|	2022-07-03	|	官方编译	|
|	AppleALC	|	1.7.3	|	2022-07-05	|	官方编译	|
|	BlueToolFixup	|	2.6.3	|	2022-06-25	|	官方编译	|
|	BrcmBluetoothInjector	|	2.6.3	|	2022-06-25	|	官方编译	|
|	BrcmFirmwareData	|	2.6.3	|	2022-06-25	|	官方编译	|
|	BrcmPatchRAM3	|	2.6.3	|	2022-06-25	|	官方编译	|
|	CpuTscSync	|	1.0.9	|	2022-06-09	|	官方编译	|
|	FeatureUnlock	|	1.0.9	|	2022-07-05	|	官方编译	|
|	HibernationFixup	|	1.4.6	|	2022-07-04	|	官方编译	|
|	Lilu	|	1.6.1	|	2022-07-05	|	官方编译	|
|	SMCBatteryManager	|	1.3.0	|	2022-07-05	|	官方编译	|
|	SMCDellSensors	|	1.3.0	|	2022-07-05	|	官方编译	|
|	SMCLightSensor	|	1.3.0	|	2022-07-05	|	官方编译	|
|	SMCProcessor	|	1.3.0	|	2022-07-05	|	官方编译	|
|	SMCSuperIO	|	1.3.0	|	2022-07-05	|	官方编译	|
|	VirtualSMC	|	1.3.0	|	2022-07-05	|	官方编译	|
|	WhateverGreen	|	1.6.0	|	2022-07-05	|	官方编译	|


---------------------------------------


## V0.8.1.0

### 发布时间： 2021.06.11

#### 添加功能 :

1. 更新OC版本至0.8.1并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.8.1
2. 更新驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.6	|	2022-06-09	|	本地编译	|
|	AlpsHID	|	1.3	|	2022-06-11	|	本地编译	|
|	AppleALC	|	1.7.3	|	2022-06-08	|	本地编译	|
|	BlueToolFixup	|	2.6.3	|	2022-06-09	|	本地编译	|
|	BrcmBluetoothInjector	|	2.6.3	|	2022-06-09	|	官方编译	|
|	BrcmFirmwareData	|	2.6.3	|	2022-06-09	|	本地编译	|
|	BrcmPatchRAM3	|	2.6.3	|	2022-06-09	|	本地编译	|
|	FeatureUnlock	|	1.0.9	|	2022-06-09	|	本地编译	|
|	HibernationFixup	|	1.4.6	|	2022-06-09	|	本地编译	|
|	Lilu	|	1.6.1	|	2022-06-08	|	本地编译	|
|	NVMeFix	|	1.1.0	|	2022-06-09	|	本地编译	|
|	SMCBatteryManager	|	1.3.0	|	2022-06-07	|	本地编译	|
|	SMCDellSensors	|	1.3.0	|	2022-06-07	|	本地编译	|
|	SMCLightSensor	|	1.3.0	|	2022-06-07	|	本地编译	|
|	SMCProcessor	|	1.3.0	|	2022-06-07	|	本地编译	|
|	SMCSuperIO	|	1.3.0	|	2022-06-07	|	本地编译	|
|	VirtualSMC	|	1.3.0	|	2022-06-07	|	本地编译	|
|	WhateverGreen	|	1.6.0	|	2022-06-11	|	本地编译	|


---------------------------------------

## V0.8.0.0

### 发布时间： 2021.04.19

#### 添加功能 :

1. 更新OC版本至0.8.0并更新了驱动
2. 清理了未使用的驱动`CPUFriend.kext`

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.8.0
2. 删除了未使用的驱动`CPUFriend.kext`
3. 更新官方编译的驱动：
| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	CpuTscSync	|	1.0.8	|	2022-04-18	|	官方编译	|
|	FeatureUnlock	|	1.0.8	|	2022-04-18	|	官方编译	|


---------------------------------------

## V0.7.9.1

### 发布时间： 2021.03.17

#### 添加功能 :

​	修复了一个bug：系统偏好设置中的软件更新模块无法检测到系统更新.

#### 文件变化 :

​	更新了`config.plist`文件：键值`misc -> security -> SecureBootModel`变化：`Disabled -> Default`.

---------------------------------------

## V0.7.9.0

### 发布时间： 2021.03.09

#### 添加功能 :

1. 更新OC版本至0.7.9并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.9
2. 更新官方编译的驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AppleALC	|	1.7.0	|	2022-03-08	|	官方编译	|
|	CpuTscSync	|	1.0.7	|	2022-03-08	|	官方编译	|
|	FeatureUnlock	|	1.0.7	|	2022-03-08	|	官方编译	|
|	SMCBatteryManager	|	1.2.9	|	2022-03-08	|	官方编译	|
|	SMCDellSensors	|	1.2.9	|	2022-03-08	|	官方编译	|
|	SMCLightSensor	|	1.2.9	|	2022-03-08	|	官方编译	|
|	SMCProcessor	|	1.2.9	|	2022-03-08	|	官方编译	|
|	SMCSuperIO	|	1.2.9	|	2022-03-08	|	官方编译	|
|	VirtualSMC	|	1.2.9	|	2022-03-08	|	官方编译	|
|	Voodoo PS/2 Controller	|	2.2.8	|	2022-03-08	|	官方编译	|
|	WhateverGreen	|	1.5.8	|	2022-03-08	|	官方编译	|


-------------------------------------

## V0.7.8.0

### 发布时间： 2021.02.12

#### 添加功能 :
1. 更新OC版本至0.7.8并更新了驱动
2. 支持通用控制（需要macOS 12.3，博通网卡，iPad OS 15.4，亲测可用）

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.8
2. 更新官方编译的驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.4	|	2022-02-08	|	官方编译	|
|	AppleALC	|	1.6.9	|	2022-02-08	|	官方编译	|
|	CpuTscSync	|	1.0.6	|	2022-02-08	|	官方编译	|
|	FeatureUnlock	|	1.0.6	|	2022-02-08	|	官方编译	|
|	Lilu	|	1.6.0	|	2022-02-08	|	官方编译	|
|	RestrictEvents	|	1.0.7	|	2022-02-08	|	官方编译	|
|	WhateverGreen	|	1.5.7	|	2022-02-08	|	官方编译	|


-------------------------------------

## V0.7.7.0

### 发布时间： 2021.01.16

#### 添加功能 :
1. 更新OC版本至0.7.7并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.7
2. 更新官方编译的驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportItlwm	|	2.1.0	|	2021-12-31	|	官方编译	|
|	AppleALC	|	1.6.8	|	2022-01-10	|	官方编译	|
|	FeatureUnlock	|	1.0.5	|	2022-01-10	|	官方编译	|
|	IntelBluetoothFirmware	|	2.1.0	|	2022-01-01	|	官方编译	|
|	IntelBluetoothInjector	|	2.1.0	|	2022-01-01	|	官方编译	|
|	Lilu	|	1.5.9	|	2022-01-10	|	官方编译	|
|	RestrictEvents	|	1.0.6	|	2022-01-10	|	官方编译	|
|	WhateverGreen	|	1.5.6	|	2022-01-10	|	官方编译	|


-------------------------------------

## V0.7.6.0

### 发布时间： 2021.12.10

#### 添加功能 :
1. 更新OC版本至0.7.6并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.6
2. 更新官方编译的驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportItlwm-Monterey	|	2.1.0	|	2021-12-10	|	本地编译	|
|	AirportItlwm	|	2.1.0	|	2021-12-10	|	本地编译	|
|	AppleALC	|	1.6.7	|	2021-12-06	|	官方编译	|
|	FeatureUnlock	|	1.0.4	|	2021-12-06	|	官方编译	|
|	IntelBluetoothFirmware	|	2.1.0	|	2021-12-10	|	本地编译	|
|	IntelBluetoothInjector	|	2.1.0	|	2021-12-10	|	本地编译	|
|	Lilu	|	1.5.8	|	2021-12-06	|	官方编译	|
|	SMCBatteryManager	|	1.2.8	|	2021-12-06	|	官方编译	|
|	SMCDellSensors	|	1.2.8	|	2021-12-06	|	官方编译	|
|	SMCLightSensor	|	1.2.8	|	2021-12-06	|	官方编译	|
|	SMCProcessor	|	1.2.8	|	2021-12-06	|	官方编译	|
|	SMCSuperIO	|	1.2.8	|	2021-12-06	|	官方编译	|
|	VirtualSMC	|	1.2.8	|	2021-12-06	|	官方编译	|


-------------------------------------

## V0.7.5.0

### 发布时间： 2021.11.2

#### 添加功能 :
1. 更新OC版本至0.7.5并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.5
2. 更新官方编译的驱动：

| 驱动          | 版本号                        | 更新日期        | 更新方式         |
|:-------------|:-----------------------------|:---------------|:----------------|
|	AppleALC	|	1.6.6	|	2021-11-01	|	官方编译	|
|	BlueToolFixup	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmBluetoothInjector	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmFirmwareData	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmPatchRAM3	|	2.6.1	|	2021-11-01	|	官方编译	|
|	HibernationFixup	|	1.4.5	|	2021-11-01	|	官方编译	|
|	Lilu	|	1.5.7	|	2021-11-01	|	官方编译	|
|	Voodoo PS/2 Controller	|	2.2.7	|	2021-11-01	|	官方编译	|
|	WhateverGreen	|	1.5.5	|	2021-11-01	|	官方编译	|

-------------------------------------

## V0.7.4.3

### 发布时间： 2021.10.30

#### 添加的功能:
1. 完全支持``Thunderbult 3`` / ``Type-C ``端口 

#### 文件变化:

1. 添加了 ``TbtForcePower.efi``
2. 删除了 ``ACPI/SSDT-THUNDERBOLT`` 和 ``Kexts/IOElectrify.kext``
3. 将 ``USBMap.kext`` 替换为 ``USBPorts.kext``
4. 编辑了 ``config.plist`` 和 ``config-Intel-wirelss-card``

-----------------------------------------------------

## V0.7.4.2

#### 添加的功能:
1. 删除``config.plist``中无用的条目
2. 清理了OC引导主题文件夹
3. 添加了``Linux``引导(支持``Ext4`` / ``Btrfs``)
4. 添加了个性化的引导图标

#### 文件变化:

1. 添加了 ``btrfs_x64.efi`` 和 ``ext4_x64.efi``
2. 删除了 ``Resources/image/blackosx/BsxImacYellow``
3. 编辑了 ``config.plist`` 和 ``config-Intel-wirelss-card``