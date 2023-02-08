import sys
import pytest

@pytest.mark.skipif(sys.platform.startswith("win32"), reason="NYI")
def test_main():
    import DiscordBridge
    assert DiscordBridge.TestBridge() == "Make Bridge!"
