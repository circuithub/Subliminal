import sublime, sublime_plugin

# only supports (a few) colors for now
# could be cleaned up, but I don't really see much value
# in doing that right now
class ColorSpecCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      undoStyle = '\x1B[39m'
      styles = [ 
        ('ch.grey',     '\x1B[90m'),
        ('ch.blue',     '\x1B[34m'),
        ('ch.green',    '\x1B[32m'),
        ('ch.magenta',  '\x1B[35m'),
        ('ch.red',      '\x1B[31m'),
        ('ch.yellow',   '\x1B[33m'),
      ]

      # styleRegions = v.find_all('\x1B\[[^A-Za-z]*m')
      v = self.view
      version = int(sublime.version())
      print(version)

      prevPosition = 0
      styleToUse = ''
      while True:
        r = v.find(r'\x1B\[[^A-Za-z]*m',prevPosition)
        if (r == None or r.empty()):  # sublime 2/3 compatibility
          if not styleToUse == '':
            if (version >= 3000):
              v.add_regions('color_'+str(prevPosition), [sublime.Region(prevPosition, v.size())], styleToUse, '', sublime.DRAW_NO_OUTLINE)          
            else:
              v.add_regions('color_'+str(prevPosition), [sublime.Region(prevPosition, v.size())], styleToUse)    
          break      
        startPosition = r.begin()
        text = v.substr(r)
        v.erase(edit, r)
       
        if not styleToUse == '':
          if (version >= 3000):
            v.add_regions('color_'+str(prevPosition), [sublime.Region(prevPosition, startPosition)], styleToUse, '', sublime.DRAW_NO_OUTLINE)          
          else:
            v.add_regions('color_'+str(prevPosition), [sublime.Region(prevPosition, startPosition)], styleToUse)          

        if text == undoStyle:
          styleToUse = ''
        for s in styles:
          if (s[1] == text):
            styleToUse = s[0]
        prevPosition = startPosition

class ColorSpecAddTextCommand(sublime_plugin.TextCommand):
   def run(self, edit, text):
      self.view.insert(edit, 0, text)
      self.view.insert(edit, 0, "=============================================\n")
      self.view.insert(edit, 0, "=                                           =\n")
      self.view.insert(edit, 0, "=                  NEW test                 =\n")
      self.view.insert(edit, 0, "=                                           =\n")
      self.view.insert(edit, 0, "\n=============================================\n")
