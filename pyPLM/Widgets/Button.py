# -*- coding: utf-8 -*-
"""

Script Name: Button.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """


from PySide2.QtWidgets                      import QPushButton, QToolButton
from pyPLM.models import DamgSignals
from pyPLM.settings import AppSettings


# -------------------------------------------------------------------------------------------------------------
""" Button presets """

class Button(QPushButton):

    Type                                    = 'DAMGBUTTON'
    key                                     = 'Button'
    _name                                   = 'DAMG Button'

    def __init__(self, preset={}, parent=None):
        super(Button, self).__init__(parent)

        self.parent                         = parent
        self.settings                       = AppSettings(self)
        self.signals                        = DamgSignals(self)
        self.preset                         = preset

        if self.preset and not {}:
            self.buildUI()

    def buildUI(self):

        from pyPLM.Gui import AppIcon, TagIcon

        for key, value in self.preset.items():
            if key == 'txt':
                self.setText(value)
            elif key == 'tt':
                self.setToolTip(value)
            elif key == 'cl':
                self.clicked.connect(value)
            elif key == 'icon':
                self.setIcon(AppIcon(32, value))
            elif key == 'tag':
                self.setIcon(TagIcon(value))
            elif key == 'icon24':
                self.setIcon(AppIcon(24, value))
            elif key == 'fix':
                self.setFixedSize(value)
            elif key == 'ics':
                self.setIconSize(value)
            elif key == 'stt':
                self.setToolTip(value)
            else:
                print("PresetKeyError at {0}: No such key registed in preset: {1}: {2}".format(__name__, key, value))

    def setValue(self, key, value):
        return self.settings.initSetValue(key, value, self.key)

    def getValue(self, key, decode=None):
        if decode is None:
            return self.settings.initValue(key, self.key)
        else:
            return self.settings.initValue(key, self.key, decode)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name                      = newName


class ToolButton(QToolButton):

    Type                                    = 'DAMGTOOLBUTTON'
    key                                     = 'ToolButton'
    _name                                   = 'DAMG Tool Button'

    def __init__(self, text, parent=None):
        QToolButton.__init__(self)

        self.parent                         = parent
        self.settings                       = AppSettings(self)
        self.signals                        = DamgSignals(self)
        self.setText(text)

    def setValue(self, key, value):
        return self.settings.initSetValue(key, value, self.key)

    def getValue(self, key):
        return self.settings.initValue(key, self.key)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 18/07/2018 - 8:37 AM
# © 2017 - 2018 DAMGteam. All rights reserved