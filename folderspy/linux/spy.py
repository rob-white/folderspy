import asyncore

import pyinotify

from folderspy.spy import Spy


class FolderSpy(Spy):

    def _setup_watchers(self, folders):
        """Setup watchers for all folders."""

        manager = pyinotify.WatchManager()
        pyinotify.AsyncNotifier(manager)

        for folder in folders:
            manager.add_watch(
                folder.path,
                mask=folder.listen_to,
                proc_fun=folder,
                rec=folder.recursive
            )
        
        return {'manager': manager}
    
    def _event_loop(self, folders, **kwargs):
        """Kicks off the event loop that begins watching for events."""

        asyncore.loop()
