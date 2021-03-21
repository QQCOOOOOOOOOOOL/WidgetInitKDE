"""
This Module is pretty much an easy way to initiate a basic widget directory, for developers (KDE)
"""

from pathlib import Path
import argparse

def parser():
    '''
    Creating a parser
    return -> parser object
    '''

    _parser = argparse.ArgumentParser(description=' :p ')
    _parser.add_argument("dest", action='store', nargs = 1, type = str,
                          help = "Enter the directory which you code",
                          metavar = "Workspace-Directory")
    return _parser.parse_args()


def create_workspace(dest: str):
    '''
    This Function creates the relevant workspace
    Parameters:
    :dest: the destination of the workspace
    :return -> return 1 if succeeded, and raise if didn't..
    '''

    name = input("Enter the name of the directory: ")
    try:
        Path(f"{dest}/{name}").mkdir(parents= True, exist_ok= True)
        Path(f"{dest}/{name}/contents").mkdir(parents = True, exist_ok=True)
        open(f"{dest}/{name}/metadata.desktop", "w+")

        # Sub Dirs for contents
        Path(f"{dest}/{name}/contents/ui").mkdir(parents = True, exist_ok=True)
        Path(f"{dest}/{name}/contents/config").mkdir(parents = True, exist_ok=True)

        # Sub Files for ui
        open(f"{dest}/{name}/contents/ui/main.qml", "w+")
        open(f"{dest}/{name}/contents/ui/configGeneral.qml", "w+")

        #  Sub Files for config
        open(f"{dest}/{name}/contents/config/config.qml", "w+")
        open(f"{dest}/{name}/contents/config/main.xml", "w+")
    except OSError as _e:
        raise _e
    return True



def main():
    '''
    Main Function..
    '''

    try:
        args = parser()
        print(f"Creating a Widget Workspace at => {args.dest[0]}")
        if create_workspace(args.dest[0]):
            print("Done[!] :)")
    except Exception as _e:
        print(_e)

if __name__ == "__main__":
    main()
