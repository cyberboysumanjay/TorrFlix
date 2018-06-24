import subprocess
def peerflix_stream(magnet):
    command=[]
    command.append('peerflix')
    command.append(magnet)
    command.append('-m')
    command.append('-a')
    command.append('--vlc')
    subprocess.call(command)
