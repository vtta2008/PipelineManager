## **SHORT FILM PIPELINE**

This applications can be used to build, manage, and optimise film making pipelines.

The latest version is compatible with Windows 10 and may run on earlier versions. It does not run in Maya 2016 or lower.

Due to VFX Reference Platform and the large invention, we need to stay with python 2.7 but expect to migrate to python 3 in 2019.

Details are as follows:

    http://www.vfxplatform.com/

**SOFTWARE TO INSTALL**

Python standalone:
    <64 bit>

        anaconda 2.7" = "https://repo.anaconda.com/archive/Anaconda2-5.1.0-Windows-x86_64.exe
        anaconda 3.6" = "https://repo.anaconda.com/archive/Anaconda3-5.1.0-Windows-x86_64.exe

    <32 bit>

    - Also require extra python packages (will update more):

        deprecated, jupyter-console, ipywidgets,'pywinauto, winshell, pandas,
        notebook, juppyter, opencv-python, pyunpack, argparse, qdarkgraystyle,
        asyncio, websockets, cx_Freeze,

    - To install extra packages, run command in CMD:

        "python -m pip install {packagename}"

**LIST SOFTWARES PACKAGE**

    - Maya 2017: https://www.autodesk.com/education/free-software/maya
    - Vray 3.6: https://www.chaosgroup.com/vray/maya
    - Phoenix FD 3.0: https://www.chaosgroup.com/phoenix-fd/maya
    - VMM for maya: https://www.mediafire.com/#gu9s1tbb2u4g9
    - Houdini: https://www.sidefx.com/download/
    - Mari download: https://www.foundry.com/products/mari
    - Mari extension: "Will update later"
    - Nuke download: https://www.foundry.com/products/nuke
    - ZBrush download: https://pixologic.com/zbrush/downloadcenter/
    - Creative Cloud download: https://www.adobe.com/creativecloud/catalog/desktop.html
    - Davinci Resolve: https://www.blackmagicdesign.com/nz/products/davinciresolve/

NOTE:
    - You can install Photoshop, Premiere, After Effects or anything you want with Adobe Creative Cloud

    - For VMM for maya, remember to configure the path once it is opened in Maya. (sadly, the author has stopped developing the plugin.)

**LIBRARY SUPPORT**

I spent many years to build this library for texturing and referencing. The library is now freely availalbe to everyone.
You may also find the following libraries useful:

    - ALPHA library: https://www.mediafire.com/#21br3oz8gf44j
    - HDRI library: https://www.mediafire.com/#33moon9n0qagc
    - TEXTURE library: https://www.mediafire.com/#v5t32j935afg7

**RUN PIPELINE TOOL**

Download and extract the zip file, remember to rename the folder as 'PipelineTool'.

**HOW TO USE PIPELINE TOOL**

Go to the diretory of 'PipelineTool' folder, hold down Shift + right-click -> Open PowerShell window here/Open command window here
In CommandPrompt/WindowShell:

    - Run directly: "start python main.py"

    - Complie executable file: "python setup.py build"

**REFERENCE**

Here is the Plugins/Files that I use in Maya:

    GitHub - mottosso/Qt.py: Minimal Python 2 & 3 shim around all Qt bindings - PySide,
    PySide2, PyQt4 and PyQt5. (n.d.). Retrieved from https://github.com/mottosso/Qt.py

Database browser:

    sqlitebrowser/sqlitebrowser. (2017, November 30).
    Retrieved from https://github.com/sqlitebrowser/sqlitebrowser

Advance Renamer:

    Advanced Renamer - Free and fast batch rename utility for files and folders. (n.d.).
    Retrieved from https://www.advancedrenamer.com/