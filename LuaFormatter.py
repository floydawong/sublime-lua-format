import os
import sublime, sublime_plugin, sys
import subprocess

def plugin_loaded():
    init_config_file()

def init_config_file():
    config_path = os.path.join(sublime.packages_path(), "User", 'lua_style')




class LuaFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit, error=True, save=True):
        # check whether the lua files
        suffix_setting = self.view.settings().get("syntax")
        file_suffix = suffix_setting.split(".")[0]
        if file_suffix[-3:].lower() != "lua":
            return

        # check whether filename is None
        filename = self.view.file_name()
        if filename is None:
            return

        # run lua-format
        package_path = os.path.split(os.path.dirname(__file__))[1]
        executable_path = os.path.join(
            sublime.packages_path(), package_path, "bin", sys.platform, "lua-format"
        )

        lua_style = os.path.join(os.path.dirname(__file__), "lua_style")
        process = subprocess.Popen([executable_path, filename, "-c", lua_style])
