from marlin.manage import ManageBookmark
from marlin.styles import label
import click


bookmark_msg = "Bookmark current folder"
rmark_msg = "Remove a bookmar"
marlin_msg = "Swim through the terminal!\n"

commands = {
    "bookmark": f"{label('good')} {'bookmark'.ljust(15)} {bookmark_msg}",
    "rmark": f"{label('bad')} {'rmark'.ljust(15)} {rmark_msg}",
    "marlin": f"{label('run')} {'marlin'.ljust(15)} {marlin_msg}",
}


def main():
    click.echo("Usage: COMMAND [bookmark-name]\n")
    click.echo("Commands:")
    for cmd in commands:
        click.echo(commands[cmd])

    list_bookmarks()


def list_bookmarks():
    bookmark_object = ManageBookmark("mock", "mock")
    all_bookmarks = bookmark_object.list_bookmark()
    click.echo("Saved bookmarks:")
    for bookmark in all_bookmarks:
        bookmark_path = bookmark_object.read_bookmark(bookmark)
        click.echo(f"{label('list')} {bookmark.ljust(17)} {bookmark_path}")


if __name__ == "__main__":
    main()
