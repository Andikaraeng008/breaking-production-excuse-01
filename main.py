import os

TEXT = "The deploy passed all 400 tests. Unfortunately, production was test number 401."


def main():
    assert 1 <= len(TEXT) <= 180 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
