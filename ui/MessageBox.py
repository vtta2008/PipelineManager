# -*- coding: utf-8 -*-
"""

Script Name: PopupMessage.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

from PyQt5.QtWidgets import QMessageBox

from cores.Loggers import Loggers
from ui.uikits.UiPreset import IconPth

class MessageBox(QMessageBox):

    def __init__(self, parent=None, title="auto", level="auto", message="test message", btn='ok', **kwargs):
        super(MessageBox, self).__init__(parent)

        self._parent                = parent
        self._title                 = title
        self._level                 = level
        self._message               = message
        self._btn                   = btn

        if self._parent is None:
            self.logger = Loggers(__name__)
        else:
            self.logger = Loggers(self)

        if self._title == 'auto' or self._title is None:
            self.popupTitle             = self._level
        else:
            self.popupTitle             = self._title

        self.popupIcon                  = self.config_icon()
        self.popupLevel                 = self.config_level()
        self.btn                        = self.config_button()

        self.popupLevel(self._parent, self.popupTitle, self._message, self.btn)


    def config_level(self):

        levels = dict(

            about                   = QMessageBox.about,
            information             = QMessageBox.information,
            question                = QMessageBox.question,
            warning                 = QMessageBox.warning,
            critical                = QMessageBox.critical,

        )

        return levels[self._level]
        
    def config_icon(self):

        icons = dict(

            about                   = QMessageBox.NoIcon,
            information             = QMessageBox.Information,
            question                = QMessageBox.Question,
            warning                 = QMessageBox.Warning,
            critical                = QMessageBox.Critical,

        )

        if self._level in icons.keys():
            return icons[self._level]
        else:
            IconPth(self._level)

    def config_button(self):
        
        buttons = dict(

            ok                      = QMessageBox.Ok,
            open                    = QMessageBox.Open,
            save                    = QMessageBox.Save,
            cancel                  = QMessageBox.Cancel,
            close                   = QMessageBox.Close,
            yes                     = QMessageBox.Yes,
            no                      = QMessageBox.No,
            abort                   = QMessageBox.Abort,
            retry                   = QMessageBox.Retry,
            ignore                  = QMessageBox.Ignore,
            discard                 = QMessageBox.Discard,
            yes_no                  = QMessageBox.Yes|QMessageBox.No,
            retry_close             = QMessageBox.Retry|QMessageBox.Close,
            
        )

        return buttons[self._btn]





# -------------------------------------------------------------------------------------------------------------
# Created by panda on 23/10/2019 - 8:57 AM
# © 2017 - 2018 DAMGteam. All rights reserved