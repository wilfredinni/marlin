from marlin.manage import ManageBookmark
from pathlib import Path

# new test path
marlin_path = Path((Path.home()) / '.test_marlin')
mock_object = ManageBookmark('mock', 'mock_path', marlin_path)


def test_create_marlin_folder():
    mock_object.create_marlin_folder()
    exists = Path(marlin_path).exists()
    # assert exists is True
    if not exists:
        raise AssertionError()


def test_add_bookmark():
    mock_object.add_bookmark()
    bookmark = Path((marlin_path) / 'mock')
    exists = Path(bookmark).exists()
    assert exists is True


def test_read_bookmark():
    mock_path = mock_object.read_bookmark('mock')
    assert mock_path == 'mock_path'


def test_list_bookmark():
    list_bookmark = mock_object.list_bookmark()
    assert isinstance(list_bookmark, list)


def test_remove_bookmark():
    mock_object.remove_bookmark()
    bookmark = Path((marlin_path) / 'mock')
    exists = Path(bookmark).exists()
    # assert exists is False
    if exists is not False:
        raise AssertionError()
