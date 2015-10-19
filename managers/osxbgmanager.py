import subprocess


class OsxBgManager:

    def __init__(self):
        self.script = """/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "%s"
        end tell
        END"""

    def set_background(self, background_file):
        subprocess.Popen(self.script % background_file, shell=True)
