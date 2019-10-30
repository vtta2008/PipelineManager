# -*- coding: utf-8 -*-
"""

Script Name: MainMenu.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys, os
from functools                      import partial

# PyQt5
from PyQt5.QtCore                   import pyqtSlot
from PyQt5.QtWidgets                import QApplication

# Plm
from appData                        import (__plmWiki__, CONFIG_DIR, APP_ICON_DIR, SETTING_DIR, ROOT_DIR,
                                            mainConfig, CONFIG_OFFICE, CONFIG_DEV, CONFIG_TOOLS)

from ui.uikits.Action               import Action
from ui.uikits.MainWindow import MainWindow
from utils                          import data_handler

class MainMenuBar(MainWindow):

    key                     = 'MainMenuBar'

    appInfo = data_handler(filePath=mainConfig)

    def __init__(self, parent=None):
        MainWindow.__init__(self)

        self._parent = parent
        self.url = __plmWiki__
        self.buildMenu()

    def buildMenu(self):

        self.mainMenu = self.menuBar()

        self.appMenu = self.mainMenu.addMenu("&App")
        self.appMenu.addAction(Action({'icon': 'Settings', 'txt': "&Settings", 'trg': partial(self.signals.showLayout.emit, 'SettingUI', 'show')}, self))
        self.appMenu.addAction(Action({'icon': 'Configurations', 'txt': '&Config', 'trg': partial(self.signals.showLayout.emit, 'Configuration', 'show')}, self))
        self.appMenu.addAction(Action({'icon': 'Preferences', 'txt': '&Preferences', 'trg': partial(self.signals.showLayout.emit, 'Preferences', 'show')}, self))

        self.appMenu.addSeparator()

        self.organisationMenu = self.appMenu.addMenu("&Organisation")
        self.organisationMenu.addAction(Action({'icon': 'NewOrganisation', 'txt': 'New', 'trg': partial(self.signals.showLayout.emit, 'NewOrganisation', 'show')}, self))
        self.organisationMenu.addAction(Action({'icon': 'EditOrganisation', 'txt': 'Edit', 'trg': partial(self.signals.showLayout.emit, 'EditOrganisation', 'show')}, self))
        self.organisationMenu.addAction(Action({'icon': 'ConfigOrganisation', 'txt': 'Config', 'trg': partial(self.signals.showLayout.emit, 'ConfigOrganisation', 'show')}, self))
        self.organisationMenu.addAction(Action({'icon': 'OrganisationManager', 'txt': 'Organisation Manager', 'trg': partial(self.signals.showLayout, 'OrganisationManager', 'show')}, self))

        self.teamMenu = self.appMenu.addMenu('&Team')
        self.teamMenu.addAction(Action({'icon': 'NewTeam', 'txt': 'New', 'trg': partial(self.signals.showLayout.emit, 'NewTeam', 'show')}, self))
        self.teamMenu.addAction(Action({'icon': 'EditTeam', 'txt': 'Edit', 'trg': partial(self.signals.showLayout.emit, 'EditTeam', 'show')}, self))
        self.teamMenu.addAction(Action({'icon': 'ConfigTeam', 'txt': 'Config', 'trg': partial(self.signals.showLayout.emit, 'ConfigTeam', 'show')}, self))
        self.teamMenu.addAction(Action({'icon': 'TeamManager', 'txt': 'Team Manager', 'trg': partial(self.signals.showLayout, 'TeamManager', 'show')}, self))

        self.projectMenu = self.appMenu.addMenu('&Project')
        self.projectMenu.addAction(Action({'icon': 'NewProject', 'txt': 'New', 'trg': partial(self.signals.showLayout.emit, 'NewProject', 'show')}, self))
        self.projectMenu.addAction(Action({'icon': 'EditProject', 'txt': 'Edit', 'trg': partial(self.signals.showLayout.emit, 'EditProject', 'show')}, self))
        self.projectMenu.addAction(Action({'icon': 'ConfigProject', 'txt': 'Config', 'trg': partial(self.signals.showLayout.emit, 'ConfigProject', 'show')}, self))
        self.projectMenu.addAction(Action({'icon': 'ProjectManager', 'txt': 'Project Manager', 'trg': partial(self.signals.showLayout.emit, 'ProjectManager', 'show')}, self))

        self.appMenu.addSeparator()
        self.appMenu.addAction(Action({'icon': 'Exit', 'txt': 'Exit app', 'trg': partial(self.signals.executing.emit, 'Exit')}, self))

        self.gotoMenu = self.mainMenu.addMenu('Go to')
        self.gotoMenu.addAction(Action({'icon': 'ConfigFolder', 'txt': 'Config folder', 'trg': partial(os.startfile, CONFIG_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'IconFolder', 'txt': 'Icon folder', 'trg': partial(os.startfile, APP_ICON_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'SettingFolder', 'txt': 'Setting folder', 'trg': partial(os.startfile, SETTING_DIR)}, self))
        self.gotoMenu.addAction(Action({'icon': 'AppFolder', 'txt': 'Application folder', 'trg': partial(os.startfile, ROOT_DIR)}, self))

        self.officeMenu = self.mainMenu.addMenu("&Office")

        officeKeys = ['TextEditor', 'NoteReminder']

        for key in officeKeys:
            if key in self.appInfo:
                self.officeMenu.addAction(Action({'icon': key,
                                                  'txt': key,
                                                  'trg': partial(self.signals.showLayout.emit, key, 'show')}, self))
        for key in CONFIG_OFFICE:
            if key in self.appInfo:
                self.officeMenu.addAction(Action({'icon': key,
                                                  'txt': key,
                                                  'trg': partial(os.startfile, key)}, self))

        self.toolMenu = self.mainMenu.addMenu("&Tools")

        for key in CONFIG_TOOLS:
            if key in self.appInfo:
                self.toolMenu.addAction(Action({'icon': key,
                                                'txt': key,
                                                'trg': partial(self.signals.showLayout.emit, key, 'show')}, self))

        self.toolMenu.addSeparator()

        self.toolMenu.addAction(Action(
            {'icon': "CleanPyc", 'txt': 'Remove .pyc files', 'trg': partial(self.signals.executing.emit, 'CleanPyc')},
            self))
        self.toolMenu.addAction(
            Action({'icon': "ReConfig", 'txt': 'Re-configure', 'trg': partial(self.signals.executing.emit, 'ReConfig')},
                   self))
        self.toolMenu.addAction(
            Action({'icon': "Debug", 'txt': 'Run PLM Debugger', 'trg': partial(self.signals.executing.emit, 'Debug')},
                   self))

        self.devMenu = self.mainMenu.addMenu("&Dev")

        for key in CONFIG_DEV:
            if key in self.appInfo:
                if key in self.appInfo:
                    self.devMenu.addAction(Action({'icon': key,
                                                   'txt': key,
                                                   'trg': partial(os.startfile, self.appInfo[key][2])},
                                                  self))

        self.libMenu = self.mainMenu.addMenu("&Lib")
        self.libMenu.addAction(Action({'icon': 'ALPHA', 'txt': 'Alpha Library', 'trg': partial(self.signals.showLayout.emit, 'AlphaLibrary', 'show')}, self))
        self.libMenu.addAction(Action({'icon': 'HDRI', 'txt': 'HDRI Library', 'trg': partial(self.signals.showLayout.emit, 'HdriLibrary', 'show')}, self))
        self.libMenu.addAction(Action({'icon': 'TEXTURE', 'txt': 'Texture Library', 'trg': partial(self.signals.showLayout.emit, 'TextureLibrary', 'show')}, self))

        self.helpMenu = self.mainMenu.addMenu("&Help")
        self.helpMenu.addAction(Action({'icon': 'PLM wiki', 'txt': 'PLM wiki', 'trg': partial(self.signals.openBrowser.emit, self.url)}, self))
        self.helpMenu.addAction(Action({'icon': 'About', 'txt': 'About', 'trg': partial(self.signals.showLayout.emit, 'About', 'show')}, self))
        self.helpMenu.addAction(Action({'icon': 'Credit', 'txt': 'Credit', 'trg': partial(self.signals.showLayout.emit, 'Credit', 'show')}, self))

        self.helpMenu.addSeparator()
        self.helpMenu.addAction(Action({'icon': 'CodeConduct', 'txt':  'Code Of Conduct' , 'trg': partial(self.signals.showLayout.emit, 'CodeOfConduct', 'show')}, self))
        self.helpMenu.addAction(Action({'icon': 'Contributing', 'txt': 'Contributing', 'trg': partial(self.signals.showLayout.emit, 'Contributing', 'show')}, self))
        self.helpMenu.addAction(Action({'icon': 'Reference', 'txt': 'Reference', 'trg': partial(self.signals.showLayout.emit, 'Reference', 'show')}, self))

        self.helpMenu.addSeparator()
        self.helpMenu.addAction(Action({'icon': 'Licence', 'txt': 'Licence', 'trg': partial(self.signals.showLayout.emit, 'Licence', 'show')}, self))
        self.helpMenu.addAction(Action({'icon': 'Version', 'txt': 'Version', 'trg': partial(self.signals.showLayout.emit, 'Version', 'show')}, self))

        self.helpMenu.addSeparator()
        self.helpMenu.addAction(Action({'icon': 'FeedBack', 'txt': 'Feedback to us', 'trg': partial(self.signals.showLayout, 'FeedBackForm', 'show')}, self))
        self.helpMenu.addAction(Action({'icon': 'ContactUs', 'txt': 'Contact Us', 'trg': partial(self.signals.showLayout, 'ContactUs', 'show')}, self))

    @pyqtSlot(bool)
    def show_layout(self, param):
        self.specs.showState.emit(True)
        self.setVisible(param)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    from ui.uikits.GroupBox import GroupBox
    subMenu = MainMenuBar()
    layout = GroupBox("Main Menu", subMenu, "qmainLayout")
    layout.show()
    app.exec_()
# -------------------------------------------------------------------------------------------------------------
# Created by panda on 11/07/2018 - 12:59 AM
# © 2017 - 2018 DAMGteam. All rights reserved