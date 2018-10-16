import sys
import logging
from abc import abstractmethod


class Spy(object):

    @classmethod
    def watch(cls, *args):
        """Set up watches and begin loop to trigger events on folders."""

        cls._setup_watchers(args)
        try:
            cls._event_loop(args)
        except KeyboardInterrupt:
            sys.exit(0)

    @staticmethod
    def _event_loop(folders):
        """Kicks off the event loop that begins watching for events."""

    @staticmethod
    def _setup_watchers(folders):
        """Setup watchers for all folders."""
