"""
From Book

"Learning Python Design Patterns", 1st edition, by Zlobin

Chapter 1
"""

import pickle
from typing import Dict


class Url:
    @classmethod
    def shorten(cls, full_url) -> "Url":
        """shortens full url
        1. Creates new Url instance and sets its short_url
           and full_url attributes on the fly
        2. short_url attribute is assigned with new short_url (instance method)
        3. Save new mapping short_url -> full_url into database
        4. Return Url instance
        Args:
            full_url (str): the full url

        """
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        Url.__save_url_mapping(instance)
        return instance

    @classmethod
    def get_by_short_url(cls, short_url) -> "Url":
        """Returns Url instance corresponding to short_url

        Args:
            short_url (str): short url

        Returns:
            dict: url mapping
        """
        url_mapping = Url.__load_url_mapping()
        return url_mapping.get(short_url, None)

    def __create_short_url(self) -> str:
        """
        1. Loads most recently saved url
        2. Creates new short_url by modifying recently saved one (instance method)
        3. Saves new short_url (staticmethod)
        4. Returns new short url (str)
        """
        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)
        return short_url

    def __increment_string(self, string) -> str:
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

        return self.__increment_string(string[:-1]) + "a"

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
    def __save_url_mapping(instance) -> None:
        """Savs short_url to url mapping.

        Args:
            instance (Url): Url instance holding full and short url
        """
        short_to_url = Url.__load_url_mapping()
        short_to_url[instance.short_url] = instance
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))
