from fsevents import Observer, Stream

from folderspy.spy import Spy


class FolderSpy(Spy):

    def _setup_watchers(self, folders):
        """Setup watchers for all folders."""
        
        return {'observer': Observer()}

    def _event_loop(self, folders, **kwargs):
        """Kicks off the event loop that begins watching for events."""

        observer = kwargs['observer']

        for folder in folders:
            observer.schedule(folder.stream)

        observer.start()

    def _on_exit(self, folders, **kwargs):
        """Called when folder spying ends."""

        observer = kwargs['observer']

        observer.stop()
        for folder in folders:
            observer.unschedule(folder.stream)
        observer.join()
