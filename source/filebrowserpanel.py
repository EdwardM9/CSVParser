"""
CSV Parsing Utility

Takes in parsed data from a CSV file and renders it onto a chart.
Prefers rendering simple data, such as sets of plot points. More
complex charting can be done, but it requires custom scripting for
each specialized chart.

FileBrowsePanel contains the button that allows the user to locate a CSV
file.

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
		"""
		Creates and configures the panel.
		"""
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.bButton = wx.lib.filebrowsebutton.FileBrowseButton(self, 
			labelText = "Find the path to a .CSV file:", 
			fileMask = "*.csv", size = (680, -1))

	def get_file_path(self):
		"""
		Accessor for the file path as chosen by the user.
		"""
		return self.bButton.GetValue()
