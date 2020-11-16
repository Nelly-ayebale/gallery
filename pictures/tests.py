from django.test import TestCase
from .models import Photo,Location,Category
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.Kampala = Location(location_of_pic='Kampala')
        self.Kampala.save_location()
    
    def tearDown(self):
        Location.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.Kampala,Location))
    
    def test_save_location(self):
        self.Kampala.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==1)
    
    def test_delete_location(self):
        self.Kampala.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)
    
    def test_update_location(self):
        new_location = 'Wakiso'
        self.Kampala.update_location(self.Kampala.id, new_location)
        newest_location = Location.objects.filter(location_of_pic='Wakiso')
        self.assertTrue(len(newest_location)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Food = Category(category_of_pic='Food')
       

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,Category))

    def test_save_category(self):
        self.Food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    

    
    
class PhotoTestClass(TestCase):
    def setUp(self):
        self.Kampala = Location(location_of_pic='Kampala')
        self.Kampala.save_location()

        self.Food = Category(category_of_pic='Food')
        self.Food.save_category()

        self.new_image = Photo(image='photo.jpg',name='Pork',description='Best in town!',location=self.new_location,category=self.new_category)
        self.new_image.save()

        def tearDown(self):
            Photo.objects.all().delete()
            Location.objects.all().delete()
            Category.objects.all().delete()

        def test_instance(self):
            self.assertTrue(isinstance(self.new_image,Photo))
        
        def test_save_image(self):
            self.new_image.save_image()
            photos = Photo.objects.all()
        
        def test_delete_image(self):
            self.new_image.save_image()
            self.new_image.delete_image()
        
        def test_update_image(self):
            self.new_image.save_image()
            self.new_image.update_image(self.new_image.id, 'photo.jpg')
            newest_image = Photo.objects.filter(image= 'photo.jpg')
            self.assertTrue(len(newest_image) > 0)
        
        def test_search_by_category(self):
            category = 'Cats'
            images_found = self.new_image.search_by_category(category)
            self.assertTrue(len(images_found) > 1)

        def test_filter_by_location(self):
            self.new_image.save_image()
            image_found = self.new_image.filter_by_location(location='Kampala')
            self.assertTrue(len(image_found) ==1)
        
        def test_get_image_by_id(self):
            got_image = self.new_image.get_image_by_id(self.new_image.id,'photo.jpg')
            photo = Photo.objects.filter(id=self.new_image.id)
            self.assertTrue(got_image,photo)
        

        
