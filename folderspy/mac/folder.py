import os.path

from fsevents import Stream
from fsevents import IN_MODIFY, IN_ATTRIB, IN_CREATE, IN_DELETE, IN_MOVED_FROM, IN_MOVED_TO


class FileEvent(object):

    def __init__(self, full_path, maskname):
        self.name = os.path.basename(full_path)
        self.pathname = full_path
        self.maskname = maskname


class WatchableFolder(object):

    MASK_NAMES = {
        IN_MODIFY: 'IN_MODIFY',
        IN_ATTRIB: 'IN_ATTRIB',
        IN_CREATE: 'IN_CREATE',
        IN_DELETE: 'IN_DELETE',
        IN_MOVED_FROM: 'IN_MOVED_FROM',
        IN_MOVED_TO: 'IN_MOVED_TO'
    }

    def __init__(self, path='', recursive=False, listen_to=None):
        self.path = path
        self.recursive = recursive
        self.listen_to = listen_to
        self.stream = Stream(self._on_event, self.path, file_events=True)

    def _on_event(self, event):
        """Called when any event is triggered."""

        mask_name = self.MASK_NAMES[event.mask]
        
        getattr(self, 'process_{0}'.format(mask_name))(
            FileEvent(event.name, mask_name)
        )

    def process_IN_ATTRIB(self, event):
        """Metadata changed for a file."""

    def process_IN_CREATE(self, event):
        """A file/directory was created in watched directory."""

    def process_IN_DELETE(self, event):
        """A file/directory was deleted in watched directory."""

    def process_IN_MODIFY(self, event):
        """A file was modified."""

    def process_IN_MOVED_FROM(self, event):
        """A file/directory was moved away from the current watched directory."""

    def process_IN_MOVED_TO(self, event):
        """A file/directory was moved into the current watched directory."""
