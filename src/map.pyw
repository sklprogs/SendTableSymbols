#encoding:utf-8
# cmd: chcp 65001

import tkinter as tk
import os, sys
from constants import *
from shared import h_os, h_lang, Message, Path, ReadTextFile, Config
from sharedGUI import Root, SymbolMap
import sendkeysctypes as sendkeys

class ConfigMap(Config):
	
	def __init__(self):
		super().__init__()
		self.sections = [SectionVariables]
		self.sections_abbr = [SectionVariables_abbr]
		self.sections_func = [config_parser.get]
		self.message = globs['mes'].missing_config + '\n'
		self.total_keys = 0
		self.changed_keys = 0
		self.missing_keys = 0
		self.missing_sections = 0
		# Create these keys before reading the config
		globs['bin_dir'] = Path(os.path.realpath(sys.argv[0])).dirname()
		self.path = globs['bin_dir'] + os.path.sep + 'map.cfg'
		self.reset()
		h_read = ReadTextFile(self.path,Silent=self.Silent)
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
		globs['var'].update({
			'spec_syms':'àáâäāæßćĉçèéêēёëəғĝģĥìíîïīĵķļñņòóôõöōœøšùúûūŭũüýÿžжҗқңөүұÀÁÂÄĀÆSSĆĈÇÈÉÊĒЁËƏҒĜĢĤÌÍÎÏĪĴĶĻÑŅÒÓÔÕÖŌŒØŠÙÚÛŪŬŨÜÝŸŽЖҖҚҢӨҮҰ',
			'ui_lang':'ru'
					   })
	
	def reset(self):
		globs['var'] = {}



class WinTray: # Requires h_root, h_map

	def __init__(self):
		if h_os.sys() == 'win':
			h_root.widget.tk.call('package', 'require', 'Winico')
			icon = h_root.widget.tk.call('winico', 'createfrom', os.path.join(os.getcwd(), 'map.ico'))
			h_root.widget.tk.call('winico', 'taskbar', 'add', icon,
						 '-callback', (h_root.widget.register(self.menu_func), '%m', '%x', '%y'),
						 '-pos',0,
						 '-text',u'Character Map') # todo: product name
			self.menu = tk.Menu(h_root.widget,tearoff=0)
		else:
			Message(func='WinTray.__init__',type=lev_err,message=globs['mes'].not_crossplatform)
			h_root.destroy()

	def menu_func(self,event,x,y):
		if event == 'WM_RBUTTONDOWN':
			h_root.widget.quit() # Destroy throws an error
		elif event == 'WM_LBUTTONDOWN':
			self.map()
		
	def map(self):
		result = h_map.get()
		for sym in result:
			keys = sendkeys.parse_keys(sym,with_newlines = True)
		for key in keys:
			key.Run()


h_root = Root()
h_root.close()
ConfigMap()
h_lang.set()
h_map = SymbolMap(parent_obj=h_root)
h_tray = WinTray()
h_root.run()
