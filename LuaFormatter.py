import os
import sublime, sublime_plugin, sys
import subprocess


class LuaFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit, error=True, save=True):
        self.filename = self.view.file_name()
        package_path = os.path.split(os.path.dirname(__file__))[1]
        command = os.path.join(
            sublime.packages_path(), package_path, "bin", sys.platform, "lua-format"
        )

        settings = sublime.load_settings("LuaFormatter.sublime-settings")
        config = settings.get("config_file")
        if config:
            process = subprocess.Popen([command, self.filename, "-c", config])
        else:
            process = subprocess.Popen([command, self.filename])
