"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""
import wx
import wx.lib
from wx.lib import filebrowsebutton
import matplotlib
from matplotlib import numpy
from numpy import arange, sin
import wxmpl
class PlotPanel(wx.Panel):
	def __init__(self, *args, **kwargs):
		super(PlotPanel, self).__init__(*args, **kwargs)
		self.create_panel()

	def create_panel(self):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.ppanel = wxmpl.PlotPanel(self, 123)#, size = (12,7))
		sizer.Add(self.ppanel, wx.ALIGN_CENTER, wx.EXPAND)

	def plot(self):
		x = arange(0.0, 2, .01)
		y = sin(1.2*x)
		fig = self.ppanel.get_figure()
		axes = fig.gca()
		axes.plot(x,y)
		self.ppanel.draw()