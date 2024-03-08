import platform, os
if platform.architecture()[0] == "64bit":
    import X_T
    X_T()
else:
    exit('YOUR DEVICE LOW BRO')
