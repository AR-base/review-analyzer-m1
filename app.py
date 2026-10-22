def normalize_review(text):
    return " ".join(text.lower().split())


def classify_review(text):
    normalized = normalize_review(text)
    if "bad" in normalized:
        return "negative"
    return "positive" if "good" in normalized else "unknown"


if __name__ == "__main__":
    print(classify_review("Good product"))
