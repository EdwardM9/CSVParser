"""
CSV Parsing Utility

Takes in parsed data from a CSV file and renders it onto a chart.
Prefers rendering simple data, such as sets of plot points. More
complex charting can be done, but it requires custom scripting for
each specialized chart.

Main class for creating the View of the application.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import wx
import filebrowserpanel as fbp
import plotpanel as pp
import parse as p

APP_HEIGHT = 805
APP_WIDTH = 550

class ParseFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(ParseFrame, self).__init__(*args, **kwargs)
		self.initialize()    
		self.Show()

	def initialize(self):
		"""
		Creates the application's interface.
		"""
		self.create_menu()
		self.create_interface()
		self.Center()

	def create_interface(self):
		"""
		Populates the interface with all necessary elements.
		"""
		self.sizer = wx.BoxSizer(wx.VERTICAL)

		#File browser
		self.fbPanel = fbp.FileBrowsePanel(self)
		sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer2.Add(self.fbPanel, wx.ALIGN_TOP, wx.EXPAND)
		gButton = wx.Button(self, label='Use File')
		gButton.Bind(wx.EVT_BUTTON, self.get_path)
		sizer2.Add(gButton, wx.ALIGN_RIGHT, wx.SHAPED)
		
		#Charting area
		self.plotPanel = pp.PlotPanel(self)
		self.gsizer = wx.GridBagSizer(5,8)
		self.gsizer.Add(self.plotPanel, pos = (2,2), span = (6,6))
		
		#Preferences
		self.cb = wx.ComboBox(self, style=wx.CB_READONLY)
		cbLabel = wx.StaticText(self, label = "X-Axis")
		self.genButton = wx.Button(self, label="Generate Chart")
		self.genButton.Bind(wx.EVT_BUTTON, self.generate_chart)
		self.gsizer.Add(cbLabel, pos = (2,8), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT)
		self.gsizer.Add(self.cb, pos = (3,8), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT)
		self.gsizer.Add(self.genButton, pos = (8,8), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT)
		
		#Add them all to the main layout.
		self.sizer.Add(sizer2, wx.ALIGN_TOP, wx.EXPAND)
		self.sizer.Add(self.gsizer)
		self.SetSizer(self.sizer)
		self.SetAutoLayout(True)
		self.SetSize((APP_HEIGHT, APP_WIDTH))

	def create_menu(self):
		"""
		Simple menu for quitting the application with a shortcut.
		"""
		menubar = wx.MenuBar()
		self.SetMenuBar(menubar)

	def get_path(self, e):
		"""
		Retrieves the file's path, parses and uses it to populate the options.
		"""
		self.filePath = self.fbPanel.get_file_path()
		self.data, self.headers = p.parse(self.filePath, ",")
		self.cb.Clear()
		self.cb.AppendItems(self.headers)
		self.Layout()

	def generate_chart(self, e):
		"""
		Creates the chart based on the data provided.
		"""
		self.plotPanel.plot(self.data, self.cb.GetValue())

	def on_quit(self, e):
		"""
		Quit gracefully.
		"""
		self.Close()

if __name__ == '__main__':
  
    app = wx.App()
    ParseFrame(None, title='CSV Charting Utility')
    app.MainLoop()