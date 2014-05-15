import sublime, sublime_plugin, os, subprocess, webbrowser

extid = "com.example.ext"

class CreateextCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().show_input_panel("Extension ID:", extid, self.on_done, None, None)
		pass

	def on_done(self, text):
		global extid
		extid = text
		self.view.window().run_command("exec", {"cmd":[sublime.packages_path() + "/CCExtensions/cc-ext-sdk/createext.sh",  "default",  text]});
		#ugly timeout until I understand how to deal with async file creation
		sublime.set_timeout(self.openManifest, 500);

	def openManifest(self):
		self.manifview = self.view.window().open_file(os.path.expanduser("~")+"/Library/Application Support/Adobe/CEPServiceManager4/extensions/"+extid+"/CSXS/manifest.xml");
		#ugly timeout until I understand how to deal with async file creation
		sublime.set_timeout(self.replaceId, 500);

	def replaceId(self):
		self.manifview.window().run_command("replaceid")
		self.manifview.window().run_command("save")



class EnabledebugCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().run_command("exec", {"cmd":[sublime.packages_path() + "/CCExtensions/cc-ext-sdk/setdebugmode.sh"]});



class FixpermissionsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		subprocess.call(["chmod", "-R", "755", sublime.packages_path() + "/CCExtensions/cc-ext-sdk/"]);



class ShowdevtoolsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		webbrowser.open_new_tab("http://localhost:8088" );



class ReplaceidCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		matches = reversed(self.view.find_all("com.example.ext"))
		for region in matches:
			self.view.replace(edit, region, extid)



class ShowextfolderCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		self.view.window().run_command("open_dir", {"dir": os.path.expanduser("~")+"/Library/Application Support/Adobe/CEPServiceManager4/extensions/"});


