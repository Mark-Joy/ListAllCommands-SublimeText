### https://stackoverflow.com/questions/48656430/how-to-list-all-commands-in-sublime-text-3
import sublime, sublime_plugin, inspect

class ListAllCommandsCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.view = self.window.new_file()
    self.view.set_scratch(True)
    self.view.set_name("Command List")

    self.list_category("Application Commands", sublime_plugin.application_command_classes)
    self.list_category("Window Commands", sublime_plugin.window_command_classes)
    self.list_category("Text Commands", sublime_plugin.text_command_classes)

  def append(self, line):
    self.view.run_command("append", {"characters": line + "\n"})

  def list_category(self, title, command_list):
    self.append(title)
    self.append(len(title)*"=")

    for command in command_list:
      self.append("{cmd} {args}".format(
        cmd=self.get_name(command),
        args=str(inspect.signature(command.run))))

    self.append("")

  def get_name(self, cls):
    clsname = cls.__name__
    name = clsname[0].lower()
    last_upper = False
    for c in clsname[1:]:
      if c.isupper() and not last_upper:
        name += '_'
        name += c.lower()
      else:
        name += c
      last_upper = c.isupper()
    if name.endswith("_command"):
      name = name[0:-8]
    return name
