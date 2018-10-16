import pyinotify


class WatchableFolder(pyinotify.ProcessEvent):

    def __init__(self, path='', recursive=False, listen_to=None):
        self.path = path
        self.recursive = recursive
        self.listen_to = listen_to

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
