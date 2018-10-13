import sys
import logging
from abc import abstractmethod


class Spy(object):

    def watch(self, *args):
        """Set up watches and begin loop to trigger events on folders."""

        self._setup_watchers(args)
        try:
            self._event_loop(args)
        except KeyboardInterrupt:
            sys.exit(0)

    @abstractmethod
    def _event_loop(self, folders):
        """Kicks off the event loop that begins watching for events."""

    def _setup_watchers(self, folders):
        """Setup watchers for all folders."""
