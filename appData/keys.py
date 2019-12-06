# -*- coding: utf-8 -*-
"""

Script Name: keys.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os, sys

# --------------------------------------------------------------------------------------------------------------
""" Autodesk _data """

autodeskVer         = [ "2017", "2018", "2019", "2020"]
autodeskApp         = [ "Autodesk Maya", "Autodesk MudBox", "Autodesk 3ds Max", "Autodesk AutoCAD"]
userMayaDir         = os.path.expanduser(r"~/Documents/maya")

# --------------------------------------------------------------------------------------------------------------
""" Adobe _data """

adobeVer            = [ "CC 2017", "CC 2018", "CC 2019", ]
adobeApp            = [ "Adobe Photoshop", "Adobe Illustrator", "Adobe Audition", "Adobe After Effects", "Adobe Premiere Pro",
                        "Adobe Media Encoder", ]

# --------------------------------------------------------------------------------------------------------------
""" Foundry _data """

foundryVer          = [ "11.1v1", "11.2v1", "4.0v1", "4.1v1", "2.6v3"]
foundryApp          = [ 'Hiero', 'HieroPlayer', 'Mari', 'NukeX', 'Katana',]

# --------------------------------------------------------------------------------------------------------------
""" Pixologic _data """

pixologiVer         = [ "4R6", "4R7", "4R8"]
pixologiApp         = [ 'ZBrush', ]

# --------------------------------------------------------------------------------------------------------------
""" Allegorithmic _data """

allegorithmicVer    = [ ]

allegorithmicApp    = [ 'Substance Painter', 'Substance Designer']

# --------------------------------------------------------------------------------------------------------------
""" SideFX _data """

sizefxVer           = [ '16.5.439', '16.5.496']
sizefxApp           = [ 'Houdini FX', ]

# --------------------------------------------------------------------------------------------------------------
""" Microsoft Office _data """

officeVer           = [ '2013', '2015', '2016', '2017', "2018", "2019", "2020"]
officeApp           = [ 'Word', 'Excel', 'PowerPoint', 'Wordpad']

# --------------------------------------------------------------------------------------------------------------
""" JetBrains _data """

jetbrainsVer        = [ '2017.3.3', '2018.1', ]
jetbrainsApp        = [ 'JetBrains PyCharm', ]

# --------------------------------------------------------------------------------------------------------------
""" Wonder Unit """

wonderUnitVer       = [ ]
wonderUniApp        = [ 'Storyboarder', 'Krita (x64)' ]

# --------------------------------------------------------------------------------------------------------------
""" another app _data """

anacondaApp         = [ 'Spyder', 'QtDesigner', 'Git Bash']
otherApp            = [ 'Sublime Text 2', 'Sublime Text 3', 'Wordpad', 'Headus UVLayout', 'Snipping Tool', ]
CONFIG_APPUI        = [ 'About', 'Calculator', 'Calendar', 'Credit', 'EnglishDictionary', 'FindFiles', 'ForgotPassword',
                        'ImageViewer', 'NewProject', 'Preferences', 'ScreenShot', 'UserSetting', 'PLMBrowser',
                        'NoteReminder', 'TextEditor', 'NodeGraph', 'Messenger', 'InviteFriend', 'SignIn', 'SignUp',
                        'SignOut', 'SwitchAccount']

# --------------------------------------------------------------------------------------------------------------
""" Tracking configKey """

TRACK_TDS           = [ 'Maya', 'ZBrush', 'Houdini', '3Ds Max', 'Mudbox', 'BLender', ]
TRACK_VFX           = [ 'NukeX', 'After Effects', ]
TRACK_ART           = [ 'Photoshop', 'Illustrator', 'Storyboarder', 'Krita (x64)']
TRACK_TEX           = [ 'Mari', 'Painter', ]
TRACK_POST          = [ 'Davinci Resolve', 'Hiero', 'HieroPlayer', 'Premiere Pro']
TRACK_OFFICE        = [ 'Word', 'Excel', 'PowerPoint', 'Wordpad']
TRACK_DEV           = [ 'PyCharm', 'Sublime Text', 'QtDesigner', 'Git Bash', 'Spyder', 'Command Prompt']
TRACK_TOOLS         = [ 'Calculator', 'Calendar', 'EnglishDictionary', 'FindFiles', 'ImageViewer', 'ScreenShot', 'NodeGraph']
TRACK_EXTRA         = [ 'ReConfig', 'CleanPyc', 'Debug', 'Snipping Tool']
TRACK_SYSTRAY       = [ 'Snipping Tool', 'ScreenShot', 'Maximize', 'Minimize', 'Restore', 'Exit', ]
KEYDETECT           = [ "Non-commercial", "Uninstall", "Verbose", "License", "Skype", ".url"]
FIX_KEY             = { 'ScreenShot': 'ScreenShot', 'Snipping Tool': 'SnippingTool'}

# --------------------------------------------------------------------------------------------------------------
""" Combine _data qssPths """

pVERSION = dict(adobe=adobeVer, autodesk=autodeskVer, allegorithmic = allegorithmicVer, foundry=foundryVer,
                pixologic=pixologiVer, sizefx=sizefxVer, office=officeVer, jetbrains=jetbrainsVer, wonderUnit=wonderUnitVer, )

pPACKAGE = dict(adobe=adobeApp, autodesk=autodeskApp, allegorithmic = allegorithmicApp, foundry=foundryApp,
                pixologic=pixologiApp, sizefx=sizefxApp, office=officeApp, jetbrains=jetbrainsApp, wonderUnit=wonderUniApp,)

pTRACK = dict(TDS=TRACK_TDS, VFX=TRACK_VFX, ART=TRACK_ART, TEXTURE = TRACK_TEX, POST = TRACK_POST,
              Office=TRACK_OFFICE, Dev=TRACK_DEV, Tools=TRACK_TOOLS, Extra=TRACK_EXTRA, sysTray=TRACK_SYSTRAY, )

# --------------------------------------------------------------------------------------------------------------
""" Store _data qssPths """

def generate_key_packages(*args):
    keyPackage = []
    for k in pPACKAGE:
        for name in pPACKAGE[k]:
            if len(pVERSION[k]) == 0:
                key = name
                keyPackage.append(key)
            else:
                for ver in pVERSION[k]:
                    if name == 'Hiero' or name == 'HieroPlayer' or name == 'NukeX':
                        key = name + ver
                    else:
                        if not ver or ver == []:
                            key = name
                        else:
                            key = name + " " + ver
                    keyPackage.append(key)

    return keyPackage + otherApp + anacondaApp + CONFIG_APPUI + ['Word', 'Excel', 'PowerPoint', 'ReConfig', 'CleanPyc', 'Debug', 'Restore', 'Maximize', 'Minimize', 'Quit']

def generate_config(key, *args):
    keyPackages = generate_key_packages()
    keys = []
    for k in keyPackages:
        for t in pTRACK[key]:
            if t in k:
                keys.append(k)
    return list(sorted(set(keys)))

KEYPACKAGE      = generate_key_packages()

# Toolbar _data
CONFIG_TDS      = generate_config('TDS')                            # TD artist
CONFIG_VFX      = generate_config('VFX')                            # VFX artist
CONFIG_ART      = generate_config('ART')                            # 2D artist
CONFIG_TEX      = generate_config('TEXTURE')                        # ShadingTD artist
CONFIG_POST     = generate_config('POST')                           # Post production

# Tab 1 sections _data
CONFIG_OFFICE   = generate_config('Office')                         # Paper work department
CONFIG_DEV      = generate_config('Dev') + ['Command Prompt']       # Rnd - Research and development
CONFIG_TOOLS    = generate_config('Tools')                          # useful/custom tool supporting for the whole pipeline
CONFIG_EXTRA    = generate_config('Extra')                          # Extra tool may be considering to use
CONFIG_SYSTRAY  = generate_config('sysTray') + ['Exit', 'SignIn']

ACTIONS_DATA = dict(TD                  = CONFIG_TDS,
                    VFX                 = CONFIG_VFX,
                    ART                 = CONFIG_ART,
                    TEXTURE             = CONFIG_TEX,
                    POST                = CONFIG_POST,
                    OFFICE              = CONFIG_OFFICE,
                    DEV                 = CONFIG_DEV,
                    TOOLS               = CONFIG_TOOLS,
                    EXTRA               = CONFIG_EXTRA,
                    SYSTRAY             = CONFIG_SYSTRAY, )

SHOWLAYOUT_KEY          = ['About', 'Alpha', 'BotTab', 'Browser', 'Calculator', 'Calendar', 'CodeOfConduct', 'Configuration',
                           'ConfigOrganisation', 'ConfigProject', 'ConfigTask', 'ConfigTeam', 'Configurations',
                           'ConnectStatus', 'ContactUs', 'Contributing', 'Credit', 'EditOrganisation', 'EditProject',
                           'EditTask', 'EditTeam', 'EnglishDictionary', 'Feedback', 'FindFiles', 'Footer',
                           'ForgotPassword', 'GridLayout', 'HDRI', 'ImageViewer', 'Licence', 'MainMenuSection',
                           'MainToolBar', 'MainToolBarSection', 'NodeGraph', 'NoteReminder', 'Notification',
                           'Organisation', 'PipelineManager', 'Preferences', 'Project', 'Reference', 'ScreenShot',
                           'SettingUI', 'SignIn', 'SignOut', 'SignUp', 'StatusBar', 'SwitchAccount', 'SysTray',
                           'Task', 'Team', 'TextEditor', 'Texture', 'TopTab', 'TopTab1', 'TopTab2', 'TopTab3',
                           'UserSetting', 'Version']
RESTORE_KEY             = ['Restore']
SHOWMAX_KEY             = ['Maximize']
SHOWMIN_KEY             = ['Minimize']

STYLESHEET_KEY          = ['bright', 'dark', 'chacoal', 'nuker']

OPEN_BROWSER_KEY        = ['PLM wiki']

START_FILE              = CONFIG_DEV + CONFIG_OFFICE + CONFIG_TDS + CONFIG_VFX + CONFIG_ART + CONFIG_TEX + CONFIG_POST + \
                            ['ConfigFolder', 'IconFolder', 'SettingFolder', 'AppFolder', 'Snipping Tool']

EDIT_KEY                = ['Cut', 'Copy', 'Paste']

START_FILE_KEY          = sorted([i for i in START_FILE if not i == 'Command Prompt'])

EXECUTING_KEY           = ['Exit', 'CleanPyc', 'ReConfig', 'Debug', 'Command Prompt', 'Showall'] + EDIT_KEY + STYLESHEET_KEY

IGNORE_ICON_NAME        = ['Widget', 'TopTab1', 'TopTab2', 'TopTab3', 'ItemWidget']

# Binding config
QT_BINDINGS = ['PyQt5', 'PySide2', 'pyqt']
"""list: values of all Qt bindings to import."""

QT_ABSTRACTIONS = ['qtpy', 'pyqtgraph', 'Qt']
"""list: values of all Qt abstraction layers to import."""

QT5_IMPORT_API = ['QtCore', 'QtGui', 'QtWidgets', 'QtWebEngineWidgets', 'QtWebKitWidgets']
"""list: which subpackage to import for Qt5 API."""

QT_API_VALUES = ['pyqt', 'pyqt5', 'pyside2']
"""list: values for QT_API environment variable used by QtPy."""

QT_LIB_VALUES = ['PyQt', 'PyQt5', 'PySide2']
"""list: values for PYQTGRAPH_QT_LIB environment variable used by PyQtGraph."""

QT_BINDING = 'Not set or nonexistent'
"""str: Qt binding in use."""

QT_ABSTRACTION = 'Not set or nonexistent'
"""str: Qt abstraction layer in use."""

IMAGE_BLACKLIST = ['base_palette']

PY2 = sys.version[0] == '2'

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 6/08/2018 - 2:30 AM
# © 2017 - 2018 DAMGteam. All rights reserved