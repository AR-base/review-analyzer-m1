from app import classify_review, normalize_review


def test_uppercase_text_is_lowercased():
    assert normalize_review("GOOD PRODUCT") == "good product"


def test_leading_and_trailing_spaces_are_removed():
    assert normalize_review("   Good    product   ") == "good product"


def test_unknown_review():
    assert classify_review("Arrived on time") == "unknown"


def test_negative_review():
    assert classify_review("Bad quality, broke after a day") == "negative"


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        t()
    print(f"{len(tests)} tests passed")
