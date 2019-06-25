from .models import Photo
def deletePhoto(pk):
    Photo.objects.get(pk=pk).delete()
