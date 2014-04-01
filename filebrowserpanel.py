"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""
import wx

class FileBrowsePanel(wx.Panel):
	def __init__(self, *args, **kwargs):
		super(FileBrowsePanel, self).__init__(*args, **kwargs)
		bButton = wx.lib.filebrowsebutton.DirBrowseButton(self)
