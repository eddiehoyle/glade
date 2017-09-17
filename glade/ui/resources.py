# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Sun Sep 17 22:06:19 2017
#      by: The Resource Compiler for PySide (Qt v4.8.7)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_data = "\x00\x00\x015QFrame#sectionHeader {\x0a    background-color: \x22blue\x22;\x0a    margin: 0px;\x0a    padding: 5px;\x0a}\x0aQFrame#sectionBody {\x0a    background-color: \x22blue\x22;\x0a    margin: 0px;\x0a    padding: 5px;\x0a}\x0aQPushButton {\x0a    background-color: red;\x0a}\x0aQScrollArea {\x0a    background-color: orange;\x0a}\x0aQLineEdit {\x0a    background-color: green;\x0a}"
qt_resource_name = "\x00\x0b\x0ck<\xf3\x00s\x00t\x00y\x00l\x00e\x00s\x00h\x00e\x00e\x00t\x00s\x00\x09\x00(\xad#\x00s\x00t\x00y\x00l\x00e\x00.\x00q\x00s\x00s"
qt_resource_struct = "\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"
def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
