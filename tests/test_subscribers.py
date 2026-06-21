from mailer.subscribers import SubscriberManager


def test_add_and_list():
    mgr = SubscriberManager()
    assert mgr.add("a@example.com") is True
    assert mgr.add("b@example.com") is True
    assert "a@example.com" in mgr.list()


def test_duplicate_add():
    mgr = SubscriberManager()
    assert mgr.add("dup@example.com") is True
    assert mgr.add("dup@example.com") is False


def test_remove():
    mgr = SubscriberManager()
    mgr.add("r@example.com")
    assert mgr.remove("r@example.com") is True
    assert mgr.remove("x@example.com") is False
