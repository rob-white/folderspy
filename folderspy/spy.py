import sys
import logging
from abc import abstractmethod


class Spy(object):

    @classmethod
    def watch(cls, *args):
        """Set up watches and begin loop to trigger events on folders."""
        
        instance = cls()

        kwargs = instance._setup_watchers(args)
        
        try:
            instance._event_loop(args, **kwargs)
        except KeyboardInterrupt:
            for folder in args:
                try:
                    folder.on_exit()
                except AttributeError:
                    pass
            
            instance._on_exit(args, **kwargs)         
            sys.exit(0)

    def _setup_watchers(self, folders):
        """Setup watchers for all folders."""

    def _event_loop(self, folders, **kwargs):
        """Kicks off the event loop that begins watching for events."""

    def _on_exit(self, folders, **kwargs):
        """Called when folder spying ends."""