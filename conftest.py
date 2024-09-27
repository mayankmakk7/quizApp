import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Hook for setting up reporting directories or global configurations
    pass
