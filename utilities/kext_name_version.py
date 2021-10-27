import os
import sys
import time
from biplist import *

os.chdir(sys.path[0])
root = os.path.abspath('..')
kext_name = []
kext_version = []
kext_time = []
kext_type = []
for kext in os.listdir(os.path.join(root,'EFI/OC/Kexts')):
    if kext == ".DS_Store":
        continue
    domain = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts'))
    kext_full = os.path.join(domain, kext)
    plist = os.path.join(kext_full, 'Contents/Info.plist')
    k_time = os.stat(plist).st_mtime
    k_time = time.strftime('%Y-%m-%d', time.localtime(k_time))
    kext_time.append(k_time)
    plist = readPlist(plist)
    kext_name.append(plist['CFBundleName'])
    kext_version.append(plist['CFBundleVersion'])
    if kext == 'USBMap.kext':
        kext_type.append('USB Ports Inject')
        continue
    if plist['BuildMachineOSBuild'] == '21A5304g':
        kext_type.append('Compile on Local Machine')
    else:
        kext_type.append('Official Release')
for i in range(len(kext_name)):
    for j in range(len(kext_name)-i-1):
        if kext_name[j] > kext_name[j+1]:
            temp1 = kext_name[j+1]
            temp2 = kext_version[j+1]
            temp3 = kext_time[j+1]
            temp4 = kext_type[j+1]
            kext_name[j+1] = kext_name[j]
            kext_version[j+1] = kext_version[j]
            kext_time[j+1] = kext_time[j]
            kext_type[j+1] = kext_type[j]
            kext_name[j] = temp1
            kext_version[j] = temp2
            kext_time[j] = temp3
            kext_type[j] = temp4
file = open('kexts.txt', 'w')
for i in range(len(kext_name)):
    str = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type[i] + '\t|\n'
    file.write(str)