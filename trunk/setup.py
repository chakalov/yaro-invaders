from cx_Freeze import setup, Executable
 
exe = Executable(
    script="Invaders.py"
    )
 
setup(
    name = "Invaders",
    version = "0.1",
    description = "Invaders Game",
    executables = [exe]
    )