"""
CSV Parsing Utility

Takes in parsed data from a CSV file and renders it onto a chart.
Prefers rendering simple data, such as sets of plot points. More
complex charting can be done, but it requires custom scripting for
each specialized chart.

PlotPanel is a simple panel that integrates wxmpl's PlotPanel to 
draw and render onto a matplotlib set of axes.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""
import wx
import wxmpl

class PlotPanel(wx.Panel):
	def __init__(self, *args, **kwargs):
		super(PlotPanel, self).__init__(*args, **kwargs)
		self.create_panel()

	def create_panel(self):
		"""
		Creates and configures the plot panel.
		"""
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.ppanel = wxmpl.PlotPanel(self, 123)
		sizer.Add(self.ppanel, wx.ALIGN_CENTER, wx.EXPAND)

	def plot(self, data, title):
		"""
		Creates a line, plots it into the wxmpl.PlotPanel and
		 renders it.
		"""
		fig = self.ppanel.get_figure()
		axes = fig.gca()
		values = []
		for item in data:
			values.append(item.get(title))
		axes.plot(values)

		#Force redraw update
		self.ppanel.draw()