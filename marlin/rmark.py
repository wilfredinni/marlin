from marlin.manage import ManageBookmark
from marlin.marlin_batch_maker import make_batch
from marlin.huepy import bad, good, yellow
import click
import sys

# labels
bad = bad('')
good = good('')


@click.command()
@click.argument('name')
def main(name):
    """
    Remove a Bookmark.
    """
    # create the bookmark instance
    bookmark_object = ManageBookmark(ManageBookmark.bookmark_path)
    # load all the bookmarks saved in bookmarks.json
    all_bookmarks = bookmark_object.read_json()

    if name in all_bookmarks:
        click.confirm('\n{}Do you want to delete {}'.format(
            bad, yellow(name)), abort=True)
    else:
        click.echo('\n{}{} does not exist.\n'.format(bad, yellow(name)))
        sys.exit(1)

    # generate, update and store the new bookmarks
    all_bookmarks.pop(name)
    bookmark_object.add_bookmark(all_bookmarks)
    click.echo('{}{} has been deleted.\n'.format(good, yellow(name)))
    make_batch()


if __name__ == '__main__':
    main()
