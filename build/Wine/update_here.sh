#!/bin/bash

# Do not use "verbose" in order to spot errors easily

mkdir -p ./resources/locale/ru/LC_MESSAGES/
mkdir ./user

# Copy shared resources
cp -u $HOME/bin/shared/resources/{error.gif,info.gif,question.gif,warning.gif} ./resources/

# Copy other SendTableSymbols resources
cp -u $HOME/bin/SendTableSymbols/resources/locale/ru/LC_MESSAGES/SendTableSymbols.mo ./resources/locale/ru/LC_MESSAGES/
cp -u $HOME/bin/SendTableSymbols/resources/third\ parties ./resources/
cp -u $HOME/bin/SendTableSymbols/user/SendTableSymbols.cfg ./user/

# Copy SendTableSymbols Python files
cp -u $HOME/bin/SendTableSymbols/src/{sendkeysctypes,SendTableSymbols}.py .

# Copy shared Python files
cp -u $HOME/bin/shared/src/{gettext_windows.py,shared.py,sharedGUI.py} .

# (Wine-only) Copy SendTableSymbols icon
cp -ru /home/pete/bin/SendTableSymbols/resources/SendTableSymbols.ico ./resources/

# (Wine-only) Copy build scripts
cp -u $HOME/bin/SendTableSymbols/build/Wine/{build.sh,clean_up.sh,SendTableSymbols.cmd,setup.py} .

ls .
