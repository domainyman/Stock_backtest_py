import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": [],
    "zip_include_packages": [],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Backtest System",
    version="0.1",
    description="Auto Backtest System",
    options={"build_exe": build_exe_options},
    executables=[Executable("Program.py", base=base,icon="coding.ico")],
)