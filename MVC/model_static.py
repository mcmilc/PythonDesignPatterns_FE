"""
From Book

"Learning Python Design Patterns", 1st edition, by Zlobin

Chapter 1

Alternative implementation -> target only static methods
"""

import pickle
from typing import Dict


class Url:
    @staticmethod
    def shorten(full_url) -> str:
        """shortens full url

        Args:
            full_url (str): the full url

        """
        short_url = Url.__create_short_url()
        Url.__save_url_mapping(short_url, full_url)
        return short_url

    @staticmethod
    def get_by_short_url(short_url) -> str:
        """Returns Url instance corresponding to short_url

        Args:
            short_url (str): short url

        Returns:
            dict: url mapping
        """
        url_mapping = Url.__load_url_mapping()
        return url_mapping.get(short_url, None)

    @staticmethod
    def __create_short_url() -> str:
        """
        1. Loads most recently saved url
        2. Creates new short_url by modifying recently saved one (instance method)
        3. Saves new short_url (staticmethod)
        4. Returns new short url (str)
        """
        last_short_url = Url.__load_last_short_url()
        short_url = Url.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)
        return short_url

    @staticmethod
    def __increment_string(string) -> str:
        """Increment string, that is:
        a->b
        z->aa
        az->ba
        empty string -> a

        Args:
            string (str): part of previous short url
        """
        if not string:
            return "a"

        last_char = string[-1]
        if last_char != "z":
            return string[:-1] + chr(ord(last_char) + 1)

        return Url.__increment_string(string[:-1]) + "a"

    @staticmethod
    def __load_last_short_url() -> Dict[str, str]:
        """Returns last generated short url."""
        try:
            return pickle.load(open("last_short.p", "rb"))
        except IOError:
            return {}

    @staticmethod
    def __save_last_short_url(short_url) -> None:
        pickle.dump(short_url, open("last_short.p", "wb"))

    @staticmethod
    def __load_url_mapping() -> dict:
        """Returns short_url to url mapping."""
        try:
            return pickle.load(open("short_to_url.p", "rb"))
        except IOError:
            return {}

    @staticmethod
    def __save_url_mapping(short_url, full_url) -> None:
        """Savs short_url to url mapping.

        Args:
            instance (Url): Url instance holding full and short url
        """
        short_to_url = Url.__load_url_mapping()
        short_to_url[short_url] = full_url
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))
