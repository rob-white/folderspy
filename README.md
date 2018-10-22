# folderspy

[![image](https://img.shields.io/pypi/v/folderspy.svg)](https://pypi.org/project/folderspy/)
[![image](https://img.shields.io/pypi/pyversions/folderspy.svg)](https://pypi.org/project/folderspy/)

> Watch folders for file/directory events with a simple API.

## Supports
* Linux & Windows
* Python 2.7 & 3.4-3.7

## Installation

### pipenv
```sh
pipenv install folderspy
```

### pip
```sh
pip install folderspy
```

## Example

Create a ```WatchableFolder``` class for each of folders you want to watch then simply start watching them with ```FolderSpy```:
```python
import pyinotify  # Linux Only
from folderspy import WatchableFolder, FolderSpy


class SaveFolder(WatchableFolder):

    def __init__(self):
        super(SaveFolder, self).__init__()

        self.path = '/path/to/this/folder'

        # Note: Only used in Linux for pyinotify bitmasks
        # Can be excluded for Windows
        self.listen_to = pyinotify.IN_CREATE

    def process_IN_CREATE(self, event):
        print('An item was created in this folder!')
    

FolderSpy.watch(SaveFolder())
```

## Available Folder Events
### Linux

```python
    def process_IN_ACCESS(self, event):
        """A file was accessed."""

    def process_IN_ATTRIB(self, event):
        """Metadata changed for a file."""

    def process_IN_CLOSE_NOWRITE(self, event):
        """An unwritable file was closed."""

    def process_IN_CLOSE_WRITE(self, event):
        """A writable file was closed."""

    def process_IN_CREATE(self, event):
        """A file/directory was created in watched directory."""

    def process_IN_DELETE(self, event):
        """A file/directory was deleted in watched directory."""

    def process_IN_DELETE_SELF(self, event):
        """The watched item itself was deleted."""

    def process_IN_ISDIR(self, event):
        """Any event occurred that was on a directory."""

    def process_IN_MODIFY(self, event):
        """A file was modified."""

    def process_IN_MOVE_SELF(self, event):
        """The watched item itself was moved somewhere."""

    def process_IN_MOVED_FROM(self, event):
        """A file/directory was moved away from the current watched directory."""

    def process_IN_MOVED_TO(self, event):
        """A file/directory was moved into the current watched directory."""

    def process_IN_OPEN(self, event):
        """A file was opened."""

    def process_IN_UNMOUNT(self, event):
        """The file system the watched directory is associated with was unmounted."""
```

### Windows
```python
    def process_IN_CREATE(self, event):
        """A file/directory was created in watched directory."""

    def process_IN_DELETE(self, event):
        """A file/directory was deleted in watched directory."""

    def process_IN_MODIFY(self, event):
        """A file was modified."""

    def process_IN_RENAMED_FROM(self, event):
        """The name the file/directory was renamed from."""

    def process_IN_RENAMED_TO(self, event):
        """The name the file/directory was renamed to."""

    def process_IN_ISDIR(self, event):
        """An event occurred that was on a directory."""
```

## To-Do
* MacOS Support
* Tests
* Clean-up

## Contribute
Pull requests are welcome to add in functionality or fix bugs!