import sys
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

setup(
    name='freetrade',
    version='0.0.1',
    description='yet a free trade software.',
    executables=[
        Executable(
            'app.py',
            base=base,
            icon='assets/freetrade.ico',
            copyright='Copyright © 2022 Chen Shen Chao',
            shortcut_name='freetrade',
            shortcut_dir='DesktopFolder',
        ),
    ],
    options={
        'build_exe': {
            'optimize': 2,
            'include_msvcr': True,
            'excludes': [
                'tkinter',
            ],
            'packages': [
                'whoosh',
                'PySide6',
                'jieba',
                'loguru',
            ],
        },
        'bdist_msi': {
            'all_users': True,
        },
    },
)