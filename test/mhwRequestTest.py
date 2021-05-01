import mhwRequest


def test_get_all():
    results = mhwRequest.get_all("locations")
    assert(len(results) > 0)


def test_get_all_wrong_type():
    results = mhwRequest.get_all("asdf")
    assert("error" in results.keys())


def test_get_id():
    results = mhwRequest.get_id("monsters", "2")
    assert(len(results) > 0)
    assert(results["name"] == "Jagras")


def test_get_id_wrong_type():
    results = mhwRequest.get_id("asdf", "2")
    assert("error" in results.keys())


def test_get_id_wrong_id():
    results = mhwRequest.get_id("monsters", "100")
    assert("error" in results.keys())


def test_get_name():
    results = mhwRequest.get_name("monsters", "gaj")
    assert(len(results) > 0)
    assert(results[0]["name"] == "Gajau")


def test_get_name_no_match():
    results = mhwRequest.get_name("monsters", "zzz")
    assert(len(results) == 0)
