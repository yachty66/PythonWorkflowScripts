import os
depth = 2

# [1] abspath() already acts as normpath() to remove trailing os.sep
#, and we need ensures trailing os.sep not exists to make slicing accurate. 
# [2] abspath() also make /../ and ////, "." get resolved even though os.walk can returns it literally.
# [3] expanduser() expands ~
# [4] expandvars() expands $HOME
# WARN: Don't use [3] expanduser and [4] expandvars if stuff contains arbitrary string out of your control.
#stuff = os.path.expanduser(os.path.expandvars(stuff)) # if trusted source
stuff = os.path.abspath('/Users/maxhager/Projects2022')

for root,dirs,files in os.walk(stuff):
    if root[len(stuff):].count(os.sep) < depth:
        for f in files:
            print(os.path.join(root,f))
        