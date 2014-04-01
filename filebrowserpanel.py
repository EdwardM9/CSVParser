"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""
import wx
import wx.lib
from wx.lib import filebrowsebutton

class FileBrowsePanel(wx.Panel):
	def __init__(self, *args, **kwargs):
		super(FileBrowsePanel, self).__init__(*args, **kwargs)
		self.create_panel()

	def create_panel(self):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.bButton = wx.lib.filebrowsebutton.FileBrowseButton(self, 
			labelText = "Find the path to a .CSV file:", 
			fileMask = "*.csv", size = (1050, -1))

	def get_file_path(self):
		return self.bButton.GetValue()
