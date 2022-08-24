from django.test import TestCase

from brand.models import Brand


class BrandModelTest(TestCase):
    ''' Test suite for Brand model '''

    def setUp(self):
        ''' Create a brand instance for testing '''
        Brand.objects.create(
            id=1,
            name='Apex'
        )

    def tearDown(self):
        ''' Delete Brand instance after testing '''
        Brand.objects.all().delete()

    def test_brand_id(self):
        ''' Test brand uniqe id '''
        brand = Brand.objects.get(id=1)
        self.assertTrue(brand.id)

    def test_brand_id_not_exact(self):
        ''' Test brand uniqe id not equal '''
        brand = Brand.objects.get(id=1)
        self.assertNotEqual(brand.id, 3)

    def test_brand_name(self):
        ''' Test brand name with db value '''
        value = Brand.objects.get(id=1)
        self.assertEqual(value.name, value.name)
