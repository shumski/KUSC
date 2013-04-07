## KDE UNSTABLE ENVIRONMENT SETUP
##
## This is the runtime environment part. All variables that are only to
## be used at build time go to build_environment.rc
 
prepend() { [ -d "$2" ] && eval $1=\"$2\$\{$1:+':'\$$1\}\" && export $1 ; }

export KDEUNSTABLEDIR="/opt/kde-unstable"
export QTDIR=$KDEUNSTABLEDIR

## KDE
export KDEDIR=$QTDIR
prepend PATH $KDEDIR/bin
export PATH

export KDEHOME=$HOME/.kde-unstable/
export KDETMP=/tmp/kde-unstable-kde-$USER
export KDEVARTMP=/var/tmp/kde-unstable-kde-$USER
mkdir -p $KDETMP
mkdir -p $KDEVARTMP
prepend KDEDIRS $KDEDIR
export KDEDIRS

#prepend QT_PLUGIN_PATH
prepend QT_PLUGIN_PATH $KDEDIR/plugins
prepend QT_PLUGIN_PATH $KDEDIR/lib/qt4/plugins
prepend QT_PLUGIN_PATH $KDEDIR/lib/kde4/plugins
prepend QML_IMPORT_PATH $KDEDIR/lib/kde4/imports

prepend LD_LIBRARY_PATH $KDEDIR/lib
export LD_LIBRARY_PATH
prepend PKG_CONFIG_PATH $KDEDIR/lib/pkgconfig
export PKG_CONFIG_PATH

export CMAKE_PREFIX_PATH=$KDEDIR
export CMAKE_INSTALL_PREFIX=$KDEDIR
export CMAKE_LIBRARY_PATH=$KDEDIR/lib
export CMAKE_INCLUDE_PATH=$KDEDIR/include
prepend PYTHONPATH $KDEDIR/lib64/python2.7/site-packages
export PYTHONPATH

export QT_PLUGIN_PATH

## Make manpages from kde-unstable visible
export MANPATH=/opt/kde-unstable/share/man/:$MANPATH

## XDG
## put these seperate, needed for e.g. akonadi
mkdir -p $KDEHOME/local/share
export XDG_DATA_HOME=$KDEHOME/local/share
mkdir -p $KDEHOME/config
export XDG_CONFIG_HOME=$KDEHOME/config
mkdir -p $KDEHOME/cache
export XDG_CACHE_HOME=$KDEHOME/cache
export XDG_DATA_DIRS=$KDEDIR/share:/usr/local/share:/usr/share

 
## make the debug output prettier
export KDE_COLOR_DEBUG=1
export QTEST_COLORED=1

