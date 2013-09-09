Subliminal
==========

Customize the Sublime Editor environment for use with CircuitHub.

Includes: Snippets, Color Schemes, Good Karma, Spec file colouring

## Installation on Mac

### Install "Package Control" 

If not already installed:
1. View -> Show Console
2. Enter ```import urllib2,os; pf='Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler( ))); open( os.path.join( ipp, pf), 'wb' ).write( urllib2.urlopen( 'http://sublime.wbond.net/' +pf.replace( ' ','%20' )).read()); print( 'Please restart Sublime Text to finish installation')```python

### Add the repository to Package Control
1. Open the add-on menu (Command-Shift-P)
2. Execute "Package Control: Add Repository"
3. Enter: ```https://github.com/circuithub/Subliminal```

### Install the package
1. Open the add-on menu (Command-Shift-P)
2. Execute "Package Control: Install Package"
3. (wait for repositories to be scanned)
4. Select "Subliminal" from the resulting package list



## Usage

### Function prototype documentation
Type `'''` (three apostrophes) and hit tab to insert the template. Use the tab key to navigate the template

### Console log comment block
Type ``` (three backticks) and hit tab to insert the template. Use the tab key to navigate.

### Color theme (optional of course)
Navigate via the application top menu: Sublime Text 2 -> Preferences -> Color Scheme -> Subliminal
