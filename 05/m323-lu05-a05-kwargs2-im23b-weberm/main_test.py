from main import active_settings


def test_active_settings_no_args():
    assert (
        active_settings() == []
    ), "Should return an empty list when no keyword arguments are passed"


def test_active_settings_single_active_arg():
    assert active_settings(wifi=True) == [
        "wifi"
    ], "Should return a list with the single active setting"


def test_active_settings_multiple_args():
    assert active_settings(wifi=True, bluetooth=False, gps=True) == [
        "wifi",
        "gps",
    ], "Should return a list with multiple active settings"


def test_active_settings_no_active_args():
    assert (
        active_settings(wifi=False, bluetooth=False) == []
    ), "Should return an empty list when no settings are active"
