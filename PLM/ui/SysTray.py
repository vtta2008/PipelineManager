#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Script Name: {}.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# PLM
from PLM import __appSlogan__, __appName__
from pyPLM.Widgets import SystemTrayIcon
from pyPLM.Gui import LogoIcon
from PLM.ui.components import SysTrayIconMenu
from PLM.cores import EventManager, sqlUtils
from PLM.ui.models import ActionManager


# -------------------------------------------------------------------------------------------------------------
class SysTray(SystemTrayIcon):

    key                                 = 'SysTray'
    _login                              = False

    def __init__(self, parent=None):
        super(SysTray, self).__init__(parent)

        self.db                         = sqlUtils()
        self.actionManager              = ActionManager()
        self.eventManager               = EventManager()

        try:
            self.username               = self.db.query_table('curUser')[0]
        except (ValueError, IndexError):
            self.username = 'DemoUser'

        self.rightClickMenu             = SysTrayIconMenu(self.actionManager, self.parent)

        self.setIcon(LogoIcon('PLM'))
        self.setToolTip(__appSlogan__)
        self.activated.connect(self.sys_tray_icon_activated)
        self.setContextMenu(self.rightClickMenu)
        self.installEventFilter(self.eventManager.wheelEvent)

        self.show()

    def sys_tray_icon_activated(self, reason):
        if reason == self.DoubleClick:
            if self._login:
                self.parent.command('Restore')

    def log_in(self):
        self.showMessage('Welcome', "Log in as {0}".format(self.username), self.Information, 500)

    def log_out(self):
        self.showMessage('Log out', "{0} Loged out".format(self.username), self.Information, 500)

    def close_event(self):
        self.showMessage('Notice', "{0} will keep running in the system tray.".format(__appName__), self.Information, 500)

    def loginChanged(self, login):
        self._login = login
        self.rightClickMenu.loginChanged(self._login)

    def notifier(self, title, mess, iconType='info', timeDelay=500):
        if iconType == 'info':
            icon = self.Information
        elif iconType == 'crit':
            icon = self.Critical
        else:
            icon = self.Context

        self.showMessage(title, mess, icon, timeDelay)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, newVal):
        self._login = newVal

    def close(self):
        return self.show()

    def hide(self):
        return self.show()

    def setVisible(self, bool):
        if not self.isVisible():
            return self.setVisible(True)


# -------------------------------------------------------------------------------------------------------------
# Created by panda on 6/07/2018 - 11:31 AM
# © 2017 - 2018 DAMGTEAM. All rights reserved