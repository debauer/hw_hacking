qemu-system-arm -m 256 -M virt \
 -kernel export/padded/uImage \
 -serial mon:stdio \
 -append 'console=ttyS0'