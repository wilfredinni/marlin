from marlin.manage import ManageBookmark
from marlin.styles import label, color
import click
import sys


@click.command()
@click.argument("bookmark_name")
def main(bookmark_name):
    """
    Remove a bookmark.
    """
    # create the bookmark instance and load all the bookmarks
    bookmark_object = ManageBookmark(bookmark_name, "mock_path")
    all_bookmarks = bookmark_object.list_bookmark()

    if bookmark_name in all_bookmarks:
        click.confirm(msg_delete(bookmark_name), abort=True)
    else:
        click.echo(msg_not_exist(bookmark_name))
        sys.exit(1)

    # delete the bookmark
    bookmark_object.remove_bookmark()
    click.echo(msg_deleted(bookmark_name))


def msg_delete(bookmark_name):
    msg = "Do you want to delete"
    return f"\n{label('info')} {msg} {color('yellow', bookmark_name)}"


def msg_not_exist(bookmark_name):
    msg = "does not exist."
    return f"\n{label('bad')} {color('yellow', bookmark_name)} {msg}"


def msg_deleted(bookmark_name):
    msg = "has been deleted."
    return f"{label('bad')} {color('yellow', bookmark_name)} {msg}"


if __name__ == "__main__":
    main()
