import pytest


def pytest_addoption(parser):
    parser.addoption("--file1", action="store")
    parser.addoption("--file2", action="store")


@pytest.fixture(scope='session')
def file1(request):
    filename = request.config.option.file1
    if filename is None:
        pytest.skip()
    return filename


@pytest.fixture(scope='session')
def file2(request):
    filename = request.config.option.file2
    if filename is None:
        pytest.skip()
    return filename
