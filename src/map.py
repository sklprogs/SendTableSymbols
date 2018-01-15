#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# cmd: chcp 65001

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('map','./locale')

import tkinter as tk
import os, sys
import shared as sh
import sharedGUI as sg

if sh.oss.win():
    import sendkeysctypes as sendkeys


class ConfigMap(sh.Config):
    
    def __init__(self):
        super().__init__()
        self.path = sh.objs.pdir().add('map.cfg')
        self.reset()
        h_read = sh.ReadTextFile(self.path,Silent=self.Silent)
        self.text = h_read.get()
        self.Success = h_read.Success
        self._default()
        if os.path.exists(self.path):
            self.open()
        else:
            self.Success = False
        self.check()
        self.load()
            
    def _default(self):
        sh.globs['var'].update ({
            'spec_syms':'àáâäāæßćĉçèéêēёëəғĝģĥìíîïīĵķļñņòóôõöōœøšùúûūŭũüýÿžжҗқңөүұÀÁÂÄĀÆSSĆĈÇÈÉÊĒЁËƏҒĜĢĤÌÍÎÏĪĴĶĻÑŅÒÓÔÕÖŌŒØŠÙÚÛŪŬŨÜÝŸŽЖҖҚҢӨҮҰ'
                               })
    
    def reset(self):
        sh.globs['var'] = {}



class WinTray:

    def __init__(self):
        if sh.oss.win():
            sg.objs.root().widget.tk.call('package', 'require', 'Winico')
            icon = sg.objs.root().widget.tk.call ('winico',
                                                  'createfrom',
                                                  os.path.join(os.getcwd(),'map.ico')
                                                 )
            #todo: product name
            sg.objs.root().widget.tk.call ('winico','taskbar','add',icon
                                          ,'-callback'
                                          ,(sg.objs.root().widget.register(self.menu_func)
                                          ,'%m','%x','%y'),'-pos',0
                                          ,'-text','Character Map'
                                          )
            self.menu = tk.Menu(sg.objs.root().widget,tearoff=0)
            ''' For some reason, 'self.menu.pack' is useless and does
                not work as expected
            '''
        else:
            sg.Message (func    = 'WinTray.__init__'
                       ,level   = _('ERROR')
                       ,message = _('This operation cannot be executed on your operating system.')
                       )

    def menu_func(self,event,x,y):
        if event == 'WM_RBUTTONDOWN':
            # 'destroy' throws an error
            sg.objs.root().widget.quit()
        elif event == 'WM_LBUTTONDOWN':
            self.map()
        
    def map(self):
        result = objs.map().get()
        for sym in result:
            keys = sendkeys.parse_keys(sym,with_newlines=True)
        for key in keys:
            key.Run()



class Objects:
    
    def __init__(self):
        self._map = None
        
    def map(self):
        if not self._map:
            self._map = sg.SymbolMap(parent=sg.objs.root())
        return self._map


if __name__ == '__main__':
    objs = Objects()
    ConfigMap()
    WinTray()
    sg.objs.root().run()
