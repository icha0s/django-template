from ..common import env

# https://github.com/respondcreate/django-versatileimagefield

VERSATILEIMAGEFIELD_SETTINGS = {
    "cache_length": env.int("VERSATILE_IMAGE_CACHE_LENGTH", default=2592000),  # 30 days
    "cache_name": env.str("VERSATILE_IMAGE_CACHE_NAME", default="default"),
    "jpeg_resize_quality": env.int("VERSATILE_IMAGE_JPEG_RESIZE_QUALITY", default=70),
    "sized_directory_name": "__sized__",
    "filtered_directory_name": "__filtered__",
    "placeholder_directory_name": "__placeholder__",
    "create_images_on_demand": True,
    "image_key_post_processor": None,
    "progressive_jpeg": env.bool("VERSATILE_IMAGE_PROGRESSIVE_JPEG", default=True),
}
VERSATILEIMAGEFIELD_USE_PLACEHOLDIT = True
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    "default": [
        ("400", "thumbnail__400x400"),
        ("800", "thumbnail__800x800"),
        ("1300", "thumbnail__1300x1300"),
        ("1900", "thumbnail__1900x1900"),
        ("3600", "thumbnail__3600x3600"),
    ]
}
VERSATILEIMAGEFIELD_CHECK_PLACEHOLDER_IN_STORAGE = False
