#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Script Name: __init__.py
Author: Do Trinh/Jimmy - 3D artist.

"""

import os

__root__ = "PLT_RT"
os.environ[__root__] = os.getcwd()

__appname__ = "Pipeline Tool (plt)"
__version__ = "13.0.1"
__organization__ = "DAMG team"
__website__ = "https://pipeline.damgteam.com"
__download__ = "https://github.com/vtta2008/pipelineTool"
__email__ = "dot@damgteam.com"
__author__ = "Trinh Do, a.k.a: Jimmy"
__description__ = "This applications can be used to build, manage, and optimise film making pipelines."
__readme__ = os.path.join(os.getenv(__root__), 'README.md')
__licence__ = os.path.join(os.getenv(__root__), 'LICENSE')

__modules__ = ['plt', 'plt_preset', 'utilities.variables', 'utilities.utils', 'utilities.sql_server',
                  'utilities.sql_local', 'utilities.message', 'ui.ui_acc_setting', 'ui.ui_calculator',
                  'ui.ui_calendar', 'ui.ui_english_dict', 'ui.ui_find_files', 'ui.ui_image_viewer',
                  'ui.ui_info_template', 'ui.ui_new_project', 'ui.ui_note_reminder', 'ui.ui_preference',
                  'ui.ui_pw_reset_form', 'ui.ui_screenshot', ]

__pkgsReq__ = ['deprecated', 'jupyter-console', 'ipywidgets', 'pywinauto', 'winshell',
               'pandas', 'notebook', 'juppyter', 'opencv-python', 'pyunpack', 'argparse']

__packages__ = ['', 'bin', 'qdarkgraystyle', 'ui', 'textedit', 'bin', 'appData', 'utilities']

__pkgsDir__ = {
        'bin': os.path.join(os.getenv(__root__), 'bin'),
        'qdarkgraystyle': os.path.join(os.getenv(__root__), 'bin', 'qdarkgraystyle'),
        'ui': os.path.join(os.getenv(__root__), 'ui'),
        'textedit': os.path.join(os.getenv(__root__), 'ui', 'textedit'),
        'appData': os.path.join(os.getenv(__root__), 'appData'),
        'utilities': os.path.join(os.getenv(__root__), 'utilities'),
    }

__classifiers__ = [
              'Development Status :: 3 - Production/Unstable',
              'Environment :: X11 Applications :: Qt',
              'Environment :: Win32 (MS Windows)',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX :: Linux',
              'Operating System :: MacOS',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Topic :: Software Development :: Libraries :: Application '
              'Frameworks',
        ]