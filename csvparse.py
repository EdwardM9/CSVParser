"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import wx
import wx.lib
from wx.lib import filebrowsebutton
import constants as c
import filebrowserpanel as fbp
import plotpanel as pp

import parse as p
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

		self.fbPanel = fbp.FileBrowsePanel(self)
		sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer2.Add(self.fbPanel, wx.ALIGN_TOP, wx.EXPAND)
		gButton = wx.Button(self, label='Use File')
		gButton.Bind(wx.EVT_BUTTON, self.get_path)
		sizer2.Add(gButton, wx.ALIGN_RIGHT, wx.SHAPED)
		
		self.plotPanel = pp.PlotPanel(self)
		gsizer = wx.GridBagSizer(5,8)
		gsizer.Add(self.plotPanel, pos = (2,2), span = (6,6))
		self.cb = wx.ComboBox(self, style=wx.CB_READONLY)
		gsizer.Add(self.cb, pos = (2,8), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT)

		sizer.Add(sizer2, wx.ALIGN_TOP, wx.EXPAND)
		sizer.Add(gsizer)
		self.SetSizer(sizer)
		self.SetAutoLayout(True)
		self.SetSize((c.APP_HEIGHT, c.APP_WIDTH))

	def create_menu(self):
		menubar = wx.MenuBar()
		self.SetMenuBar(menubar)

	def get_path(self, e):
		self.filePath = self.fbPanel.get_file_path()
		self.data, self.headers = p.parse(self.filePath, ",")
		self.cb.Clear()
		self.cb.AppendItems(self.headers)

	def on_quit(self, e):
		self.Close()

if __name__ == '__main__':
  
    app = wx.App()
    ParseFrame(None, title='CSV Charting Utility')
    app.MainLoop()