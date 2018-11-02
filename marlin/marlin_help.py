from marlin.manage import ManageBookmark
from marlin.styles import label
import click

commands = {
    'bookmark': '{} {} {}'.format(
        label('good'), 'bookmark'.ljust(15), 'Bookmark current folder'
    ),
    'rmark': '{} {} {}'.format(
        label('bad'), 'rmark'.ljust(15), 'Remove a bookmark'
    ),
    'marlin': '{} {} {}'.format(
        label('run'),
        'marlin'.ljust(15),
        'Swim through the terminal!\n')
}


def main():
    click.echo('Usage: COMMAND [bookmark-name]\n')
    click.echo('Commands:')
    for command in commands:
        click.echo(commands[command])

    list_bookmarks()


def list_bookmarks():
    bookmark_object = ManageBookmark('mock', 'mock')
    all_bookmarks = bookmark_object.list_bookmark()
    click.echo('Saved bookmarks:')
    for bookmark in all_bookmarks:
        bookmark_path = bookmark_object.read_bookmark(bookmark)
        click.echo('{} {} {}'.format(
            label('list'),
            bookmark.ljust(17),
            bookmark_path
        ))


if __name__ == '__main__':
    main()
