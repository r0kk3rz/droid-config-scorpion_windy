# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device scorpion_windy
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia Z3 Tablet Compact

%define dcd_path ./

%define pixel_ratio 1.25

%define remove_modem 1
%define community_adaptation 1

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
