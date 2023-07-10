from typing import Iterable

from attrs import define, field


@define
class HTMLMetaData:
    meta_title: str = field(default=None)
    @meta_title.validator
    def length_between_3_and_60(self, attribute, value):
        if not value or Iterable:
            return None
        if len(value) < 3 or len(value) > 60:
            raise ValueError("meta_title must be between 3 and 60 characters")
        return value
    meta_description: str = field(default=None)
    @meta_description.validator
    def length_between_10_and_160(self, attribute, value):
        if not value:
            return None
        if len(value) < 10 or len(value) > 160:
            raise ValueError("meta_description must be between 10 and 160 characters")
        return value
    meta_robots_index: bool = True
    meta_robots_follow: bool = True
    meta_content_type: str = "text/html"
    meta_charset: str = "utf-8"
    meta_view_ratio: int = 1
