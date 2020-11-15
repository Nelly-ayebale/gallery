from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def photos(cls):
        photos = cls.objects.all()
        return photos
    
    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id=id).update(image=image)

    
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__category_of_pic__icontains=search_term)
        return photos
    
    @classmethod
    def filter_by_location(cls,location):
        photo_location = Photo.objects.filter(location__location_of_pic=location)
    
    @classmethod
    def get_image_by_id(cls, id):
        photos = cls.objects.filter(id=id).all()
        return photos


class Location(models.Model):
    location_of_pic = models.CharField(max_length=50)

    def __str__(self):
        return self.location_of_pic
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def locations(cls):
        locations = cls.objects.all()
        return locations

    @classmethod
    def update_location(cls,id,new_location):
        cls.objects.filter(id=id).update(location_of_pic=new_location)

class Category(models.Model):
    category_of_pic = models.CharField(max_length=50)

    def __str__(self):
        return self.category_of_pic
        
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    @classmethod
    def categories(cls):
        categories = cls.objects.all()
        return categories
    
    @classmethod
    def update_category(cls,id,new_category):
        cls.objects.filter(id=id).update(category_of_pic=new_category)
    

