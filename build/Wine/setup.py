from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict (packages = []
                    ,includes = ['re']
                    ,excludes = []
                    )

executables = [Executable ('SendTableSymbols.py'
                          ,base       = 'Win32GUI'
                          ,targetName = 'SendTableSymbols.exe'
                          )
              ]

setup (name        = 'SendTableSymbols.py'
      ,version     = '1.0'
      ,description = 'Paste a special symbol into an external application'
      ,options     = dict(build_exe=buildOptions)
      ,executables = executables
      )
