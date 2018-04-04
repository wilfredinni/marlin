from marlin.manage import ManageBookmark
from marlin.huepy import bad, yellow
import click
import os

# style
bad = bad('')

workon = os.path.join(
    os.path.dirname(__file__), '.', 'scripts', 'test.bat')


@click.command()
@click.argument('bookmark-name')
def main(bookmark_name):
    """
    Swim between bookmarks in the Terminal.
    """
    bookmark_objetct = ManageBookmark(ManageBookmark.bookmark_path)
    bookmarks = bookmark_objetct.read_json()
    if bookmark_name in bookmarks:
        if os.name == 'posix':
            os.chdir(bookmarks[bookmark_name])
            os.system("/bin/bash")
        else:
            os.chdir(bookmarks[bookmark_name])
    else:
        click.echo('\n{}{} is not Bookmarked.\n'. format(
            bad, yellow(bookmark_name)))


if __name__ == '__main__':
    main()
