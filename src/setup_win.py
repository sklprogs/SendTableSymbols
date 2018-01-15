from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict (packages = []
                    ,includes = []
                    ,excludes = []
                    )

executables = [Executable ('map.py'
                          ,base = 'Win32GUI'
                          ,targetName = 'map.exe'
                          )
              ]

setup (name        = 'map.py'
      ,version     = '1.0'
      ,description = 'Paste a special symbol into an external application'
      ,options     = dict(build_exe=buildOptions)
      ,executables = executables
      )
