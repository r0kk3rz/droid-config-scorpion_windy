#!/bin/sh
/system/bin/macaddrsetup /sys/devices/platform/bcmdhd_wlan/macaddr
ifconfig wlan0 up

