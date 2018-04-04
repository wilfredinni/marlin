from marlin.manage import ManageBookmark
from marlin.huepy import info, good, yellow
from marlin.marlin_batch_maker import make_batch
from pathlib import Path
import click
# import os

# labels and long msgs
info = info('')
bookmark_exist = 'alredy exist. Do you want to overwrite it?'


@click.command()
@click.argument('name')
@click.argument('path', default=Path.cwd())
def main(name, path):
    """
    Bookmark the current folder.
    """
    # create the bookmark instance
    bookmark_object = ManageBookmark(ManageBookmark.bookmark_path)
    # load all the bookmarks saved in bookmarks.json
    all_bookmarks = bookmark_object.read_json()

    if name in all_bookmarks:
        click.confirm('\n{}{} {}'.format(info, yellow(name), bookmark_exist
                                         ), abort=True)
    else:
        click.confirm('\n{}Do you want to bookmark {}'.format(
            info, yellow(name)), abort=True)

    # generate, update and store the new bookmark
    new_bookmark = {name: str(path)}
    all_bookmarks.update(new_bookmark)
    bookmark_object.add_bookmark(all_bookmarks)

    click.echo(good('{} has been Bookmarked\n'.format(yellow(name))))
    make_batch()


if __name__ == '__main__':
    main()
