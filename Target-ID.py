import os,platform
os.system('clear')
print('\033[1;34m[•] Checking Updates...')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='32bit':
    print('\033[1;32m[•] Congrats! Your Device Support This Tools')
    os.system('xdg-open https://www.facebook.com/MUHID.LI.REPORT.DIYA.LAB.NAI7')
    import FU3K3
    FU3K3.menu()
