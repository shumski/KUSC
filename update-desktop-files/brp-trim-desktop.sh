#! /bin/sh

# macro: suse_update_desktop_file
#
#     Used to add easily a category to .desktop files according to XDG
#     standard.
#

#
# find file
#
BASEDIR=`dirname $RPM_SOURCE_DIR`/OTHER

if ! test -f /.buildenv; then
   # this looks fishy, skip it
   echo "WARNING: I better not trim without a /.buildenv around"
   exit 0
fi

if ! test -w $BASEDIR; then
   echo "WARNING: Can't write to $BASEDIR, skipping"
   exit 0
fi

find /$RPM_BUILD_ROOT/opt/kde3/share/applications/kde/ \
  /$RPM_BUILD_ROOT/opt/kde3/share/applnk/ \
  /$RPM_BUILD_ROOT/usr/share/xsessions/ \
  /$RPM_BUILD_ROOT/usr/share/applications/ \
  /$RPM_BUILD_ROOT/usr/share/mimelnk/ \
  /$RPM_BUILD_ROOT/usr/share/gnome/apps/ \
  /$RPM_BUILD_ROOT/etc/xdg/autostart/ -name *.desktop -o -name .directory 2>/dev/null | while read FILE; do

	if grep -q ^X-SuSE-translate= "$FILE"; then
	   echo "DEBUG: $FILE contains X-SuSE-translate - skipping" >&2
	   continue
	fi

	# save for backup 
	NFILE=${FILE#$RPM_BUILD_ROOT}
	echo "<<$NFILE>>" >> $BASEDIR/$RPM_PACKAGE_NAME.desktopfiles
	cat $FILE >> $BASEDIR/$RPM_PACKAGE_NAME.desktopfiles
	echo "trimmed output to $BASEDIR/$RPM_PACKAGE_NAME.desktopfiles"

	#
	# Trim translations (desktops will use gettext to find them)
	#
	grep -v -E '^Name\[|^GenericName\[|^Comment\[' $FILE > ${FILE}_ 
	sed -i -e '/^\[Desktop Entry\]/a \
X-SuSE-translate=true' ${FILE}_
	mv ${FILE}_ $FILE

done

