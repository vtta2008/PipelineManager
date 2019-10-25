# -*- coding: utf-8 -*-
"""

Script Name: Widget.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------

from PyQt5.QtWidgets import QWidget


from ui.UiSignals import UiSignals
from utils.utils import get_layout_size

class Widget(QWidget):

    def __init__(self, preset={}, parent=None):
        QWidget.__init__(self)

        self.preset = preset
        self.parent = parent
        self.signals = UiSignals(self)

    def moveEvent(self, event):
        position = "{0},{1}".format(self.x(), self.y())
        self.signals.setSetting.emit('position', position, self.objectName(), )

    def resizeEvent(self, event):
        sizeW, sizeH = get_layout_size(self)
        self.signals.setSetting.emit('width', str(sizeW), self.objectName())
        self.signals.setSetting.emit('height', str(sizeH), self.objectName())

    def sizeHint(self):
        size = super(Widget, self).sizeHint()
        size.setHeight(size.height())
        size.setWidth(max(size.width(), size.height()))
        return size

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 1/08/2018 - 4:12 AM
# © 2017 - 2018 DAMGteam. All rights reserved