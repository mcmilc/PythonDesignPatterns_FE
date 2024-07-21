import model_static as model


def test_shorten():
    input_url = "http://www.example-domain.com/page_1.html"
    short_url = model.Url.shorten(full_url=input_url)
    print(f"Input url {input_url} shortened to {short_url}")


def test_get_original():
    short_url = "a"
    full_url = model.Url.get_by_short_url(short_url)
    print(f"Model output: full_url {full_url} -> short_url {short_url}")


if __name__ == "__main__":
    test_shorten()
    test_get_original()
