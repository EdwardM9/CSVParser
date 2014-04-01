"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import wx
import constants as c
import filebrowserpanel as fbp
class ParseFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(ParseFrame, self).__init__(*args, **kwargs)
		self.initialize()    
		self.Show()

	def initialize(self):
		self.create_menu()
		self.create_interface()
		self.Center()

	def create_interface(self):
		sizer = wx.BoxSizer(wx.VERTICAL)
		
		fbPanel = fbp.FileBrowsePanel(self)
		sizer.Add(fbPanel, wx.ALIGN_RIGHT, wx.EXPAND)
		
		self.SetSizer(sizer)

		self.SetSize((c.APP_HEIGHT, c.APP_WIDTH))

	def create_menu(self):
		menubar = wx.MenuBar()
		self.SetMenuBar(menubar)

	def on_quit(self, e):
		self.Close()

if __name__ == '__main__':
  
    app = wx.App()
    ParseFrame(None, title='CSV Charting Utility')
    app.MainLoop()