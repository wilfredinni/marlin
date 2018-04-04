import os
from marlin.manage import ManageBookmark


head = """@ECHO OFF
set bookmark=%1
if [%bookmark%]==[] goto :none
"""

bat_file = os.path.join(
    os.path.dirname(__file__), 'scripts', 'marlin.bat')


def ifs():
    bookmark_objetc = ManageBookmark(ManageBookmark.bookmark_path)
    all_bookmarks = bookmark_objetc.read_json()
    # if and goto
    if_goto = ''
    for bookmark in all_bookmarks:
        if_goto += '{}{} {}{}\n'.format(
            'if %bookmark%==',
            bookmark,
            'goto :',
            bookmark
        )
    return if_goto


def labels():
    bookmark_objetc = ManageBookmark(ManageBookmark.bookmark_path)
    all_bookmarks = bookmark_objetc.read_json()
    # labels
    labels = str()
    for bookmark in all_bookmarks:
        labels += '{}{}{}'.format(':', bookmark, '\n')
        labels += '{} {}{}'.format('cd', all_bookmarks[bookmark], '\n')
        labels += '{}{}'.format('exit /b 0', '\n')
    return labels


def make_batch():
    bat = '{}{}{}{}'.format(
        head,
        ifs(),
        ':none\necho hola mundo\nexit /b 0\n',
        labels()
    )
    with open(bat_file, 'w') as f:
        f.write(bat)


if __name__ == '__main__':
    make_batch()
