import pytest
import os


@pytest.fixture
def rm_pdf():
    yield
    os.remove('tmp.pdf')
