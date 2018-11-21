Name: jolla-configuration-shinano
Summary: Jolla Configuration shinano
Version: 0.0.1
Release: 1
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz
Requires: patterns-sailfish-applications
Requires: patterns-sailfish-ui

# Early stages of porting benefit from these:
#Requires: sailfish-porter-tools

# Jolla Store Items
Requires: patterns-sailfish-consumer-generic


Requires: sailfish-content-graphics-z1.25
Requires: jolla-settings-accounts-extensions-3rd-party-all

# For Mozilla location services (online)
Requires: geoclue-provider-mlsdb

 # Sailfish OS CSD tool for hardware testing
Requires: csd
%description
Pattern with packages for shinano configurations
%files
