from app.queries.brute_force import check_user


def test_known_user_exists():
    assert check_user("alice@example.com") is True


def test_unknown_user_does_not_exist():
    assert check_user("nonexistent_123456@example.com") is False
