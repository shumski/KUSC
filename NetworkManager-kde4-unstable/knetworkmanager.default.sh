kdehome=$HOME/.kde4
test -n "$KDEHOME" && kdehome=`echo "$KDEHOME"|sed "s,^~/,$HOME/,"`

configfile=$kdehome/share/config/networkmanagementrc
knetworkmanager_autostart=
if test ! -f $configfile; then
    knetworkmanager_autostart=$(. /etc/sysconfig/network/config && echo "$NETWORKMANAGER")
elif test $configfile -ot  /etc/sysconfig/network/config; then
    knetworkmanager_autostart=$(. /etc/sysconfig/network/config && echo "$NETWORKMANAGER")
fi

# kconfig will merge it in case we overwrite another setting
if test -n "$knetworkmanager_autostart"; then
    mkdir -p $kdehome/share/config
    echo "[General]" >> $configfile
    case "$knetworkmanager_autostart" in
     no)
	knetworkmanager_autostart=false
	;;
     yes)
	knetworkmanager_autostart=true
        ;;
    esac
    echo "Autostart=$knetworkmanager_autostart" >> $configfile
fi
