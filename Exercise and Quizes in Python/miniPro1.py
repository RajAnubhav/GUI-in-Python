from cProfile import label
from distutils import command
from tkinter import *

root = Tk()
root.title("RA Editor")
root.geometry("800x680")

menuBar = Menu(root)

# ****************    FILE MENU   ***************************
# this is to display the File menu

file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="New File...", command=None)
file.add_command(label="New Window", command=None)

file.add_separator()

file.add_command(label="Open File", command=None)
file.add_command(label="Open Folder", command=None)
file.add_command(label="Open Workspace from File...", command=None)

# a submenu is created
subfile1 = Menu(file, tearoff=0)
subfile1.add_command(label="Reopen Closed Editors...")

subfile1.add_separator()

subfile1.add_command(label="More...")

subfile1.add_separator()

subfile1.add_command(label="Clear Recently Opened")

# this is how we link a subMenu to the mainMenu
file.add_cascade(label="Open Recents", menu=subfile1)

file.add_separator()

file.add_command(label="Add Folder to Workspace...", command=None)
file.add_command(label="Save Workspace As...", command=None)
file.add_command(label="Duplicate Workspace", command=None)

file.add_separator()

file.add_command(label="Save", command=None)
file.add_command(label="Save As...", command=None)
file.add_command(label="Save All", command=None)

file.add_separator()

file.add_command(label="Auto Save", command=None)

# sub Menu 2 for the Preferances
subfile2 = Menu(file, tearoff=0)
subfile2.add_command(label="Setting")
subfile2.add_command(label="Online Services Setting")
subfile2.add_command(label="Telemetry Setting")
subfile2.add_command(label="Exclusions")

subfile2.add_separator()

subfile2.add_command(label="Keyboard Shortcuts")
subfile2.add_command(label="Migrate Keyboard Shortcuts from...")

subfile2.add_separator()

subfile2.add_command(label="User Snippets")

subfile2.add_separator()

subfile2.add_command(label="Color Theme")
subfile2.add_command(label="File Icon Theme")
subfile2.add_command(label="Product Icon Theme")

subfile2.add_separator()

subfile2.add_command(label="Turn on Settings Sync...")

file.add_cascade(label="Preferances", menu=subfile2)

file.add_separator()

file.add_command(label="Revert File", command=None)
file.add_command(label="Close File", command=None)
file.add_command(label="Close Folder", command=None)

file.add_separator()

file.add_command(label="Exit", command=root.destroy)


# **************     EDIT MENU    *********************
# this is to display the edit menu
edit = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo", command=None)
edit.add_command(label="Redo", command=None)

edit.add_separator()

edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)

edit.add_separator()

edit.add_command(label="Find", command=None)
edit.add_command(label="Replace", command=None)

edit.add_separator()

edit.add_command(label="Find in Files", command=None)
edit.add_command(label="Replace in Files", command=None)

edit.add_separator()

edit.add_command(label="Toggle Line Comment", comment=None)
edit.add_command(label="Toggle Block Comment", comment=None)
edit.add_command(label="Emmet: Expand Abbreviation", command=None)


# ***************    SELECTION    **********************
# this will display the selection part of the menu
sel = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Selection", menu=sel)
sel.add_command(label="Select All")
sel.add_command(label="Expand Selection")
sel.add_command(label="Shrink Selction")

sel.add_separator()

sel.add_command(label="Copy Line Up")
sel.add_command(label="Copy Line Down")
sel.add_command(label="Move Line Up")
sel.add_command(label="Move Line Down")
sel.add_command(label="Duplicate Selection")

sel.add_separator()

sel.add_command(label="Add Cursor Above")
sel.add_command(label="Add Cursor Below")
sel.add_command(label="Add Cursor to Line Ends")
sel.add_command(label="Add Next Occurance")
sel.add_command(label="Add Previous Occurance")
sel.add_command(label="Select All Occurances")

sel.add_separator()

sel.add_command(label="Switch to Ctrl+Click for Multi-Cursor")
sel.add_command(label="Column Selection Mode")

#**************     VIEW    ***********************
# this will show the view part of the menu

view = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="View", menu=view)
view.add_command(label="Command Palette...")
view.add_command(label="Open View...")

view.add_separator()

# this will create the 3rd subfile
subfile3 = Menu(view, tearoff=0)
subfile3.add_command(label="Full Screen")
subfile3.add_command(label="Zen Mode")
subfile3.add_command(label="Centered Layout")

subfile3.add_separator()

subfile3.add_checkbutton(label="Show Menu Bar")
subfile3.add_checkbutton(label="Show Side Bar")
subfile3.add_checkbutton(label="Show Status Bar")
subfile3.add_checkbutton(label="Show Activity Bar")
subfile3.add_checkbutton(label="Show Panel")
subfile3.add_checkbutton(label="Show Side Panel")

subfile3.add_separator()

subfile3.add_command(label="Move Side Bar Right")

# this is for the subSubfile1
subSubfile1 = Menu(subfile3, tearoff=0)
subSubfile1.add_checkbutton(label="Bottom")
subSubfile1.add_checkbutton(label="Left")
subSubfile1.add_checkbutton(label="Right")

# this is for the subSubfile2
subSubfile2 = Menu(subfile3, tearoff=0)
subSubfile2.add_checkbutton(label="Center")
subSubfile2.add_checkbutton(label="Justify")
subSubfile2.add_checkbutton(label="Left")
subSubfile2.add_checkbutton(label="Right")

subfile3.add_cascade(label="Panel Position", menu=subSubfile1)
subfile3.add_cascade(label="Align Position", menu= subSubfile2)

subfile3.add_separator()

subfile3.add_command(label="Zoom In")
subfile3.add_command(label="Zoom Out")
subfile3.add_command(label="Reset Zoom")

view.add_cascade(label="Appearance", menu=subfile3)

# this is for the subfile4 of the Editor Layout in the View Section
subfile4 = Menu(view, tearoff=0)
view.add_cascade(label="Editor Layout", menu=subfile4)

subfile4.add_command(label="Split Up")
subfile4.add_command(label="Split Down")
subfile4.add_command(label="Split Left")
subfile4.add_command(label="Split Right")

subfile4.add_separator()

subfile4.add_command(label="Split in Group")

subfile4.add_separator()

subfile4.add_command(label="Single")
subfile4.add_command(label="Two Columns")
subfile4.add_command(label="Three Columns")
subfile4.add_command(label="Two Rows")
subfile4.add_command(label="Three Rows")
subfile4.add_command(label="Grid (2x2)")
subfile4.add_command(label="Two Rows Right")
subfile4.add_command(label="Two Columns Bottom")

subfile4.add_separator()

subfile4.add_command(label="Flip Layout")

view.add_separator()

view.add_command(label="Explorer")
view.add_command(label="Search")
view.add_command(label="SCM")
view.add_command(label="Run")
view.add_command(label="Extensions")

view.add_separator()

view.add_command(label="Problems")
view.add_command(label="Output")
view.add_command(label="Debug Console")
view.add_command(label="Terminal")

view.add_separator()

view.add_command(label="Word Wrap")
view.add_checkbutton(label="Show Minimap")
view.add_checkbutton(label="Show Breadcrumbs")
view.add_checkbutton(label="Show Whitespace")
view.add_checkbutton(label="Render Control Characters")

# **************    GO    *****************
# this is for go option in the menu bar
go = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Go", menu=go)
go.add_command(label="Back")
go.add_command(label="Forward")
go.add_command(label="Last Edit Location")

go.add_separator()

subSubfile3 = Menu(go, tearoff=0)
go.add_cascade(label="Switch Editor", menu=subSubfile3)
subSubfile3.add_command(label="Next Editor")
subSubfile3.add_command(label="Previous Editor")

subSubfile3.add_separator()

subSubfile3.add_command(label="Next Used Editor")
subSubfile3.add_command(label="Previous Used Editor")

subSubfile3.add_separator()

subSubfile3.add_command(label="Next Editor in Group")
subSubfile3.add_command(label="Previous Editor in Group")

subSubfile3.add_separator()

subSubfile3.add_command(label="Next Used Editor in Group")
subSubfile3.add_command(label="Previous Used Editor in Group")

subSubfile4 = Menu(go, tearoff=0)
go.add_cascade(label="Switch Group", menu=subSubfile4)

subSubfile4.add_command(label="Group1")
subSubfile4.add_command(label="Group2")
subSubfile4.add_command(label="Group3")
subSubfile4.add_command(label="Group4")
subSubfile4.add_command(label="Group5")

subSubfile4.add_separator()

subSubfile4.add_command(label="Next Group")
subSubfile4.add_command(label="Previous Group")

subSubfile4.add_separator()

subSubfile4.add_command(label="Group Left")
subSubfile4.add_command(label="Group Right")
subSubfile4.add_command(label="Group Above")
subSubfile4.add_command(label="Group Below")

go.add_separator()

go.add_command(label="Go to File...")
go.add_command(label="Go to Symbol in Workspace...")

go.add_separator()

go.add_command(label="Go to Symbol in Editor...")
go.add_command(label="Go to Definition")
go.add_command(label="Go to Declaration")
go.add_command(label="Go to Type Definition")
go.add_command(label="Go to Implementations")
go.add_command(label="Go to References")

go.add_separator()

go.add_command(label="Go to Line/Column...")
go.add_command(label="Go to Bracket")

go.add_separator()

go.add_command(label="Next Problem")
go.add_command(label="Previous Problem")

go.add_separator()

go.add_command(label="Next Change")
go.add_command(label="Previous Change")

#***********    Run     *************
# this is the run menu in the menu bar

run  = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Run", menu=run)
run.add_command(label="Start Debugging")
run.add_command(label="Run Without Debugging")
run.add_command(label="Stop Debugging")
run.add_command(label="Restart Debugging")

run.add_separator()

run.add_command(label="Open Configurations")
run.add_command(label="Add Configuration...")

run.add_separator()

run.add_command(label="Step Overr")
run.add_command(label="Step Info")
run.add_command(label="Step Out")
run.add_command(label="Continue")

run.add_separator()

run.add_command(label="Toggle Breakpoint")

# this is the subfile5
subfile5 = Menu(run, tearoff=0)
run.add_cascade(label="New Breakpoint", menu=subfile5)
subfile5.add_command(label="Conditional Breakpoint...")
subfile5.add_command(label="Inline Breakpoint...")
subfile5.add_command(label="Functional Breakpoint...")
subfile5.add_command(label="Logpoint")

run.add_separator()

run.add_command(label="Enable All Breakpoints")
run.add_command(label="Desible All Breakpoints")
run.add_command(label="Remove All Breakpoints")
run.add_command(label="Install Additional Debuggers...")

#******************      TERMINAL MENU       ******************
# this is the terminal menu in the menu bar
terminal = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Terminal", menu=terminal)
terminal.add_command(label="New Terminal")
terminal.add_command(label="Split Terminal")

terminal.add_separator()

terminal.add_command(label="Run Task...")
terminal.add_command(label="Run Build Task...")
terminal.add_command(label="Run Active File")
terminal.add_command(label="Run Selected Text")

terminal.add_separator()

terminal.add_command(label="Show Running Tasks...")
terminal.add_command(label="Restart Running Tasks...")

terminal.add_separator()

terminal.add_command(label="Terminate Task...")
terminal.add_command(label="Configure Tasks...")
terminal.add_command(label="Configure Default Build Task...")

#*********************      HELP MENU    *************************
# this is the help menu in the menu bar

helP = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helP)
helP.add_command(label="Get Started")
helP.add_command(label="Show All Commands")
helP.add_command(label="Documentation")
helP.add_command(label="Editor Playgroud")
helP.add_command(label="Release Notes")

helP.add_separator()

helP.add_command(label="Keyboard Shortcuts Reference")
helP.add_command(label="Video Tutorials")
helP.add_command(label="Tips and Tricks")

helP.add_separator()

helP.add_command(label="Join Us on Twitter")
helP.add_command(label="Search Feature Requests")
helP.add_command(label="Report Issue")

helP.add_separator()

helP.add_command(label="View License")
helP.add_command(label="Privacy Statement")

helP.add_separator()

helP.add_command(label="Toggle Developer Tools")
helP.add_command(label="Open Process Explorer")

helP.add_separator()

helP.add_command(label="Check for Updates...")

helP.add_separator()

helP.add_command(label="About")

# display Menus
root.config(menu=menuBar)

root.mainloop()
