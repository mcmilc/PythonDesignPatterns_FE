import model


def test_shorten():
    input_url = "http://www.example-domain.com/page_1.html"
    url_instance = model.Url.shorten(input_url)
    print(f"Input url {input_url} shortened to {url_instance.short_url}")


def test_get_original():
    url_instance = model.Url.get_by_short_url("a")
    print(
        f"Model output: full_url {url_instance.full_url} -> short_url {url_instance.short_url}"
    )


if __name__ == "__main__":
    test_shorten()
    test_get_original()
