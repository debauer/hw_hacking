
mkdir export/origin -p
mkdir export/padded -p
mkdir export/header -p
mkdir export/files/combined -p


unzip -u firmware.bin -d export/origin 

for value in "romfs-x" "custom-x" "user-x" "user-x"
do
    dd bs=1 skip=64 if=export/origin/$value.cramfs.img of=export/padded/$value.cramfs
    dd bs=1 count=64 if=export/origin/$value.cramfs.img of=export/header/$value.header
done
dd bs=1 skip=64 if=export/origin/uImage.img of=export/padded/uImage
dd bs=1 count=64 if=export/origin/uImage.img of=export/header/uImage.header

cp export/origin/u-boot.env.img export/padded -f
cp export/origin/u-boot.bin.img export/padded -f
cp export/origin/InstallDesc export/padded -f


for value in "romfs-x" "custom-x" "user-x"
do
    # mount and create folders
    mkdir /tmp/cramfs-mount -p
    sudo mount export/padded/$value.cramfs /tmp/cramfs-mount
    mkdir /tmp/cramfs-export -p
    
    cd /tmp/cramfs-mount
    echo ""
    echo "sudo find ~+ > /tmp/$value.filelist.txt"
    find ~+ > /tmp/$value.filelist.txt
    
    echo ""
    echo "cat /tmp/$value.filelist.txt  | cpio -pdm /tmp/cramfs-export"
    cat /tmp/$value.filelist.txt  | cpio -pdm /tmp/cramfs-export
    
    echo ""
    cd -
    cp /tmp/$value.filelist.txt export/$value.filelist.txt 
    mkdir export/files/$value
    cp /tmp/cramfs-export/tmp/cramfs-mount/* export/files/$value -RP
    
    #cleanup
    sudo umount /tmp/cramfs-mount
    sudo rm /tmp/cramfs-export -R
    sudo rm /tmp/cramfs-mount -R
done

cp export/files/romfs-x/* export/files/combined -R 
cp export/files/user-x/* export/files/combined/usr -R 
cp export/files/custom-x/* export/files/combined/mnt/custom -R 