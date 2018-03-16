#!/bin/sh

# Do not use "verbose" in order to spot errors easily

# Remove shared resources
rm -f ./resources/{error.gif,info.gif,question.gif,warning.gif}

# Remove other SendTableSymbols resources
rm -f ./resources/locale/ru/LC_MESSAGES/SendTableSymbols.mo
rm -f ./resources/third\ parties
rm -f ./user/SendTableSymbols.cfg

# Remove SendTableSymbols Python files
rm -f ./{sendkeysctypes,SendTableSymbols}.py

# Remove shared Python files
rm -f ./{gettext_windows.py,shared.py,sharedGUI.py}

# (Wine-only) Remove SendTableSymbols icon
rm -f ./resources/SendTableSymbols.ico

# (Wine-only) Remove build scripts
rm -f ./{build.sh,clean_up.sh,SendTableSymbols.cmd,setup.py}

rmdir -p resources/locale/ru/LC_MESSAGES user

ls .
