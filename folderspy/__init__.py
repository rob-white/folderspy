import platform

if platform.system() == 'Windows':
    from .windows import WatchableFolder, FolderSpy
elif platform.system() == 'Linux':
    from .linux import WatchableFolder, FolderSpy
else:
    raise Exception('{0} is not a supported.'.format(platform.system()))
