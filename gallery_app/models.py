from django.db import models



# Create your models here.

class category(models.Model):
    name = models.Charfield(max_length = 35)

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

class location(models.Model):
    name = models. Charfield(max_length = 35)

    def __str__(self):
        return self.name

    def save_loc(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='photos/', blank=True)
    name = models.CharField(max_length=35)
    description=models.CharField(max_length=200)
    my_image = models.ImageField(upload_to ='photos/', blank=True)
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,photo_id):
        images = cls.objects.filter(photo_id=photo_id)
        return images


    @classmethod
    def current_images(cls,location):
        images = cls.objects.filter(location_in= location)
        return images

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category_name_icontains = search_term)
        return photos
    @classmethod
    def find_by_location(cls,search_location):
        photos = cls.objects.filter(location__name__incontains = search_term)
        return photos  