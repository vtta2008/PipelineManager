# -*- coding: utf-8 -*-
"""

Script Name: StatusBar.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys

# PyQt5
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QStatusBar

# Plt
import appData as app

# -------------------------------------------------------------------------------------------------------------
""" StatusBar """


class StatusBar(QStatusBar):

    statusBarSig = pyqtSignal(str)

    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        # from core.Settings import Settings
        self.settings = app.appSetting
        self.applySetting()

    def applySetting(self):
        pass



def main():
    app = QApplication(sys.argv)
    layout = StatusBar()
    layout.show()
    app.exec_()


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/06/2018 - 10:39 PM
# © 2017 - 2018 DAMGteam. All rights reserved
