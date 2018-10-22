__version__ = '0.0.4'

import platform

if platform.system() == 'Windows':
    from .windows import WatchableFolder, FolderSpy
elif platform.system() == 'Linux':
    from .linux import WatchableFolder, FolderSpy
elif platform.system() == 'Darwin':
    from .mac import WatchableFolder, FolderSpy
else:
    raise Exception('{0} is not a supported.'.format(platform.system()))
