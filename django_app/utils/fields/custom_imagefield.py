from django.db.models.fields.files import ImageFieldFile, ImageField
from django.conf import settings
from django.utils.module_loading import import_string

__all__ = (
    'CustomImageField',
)


class CustomImageFieldFile(ImageFieldFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.name and self.field.static_image_path:
            self.name = self.field.static_image_path
            self.storage = import_string(settings.STATICFILES_STORAGE)()


class CustomImageField(ImageField):
    attr_class = CustomImageFieldFile

    def __init__(self, *args, **kwargs):
        self.static_image_path = kwargs.pop('default_static_image', 'images/no_image.png')
        super().__init__(*args, **kwargs)
