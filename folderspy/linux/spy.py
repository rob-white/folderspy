import asyncore

import pyinotify

from folderspy.spy import Spy


class FolderSpy(Spy):

    @staticmethod
    def _setup_watchers(folders):
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
    
    @staticmethod
    def _event_loop(folders, **kwargs):
        """Kicks off the event loop that begins watching for events."""

        asyncore.loop()
