import queue

from .watcher import FolderWatcher
from folderspy.spy import Spy


class FolderSpy(Spy):

    def _event_loop(self, folders):
        """Kicks off the event loop that begins watching for events."""

        event_queue = queue.Queue()
        for folder in folders:
            FolderWatcher(folder, queue=event_queue)

        while 1:
            try:
                folder, events = event_queue.get_nowait()
                for event in events:
                    getattr(folder, 'process_{0}'.format(event.maskname))(event)
            except queue.Empty:
                pass
