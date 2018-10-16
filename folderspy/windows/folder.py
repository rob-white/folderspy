class WatchableFolder(object):

    def __init__(self, path='', recursive=False, listen_to=None):
        self.path = path
        self.recursive = recursive
        self.listen_to = listen_to

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
        """Any event occurred that was on a directory."""
