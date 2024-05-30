from enum import Enum

class MediaType(Enum):
    VIDEO = "VIDEO"
    PHOTO = "PHOTO"
    STREAM = "STREAM"

class PlatformType(Enum):
    TW = "TWITCH"
    YT = "YOUTUBE"
    IM = "IMGUR"

class CategoryType(Enum):
    GAMEPLAY = "GAMEPLAY"
    TUTORIAL = "TUTORIAL"
    REVIEW = "REVIEW"
    CLIP = "CLIP"
    STREAM = "STREAM"
    SHORT = "SHORT"
    OTHER = "OTHER"