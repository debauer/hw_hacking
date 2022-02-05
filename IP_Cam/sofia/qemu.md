### run sofia

```bash 
cd $filesystem_root
qemu-arm -L . usr/bin/Sofia
```

### output
```bash
LIBDVR : FILE -> src/init/ver.c, LINE -> 145: Can't build /tmp/lockfile
LIBHICAP: Complied at May 26 2020 15:39:08 GIT:c0ba0b9
SampleSysInit enter, May 26 2020, 15:39:08
May 27 2020 16:56:43 ==>XMJSON_ParseViV2(267): Get ViV2 object error!
Parse File succeed!
Vi: sensorFPS=[25, 25], capW=1920,capH=1080,capX=0,capY=0
ViChn  ImageSize TitleMagn
   0      14       0
   1       0       0
Venc: vencTypes=07
VencChn MaxSize SupportSizes
     0       14         4800
     1        0            9
Audio: playEnable=1
LIBDVR : FILE -> src/misc/env.c, LINE -> 143: Open Mtd0 Failed
[1]    191741 segmentation fault (core dumped)  qemu-arm usr/bin/Sofia


```


```bash
qemu-system-arm -m 256 -M virt -nographic \
 -device nand,chip_id=0x59,id=myflash \
 -drive if=mtd,format=raw,file=firmware.bin,id=myflash \


```