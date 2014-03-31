"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'simple.py')
frame.Show()

app.MainLoop()

if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()