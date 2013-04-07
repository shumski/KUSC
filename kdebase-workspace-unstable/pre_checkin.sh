#!/bin/bash
# This script is called automatically during autobuild checkin.

version=$(grep '^Version:.*' kdebase4-workspace.spec)
for change in python-kdebase4; do
    cp -f kdebase4-workspace.changes $change.changes
    sed -i -e "s,Version:.*,$version," ${change}.spec
done
