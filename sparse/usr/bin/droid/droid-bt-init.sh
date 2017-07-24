#!/bin/sh
MAC_ADDR=`cat /data/etc/bluetooth_bdaddr`
echo "0" > /sys/class/rfkill/rfkill0/state
echo "1" > /sys/class/rfkill/rfkill0/state
echo " " > /dev/ttyHS0
hciattach /dev/ttyHS0 bcm43xx 115200 flow dbaddr $MAC_ADDR

