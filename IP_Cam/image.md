
## usefull links

Unpacking, editing and packaging of firmware of DVRs and IP cameras  
https://sudonull.com/post/115122-Unpacking-editing-and-packaging-of-firmware-of-DVRs-and-IP-cameras-from-Xiong-Mai

GNU / Linux und ein Rockchip 2918-Gerät  
https://habr.com/en/post/147793/


## random commands
```bash
binwalk $binary
file $binary
dumpimage -l $image
```

## find

```bash
hexdump $file | grep ...
strings $file | grep ...
```

## remove uImage Header
when binwalkink ```romfs-x.cramfs.img``` we see an 64byte uImage header.

 We remove it to get only the cramfs filesystem
```bash
dd bs=1 skip=64 if=romfs-x.cramfs.img of=romfs-x.cramfs
```

file before offsetting
```bash
~ file romfs-x.cramfs.img
romfs-x.cramfs.img: u-boot legacy uImage, linux, Linux/ARM, OS Kernel Image (gzip),
1310656 bytes, Tue Jul  7 06:14:23 2020, 
Load Address: 0X1C0000, 
Entry Point: 0X300000, 
Header CRC: 0XB7E2CEE1, 
Data CRC: 0X1C2CA334

~ binwalk romfs-x.cramfs.img
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             uImage header, header size: 64 bytes, header CRC: 0xB7E2CEE1, created: 2020-07-07 06:14:23, image size: 1310656 bytes, Data Address: 0x1C0000, Entry Point: 0x300000, data CRC: 0x1C2CA334, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: gzip, image name: "linux"
64            0x40            CramFS filesystem, little endian, size: 1179648, version 2, sorted_dirs, CRC 0xAE6C99C6, edition 0, 601 blocks, 160 files
```

file after offsetting
```bash
~ file romfs-x.cramfs
romfs-x.cramfs: Linux Compressed ROM File System data, little endian size 1179648 version \#2 
sorted_dirs CRC 0xae6c99c6, edition 0, 601 blocks, 160 files

~ binwalk romfs-x.cramfs 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             CramFS filesystem, little endian, size: 1179648, version 2, sorted_dirs, CRC 0xAE6C99C6, edition 0, 601 blocks, 160 files
```

## edit cramfs

```bash
sudo mkdir /hack/cramfs
#mount cramfs - its read only
sudo mount $cramfs_file /hack/cramfs
cd /hack/cramfs
#to edit we must copy the tree
sudo find ~+ > /tmp/filelist.txt
cat /tmp/filelist.txt | cpio -pdm /hack/cramfs-new
```
now edit the files.
in this case only ```ttyS000``` to ```ttyAMA0``` in ```/etc/inittab``` to get the rootshell over serial.

## repack image
```bash
#repack
mkcramfs $modified_root_dir romfs-x.mod.cramfs
```

the new cramfs filesystem looks like
```bash
~ binwalk romfs-x.mod.cramfs 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             CramFS filesystem, little endian, size: 1179648, version 2, sorted_dirs, CRC 0x61099993, edition 0, 601 blocks, 160 files
```
DIFF CRC ```0xAE6C99C6``` to ```0x61099993```  
DIFF FILESIZE ```1310656``` to ```1179648```

before packing we need the load and entrypoint adress from ```file romfs-x.cramfs.img```.
```bash 
Load Address: 0X1C0000, 
Entry Point: 0X300000, 
```
edit mkimage command to match the adresses
```bash
mkimage -A arm -O linux -T ramdisk -n "linux" -e 0x00300000 -a 0x001C0000 -d romfs-x.mod.cramfs romfs-x.mod.cramfs.img

Image Name:   linux
Created:      Sat Jan  8 15:21:27 2022
Image Type:   ARM Linux RAMDisk Image (gzip compressed)
Data Size:    1179648 Bytes = 1152.00 KiB = 1.12 MiB
Load Address: 001c0000
Entry Point:  00300000

~ file
romfs-x.mod.cramfs.img: u-boot legacy uImage, linux, Linux/ARM, RAMDisk Image (gzip), 
1179648 bytes, Sat Jan  8 14:21:27 2022, 
Load Address: 0X1C0000, 
Entry Point: 0X300000, 
Header CRC: 0XE93051B0, 
Data CRC: 0X6D58C572
```

now move all modified and unmodified files to a new folder and zip everyting to and "binary"
```bash
zip -D -X firmware.bin *
```

## print 64byte headers

```bash
xxd export/padded/header/romfs-x.header                                                                                                                                                                                               INT ✘  embedded_hacking  
00000000: 2705 1956 b7e2 cee1 5f04 12bf 0013 ffc0  '..V...._.......
00000010: 001c 0000 0030 0000 1c2c a334 0502 0201  .....0...,.4....
00000020: 6c69 6e75 7800 0000 0000 0000 0000 0000  linux...........
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................

xxd export/padded/header/uImage.header                                                                                                                                                                                                    ✔  embedded_hacking  
00000000: 2705 1956 213e 485c 5f04 12bf 0017 ffc0  '..V!>H\_.......
00000010: 0004 0000 001c 0000 df49 9ef6 0502 0201  .........I......
00000020: 6c69 6e75 7800 0000 0000 0000 0000 0000  linux...........
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................

xxd export/padded/header/user-x.header                                                                                                                                                                                                    ✔  embedded_hacking  
00000000: 2705 1956 72c4 ac26 5f04 12bf 0046 ffc0  '..Vr..&_....F..
00000010: 0030 0000 0077 0000 8009 0ff5 0502 0201  .0...w..........
00000020: 6c69 6e75 7800 0000 0000 0000 0000 0000  linux...........
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................

xxd export/padded/header/custom-x.header                                                                                                                                                                                                  ✔  embedded_hacking  
00000000: 2705 1956 52a6 68a5 5f04 12bc 0003 ffc0  '..VR.h._.......
00000010: 0077 0000 007b 0000 ba11 cce2 0502 0101  .w...{..........
00000020: 6c69 6e75 7800 0000 0000 0000 0000 0000  linux...........
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................

```