from django.test import TestCase
from .models import Profile,Post

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile = Profile(name="reggo",user_name="reggo",profile_picture="image.jpeg",bio="just testing")
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
class PostTestClass(TestCase):

    def setUp(self):
        self.new_post=Post(sitename="awards",url="#",Description="test app stuff",image="image.jpeg",Technology="basic",country="kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
    

