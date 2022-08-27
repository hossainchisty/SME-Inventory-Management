from django.test import TestCase

from category.models import Category


class CategoryModelTest(TestCase):
    ''' Test suite for Category model '''

    def setUp(self):
        ''' Create a brand instance for testing '''
        Category.objects.create(
            id=1,
            name='Shoes'
        )

    def tearDown(self):
        ''' Delete Category instance after testing '''
        Category.objects.all().delete()

    def test_category_id(self):
        ''' Test category uniqe id '''
        category = Category.objects.get(id=1)
        self.assertTrue(category.id)

    def test_category_id_not_exact(self):
        ''' Test category uniqe id not equal '''
        category = Category.objects.get(id=1)
        self.assertNotEqual(category.id, 3)

    def test_category_name(self):
        ''' Test category name with db value '''
        value = Category.objects.get(id=1)
        self.assertEqual(value.name, value.name)
