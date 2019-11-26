# -*- coding: utf-8 -*-
"""

Script Name: StyleSheet.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os
import platform

# PyQt5
from PyQt5.QtCore                    import QFile

# Plm
from bin.dependencies.damg.damg     import DAMG
from cores.Loggers                  import Loggers
from appData                        import QSS_DIR
from ui.uikits.TextSteam            import TextStream
from scripts.rcs                    import darkstyle_rc, tooltips_rc


class StyleSheet(DAMG):

    _filename = None
    _stylesheet = None

    def __init__(self, style):
        super(StyleSheet, self).__init__()

        self._filename = self.getFileName(style)
        self._filename.open(QFile.ReadOnly | QFile.Text)

        ts = TextStream(self._filename)
        self.logger = Loggers(__name__)
        self._stylesheet = ts.readAll()

        super(StyleSheet, self).__init__()

        if platform.system().lower() == 'darwin':  # see issue #12 on github
            mac_fix = '''
            QDockWidget::title
            {
                background-color: #31363b;
                text-align: center;
                height: 12px;
            }
            '''
            self._stylesheet += mac_fix

    def getFileName(self, name):
        if name == 'dark':
            filename = QFile(os.path.join(QSS_DIR, 'darkstyle.qss'))
        elif name == 'bright':
            filename = QFile(os.path.join(QSS_DIR, 'darkstyle.qss'))
        else:
            if not os.path.exists(name):
                fn = QFile(os.path.join(QSS_DIR, name))
                if fn.exists():
                    filename = fn
                else:
                    filename = QFile()
                    self.logger.error('FileNameError: could not find name: {0}'.format(name))
            else:
                filename = QFile(name)

        return filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, val):
        self._filename = val

    @property
    def stylesheet(self):
        return self._stylesheet

    @stylesheet.setter
    def stylesheet(self, val):
        self._stylesheet = val

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 22/06/2018 - 3:51 AM
# © 2017 - 2018 DAMGteam. All rights reserved