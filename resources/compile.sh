#!/usr/bin/env bash

GLADE_ROOT_DIRECTORY=".."
GLADE_MODULE_DIRECTORY="$GLADE_ROOT_DIRECTORY/glade"
RESOURCE_INPUT="resources.qrc"
RESOURCE_OUTPUT="resources.py"

echo "Compiling resources file: $RESOURCE_INPUT";
pyside-rcc $RESOURCE_INPUT -o $RESOURCE_OUTPUT

echo "Moving into glade module directory..."
mv $RESOURCE_OUTPUT "$GLADE_MODULE_DIRECTORY/ui/$RESOURCE_OUTPUT"
echo "Done!"


