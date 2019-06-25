from .models import Photo
def delete_photo(pk):
    Photo.objects.get(pk=pk).delete()

def new_des(pk,newDes):
    photo = Photo.objects.get(pk=pk)
    photo.description = newDes
    photo.save()