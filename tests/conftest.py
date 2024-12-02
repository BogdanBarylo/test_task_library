import os
import pytest
from library_model import Library


@pytest.fixture
def library():
    test_file = "test_library.json"
    lib = Library(file_path=test_file)
    yield lib
    if os.path.exists(test_file):
        os.remove(test_file)
