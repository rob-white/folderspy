"""
Thanks to Tim Golden for his write-up on events with pywin32:
http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
"""

import os
from threading import Thread

import win32con
import win32file


class FileEvent(object):

    def __init__(self, file_type, name, full_path, maskname):
        self.dir = True if file_type == 'dir' else False
        self.name = name
        self.pathname = full_path
        self.maskname = maskname


class FolderWatcher(Thread):

    ACTIONS = {
        1: "IN_CREATE",
        2: "IN_DELETE",
        3: "IN_MODIFY",
        4: "IN_RENAMED_FROM",
        5: "IN_RENAMED_TO"
    }

    FILE_LIST_DIRECTORY = 0x0001

    def __init__(self, folder, queue, **kwargs):
        super(FolderWatcher, self).__init__(**kwargs)

        self.setDaemon(1)
        self.folder = folder
        self.queue = queue
        self.start()

    def run(self):
        for events in self._watch():
            self.queue.put((self.folder, events))

    def _watch(self):
        w_dir = win32file.CreateFile(
            self.folder.path,
            self.FILE_LIST_DIRECTORY,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_FLAG_BACKUP_SEMANTICS,
            None
        )

        while 1:
            results = win32file.ReadDirectoryChangesW(
                w_dir,
                1024,
                self.folder.recursive,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_SIZE |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY,
                None,
                None
            )

            for action, name in results:
                if action not in self.ACTIONS:
                    continue

                maskname = self.ACTIONS[action]
                if not hasattr(self.folder, 'process_{0}'.format(maskname)):
                    continue

                full_path = os.path.join(self.folder.path, name)
                if not os.path.exists(full_path):
                    file_type = 'deleted'
                elif os.path.isdir(full_path):
                    file_type = 'dir'
                else:
                    file_type = 'file'

                events = [FileEvent(file_type, name, full_path, maskname)]

                if file_type == 'dir':
                    events.append(FileEvent(file_type, name, full_path, 'IN_ISDIR'))

                yield events
