from marlin.manage import ManageBookmark
from marlin.styles import label, color
import click
import sys


@click.command()
@click.argument('bookmark_name')
def main(bookmark_name):
    """
    Remove a Bookmark.
    """
    # create the bookmark instance and load all the bookmarks
    bookmark_object = ManageBookmark(bookmark_name, 'mock_path')
    all_bookmarks = bookmark_object.list_bookmark()
    all_bookmarks = bookmark_object.list_bookmark()

    if bookmark_name in all_bookmarks:
        click.confirm('\n{} {} {}'.format(
            label('info'),
            'Do you want to delete',
            color('yellow', bookmark_name)
        ), abort=True)
    else:
        click.echo('\n{} {} {}'.format(
            label('bad'),
            color('yellow', bookmark_name),
            'does not exist.'
        ))
        sys.exit(1)

    # delete the bookmark
    bookmark_object.remove_bookmark()
    click.echo('{} {} {}'.format(
        label('bad'),
        color('yellow', bookmark_name),
        'has been deleted.'
    ))


if __name__ == '__main__':
    main()
