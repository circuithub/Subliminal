subliminal
==========

Customize the Sublime Editor environment for use with CircuitHub.

Includes: Snippets, Color Schemes, Good Karma, Spec file colouring

## Installation on Mac

### Version 2
`git clone git@github.com:circuithub/subliminal.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/CircuitHub`

### Version 3
`git clone git@github.com:circuithub/subliminal.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/CircuitHub`

## Usage

### Function prototype documentation
Type `'''` (three apostrophes) and hit tab to insert the template. Use the tab key to navigate the template

### Color theme (optional of course)
Navigate via the application top menu: Sublime Text 2 -> Preferences -> Color Scheme -> User -> CircuitHub

### Spec file colouring
To have this work, you have to have the CH-Monokai theme selected (Tomorrow-Night-Blue-Circuits will also work,
but the colouring does not look very good).  
* Whenever a spec file is loaded or modified which has console colour symbols embedded, it will be converted
to have the colours displayed.  
* When running a test directly (via the sublime `run` command), a new window will be opened with the coloured 
output embedded.
