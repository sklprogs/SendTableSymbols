SendTableSymbols is a program that allows to send special symbols (like àáâæßç) to an external application. Launch the program (map.exe), click on a tray icon, select a special symbol - this symbol will be pasted into the program that is open right in front of you. Right click on a tray icon to quit.

You can add additional characters by editing map.cfg. Use specialized editors such as AkelPad (akelpad.sourceforge.net) to edit map.cfg, do not preserve BOM when saving - otherwise, reading the config file will fail.

Only Windows is currently supported (because of such components as SendKeys and winico). To run as a script, copy winico0.6 to tcl folder, e.g. C:\Python34\tcl\winico0.6\.

Enjoy :-)
