## boot

```bash 
U-Boot 2014.04 (Nov 18 2019 - 10:37:35)

CPU: XM530
DRAM:  64 MiB


U-Boot 2014.04 (Nov 18 2019 - 10:37:35)

CPU: XM530
DRAM:  64 MiB
MMC:   arasan: 0
In:    serial
Out:   serial
Err:   serial
Net:   dwmac.10010000
Press Ctrl+C to stop autoboot
```

## help


```bash 
U-Boot> help
?       - alias for 'help'
base    - print or set address offset
bdinfo  - print Board Info structure
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootm   - boot application image from memory
bootp   - boot image via network using BOOTP/TFTP protocol
cmp     - memory compare
coninfo - print console devices and information
cp      - memory copy
cramfsload- load binary file from a filesystem image
cramfsls- list files in a directory (default /)
crc32   - checksum calculation
dhcp    - boot image via network using DHCP/TFTP protocol
echo    - echo args to console
editenv - edit environment variable
env     - environment handling commands
fatinfo - print information about filesystem
fatload - load binary file from a dos filesystem
fatls   - list files in a directory (default /)
flwrite - SPI flash sub-system
go      - start application at address 'addr'
help    - print command description/usage
imxtract- extract a part of a multi-image
itest   - return true/false on integer compare
loadb   - load binary file over serial line (kermit mode)
loadx   - load binary file over serial line (xmodem mode)
loady   - load binary file over serial line (ymodem mode)
loop    - infinite loop on address range
md      - memory display
mm      - memory modify (auto-incrementing address)
mmc     - MMC sub system
mmcinfo - display MMC info
mw      - memory write (fill)
nfs     - boot image via network using NFS protocol
nm      - memory modify (constant address)
ping    - send ICMP ECHO_REQUEST to network host
printenv- print environment variables
reset   - Perform RESET of the CPU
run     - run commands in an environment variable
saveenv - save environment variables to persistent storage
setenv  - set environment variables
setexpr - set environment variable as the result of eval expression
sf      - SPI flash sub-system
sleep   - delay execution for some time
source  - run script from memory
tftpboot- boot image via network using TFTP protocol
version - print monitor, compiler and linker version

```

##version 

```bash
U-Boot> version

U-Boot 2014.04 (Nov 18 2019 - 10:37:35)
arm-linux-gcc (Buildroot 2014.08) 4.9.2
GNU ld (GNU Binutils) 2.24
```


## printenv

```bash 
appCloudExAbility=5rMyqrbDYq0=
appProducerID=000
baudrate=115200
bootargs=mem=36M init=/bin/ash console=ttyAMA0,115200 root=/dev/mtdblock2 rootfstype=cramfs mtdparts=xm_sfc:256K(boot),1536K(kernel),1280K(romfs),4544K(user),256K(custom),320K(mtd)
bootcmd=sf probe 0;sf read 80007fc0 40000 180000;bootm 80007fc0
bootdelay=1
cramfsaddr=0x60040000
da=mw.b 0x81000000 ff 800000;tftp 0x81000000 u-boot.bin.img;sf probe 0;flwrite
dc=mw.b 0x81000000 ff 800000;tftp 0x81000000 custom-x.cramfs.img;sf probe 0;flwrite
dd=mw.b 0x81000000 ff 800000;tftp 0x81000000 mtd-x.jffs2.img;sf probe 0;flwrite
dr=mw.b 0x81000000 ff 800000;tftp 0x81000000 romfs-x.cramfs.img;sf probe 0;flwrite
du=mw.b 0x81000000 ff 800000;tftp 0x81000000 user-x.cramfs.img;sf probe 0;flwrite
dw=mw.b 0x81000000 ff 800000;tftp 0x81000000 web-x.cramfs.img;sf probe 0;flwrite
ethact=dwmac.10010000
ethaddr=00:12:41:5e:c4:b5
ipaddr=192.168.1.10
netmask=255.255.255.0
serverip=192.168.1.107
stderr=serial
stdin=serial
stdout=serial
tk=mw.b 0x81000000 ff 800000;tftp 0x81000000 uImage; bootm 0x81000000
ua=mw.b 0x81000000 ff 800000;tftp 0x81000000 upall_verify.img;sf probe 0;flwrite
up=mw.b 0x81000000 ff 800000;tftp 0x81000000 update.img;sf probe 0;flwrite
verify=n

Environment size: 1273/65532 bytes
```