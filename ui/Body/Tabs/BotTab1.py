# -*- coding: utf-8 -*-
"""

Script Name: BotTab1.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


from ui.uikits.Widget                       import Widget
from ui.uikits.GridLayout                   import GridLayout
from ui.uikits.CheckBox                     import CheckBox
from ui.uikits.Label                        import Label
from bin.dependencies.damg.damg             import DAMGDICT, DAMGLIST
from utils                                  import str2bool
from appData                                import SiPoMin


class BotTab1(Widget):

    key = 'BotTab1'
    checkboxes = DAMGDICT()
    cbs = DAMGLIST()

    def __init__(self, parent=None):
        super(BotTab1, self).__init__(parent)

        self.parent = parent
        self.layout = GridLayout()
        # self.layout.addWidget(Label({'txt': 'test'}), 0, 0, 1, 1)
        self.buildUI()
        self.setLayout(self.layout)
        # self.setSizePolicy(SiPoMin, SiPoMin)
        # self.layout.setContentsMargins(1,1,1,1)

    def buildUI(self):

        self.recieveSignalCB                = CheckBox('Recieve')
        self.blockSignalCB                  = CheckBox('Block')
        self.commandCB                      = CheckBox('Command')
        self.registLayoutCB                 = CheckBox('Register')
        self.jobsTodoCB                     = CheckBox('TODO')
        self.showLayoutErrorCB              = CheckBox('ShowError')
        self.trackEventCB                   = CheckBox('Events')
        self.allTrackingCB                  = CheckBox('All')

        self.allTrackingCB.stateChanged.connect(self.changeAllCB)

        x = 0
        y = 0
        w = 1
        h = 1

        for cb in [self.recieveSignalCB, self.blockSignalCB, self.commandCB, self.registLayoutCB, self.jobsTodoCB,
                   self.showLayoutErrorCB, self.trackEventCB, self.allTrackingCB]:
            cb.key = '{0}_{1}_CheckBox_{2}'.format(self.parent.key, self.key, cb.text())
            cb._name = '{0} {1} Check Box: {2}'.format(self.parent.key, self.key, cb.text())
            cb.settings._settingEnable = True
            state = cb.getValue('checkState')
            if state is None:
                state = True
            cb.setValue('checkState', state)
            cb.setChecked(str2bool(state))
            self.checkboxes.add(cb.key, cb)
            self.cbs.append(cb)

            self.layout.addWidget(cb, x, y, w, h)
            y += 1
            if y == 4:
                x += 1
                y = 0

    def set_tooltip(self):
        self.recieveSignalCB.setToolTip('Tracking Signal recieved')
        self.blockSignalCB.setToolTip('Tracking Signal is blocked')
        self.commandCB.setToolTip('Tracking Command working')
        self.registLayoutCB.setToolTip('Tracking layout is registed')
        self.jobsTodoCB.setToolTip('Tracking Jobs to do')
        self.showLayoutErrorCB.setToolTip('Tracking show layout error')
        self.trackEventCB.setToolTip('Tracking Events happening')

    def changeAllCB(self, bool):
        for cb in self.cbs:
            cb.setChecked(bool)

    def showEvent(self, event):
        self.resize(100, 30)
        self.resize(297, 112)

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 11/11/2019 - 12:19 PM
# © 2017 - 2018 DAMGteam. All rights reserved