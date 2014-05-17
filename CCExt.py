import sublime, sublime_plugin, os, subprocess, webbrowser
from os.path import dirname, realpath

extid = "com.example.ext"
PLUGIN_PATH = dirname(realpath(__file__))
SDK_PATH = PLUGIN_PATH + "/cc-ext-sdk/"
CEP_PATH = os.path.expanduser("~")+"/Library/Application Support/Adobe/CEPServiceManager4/"
CEP_EXT_PATH = CEP_PATH + "extensions/"


class CreateextCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().show_input_panel("Extension ID:", extid, self.on_done, None, None)
		pass

	def on_done(self, text):
		global extid
		extid = text
		self.view.window().run_command("exec", {"cmd": [SDK_PATH + "createext.sh",  "default",  text]});
		#ugly timeout until I understand how to deal with async file creation
		sublime.set_timeout(self.openDebugFile, 300);

	def openDebugFile(self):
		debugview = self.view.window().open_file(CEP_EXT_PATH + extid + "/.debug");
		#ugly timeout until I understand how to deal with async file creation
		sublime.set_timeout(lambda:self.replaceDebugId(debugview), 300);

	def replaceDebugId(self, v):
		v.window().run_command("replaceid")
		v.window().run_command("save")
		manifview = v.window().open_file(CEP_EXT_PATH + extid + "/CSXS/manifest.xml");
		#ugly timeout until I understand how to deal with async file creation
		sublime.set_timeout(lambda:self.replaceId(manifview), 300);

	def replaceId(self, v):
		v.window().run_command("replaceid")
		v.window().run_command("save")


class EnabledebugCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().run_command("exec", {"cmd":[SDK_PATH + "setdebugmode.sh"]});



class FixpermissionsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		subprocess.call(["chmod", "-R", "755", SDK_PATH ]);



class ShowdevtoolsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		# Warning: Static debugging port
		webbrowser.open_new_tab("http://localhost:8088" );



class ReplaceidCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		matches = reversed(self.view.find_all("com.example.ext"))
		for region in matches:
			self.view.replace(edit, region, extid)



class ShowextfolderCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().run_command("open_dir", {"dir": CEP_EXT_PATH});


