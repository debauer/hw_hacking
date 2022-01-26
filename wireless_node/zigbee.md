
https://www.zigbee2mqtt.io/advanced/zigbee/04_sniff_zigbee_traffic.html  
http://blog.antiblau.de/2018/10/24/ssh-remote-capture-mit-wireshark/


### zigbee2mqtt

https://www.zigbee2mqtt.io/guide/getting-started/


### pyCCSniffer

https://github.com/andrewdodd/pyCCSniffer

```bash
git clone https://github.com/andrewdodd/pyCCSniffer
cd pyCCSniffer
python pyCCSniffer
```


### whsniff

https://github.com/homewsn/whsniff

```bash
curl -L https://github.com/homewsn/whsniff/archive/v1.3.tar.gz | tar zx
cd whsniff-1.3
make
sudo make install
```

```bash 
whsniff -c 18 > whsniff-log.pcap
tshark -r whsniff-log.pcap
tshark -r whsniff-log.pcap -V
```

### lidl zigbee gateway

Channel: 15

https://www.lidl.de/p/silvercrest-gateway-zigbee-smart-home-sgwz-1-a1/p100335204  
https://paulbanks.org/projects/lidl-zigbee/