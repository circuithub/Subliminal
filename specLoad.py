import sublime, sublime_plugin

class SpecEvents(sublime_plugin.EventListener):
  executing = {}
  TEST_SPEC_NAME = "__ch_test_spec__"
  def __init__(self):
    executing = False
  def on_load(self, view):  
    self.convertSpecFiles(view)
    
  def on_modified(self, view):  
     self.convertSpecFiles(view)

  def convertSpecFiles(self, view):
    if not self.executing:
      if (not view.file_name()):  # output panel
        text = view.substr(sublime.Region(0, view.size()-1))
        if (text.find("Finished in") > -1):
          self.executing = True
          views = view.window().views()
          testView = filter(lambda v: v.name() ==  self.TEST_SPEC_NAME, views)
          if (len(testView) == 0):
            testView = view.window().new_file()
            testView.set_name(self.TEST_SPEC_NAME)
          else:
            testView = testView[0]
          testView.run_command("color_spec_add_text", {"text": text})
          testView.run_command("color_spec")    
          view.window().focus_view(testView)   
          testView.show(0)          
          self.executing = False
          print "Converted ouput spec..."

      elif (view.file_name().find(".spec") != -1):
        self.executing = True
        view.run_command("color_spec")                 
        self.executing = False
        print "Converted spec file: ", view.file_name()
