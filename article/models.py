from django.db import models

class category(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
# Create your models here.
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title





# import os
# import mimetypes
# import logging
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.core.exceptions import ValidationError
# from django.db import models
# from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
# from your_app.models import Media, User
#
# logger = logging.getLogger(__name__)
#
#
#

# from django.views import View
# from django.http import JsonResponse
# from your_app.services import BaseService


# class UploadMediaView(View):
#     def post(self, request, *args, **kwargs):
#         service = BaseService()
#         model_instance = YourModel.objects.get(pk=kwargs['pk'])
#
#         try:
#             media_records = service.validate_and_store_media(request, model_instance, path='uploads', is_create_thumbnail=True)
#             return JsonResponse({'status': 'success', 'media': [media.url for media in media_records]})
#         except ValidationError as e:
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': 'Something went wrong'}, status=500)
