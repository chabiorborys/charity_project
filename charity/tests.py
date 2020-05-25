from django.test import TestCase
from charity.models import Institution, Category


class InstitutionTestCase(TestCase):
    def setUp(self):
        # Category.objects.create(name='C')
        Institution.objects.create(name="A",
                                   description="d",
                                   type=Institution.FOUNDATION
                                   )
        Institution.objects.create(name="B",
                                   description="x",
                                   type=Institution.NONPROFIT
                                   )


    def test_abc(self):
        i = Institution.objects.get(name='A')
        y = Institution.objects.get(name='B')
        self.assertEqual(i.is_foundation(), True)
        self.assertEqual(y.is_foundation(), False)
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_all_foundations(self):
        x = Institution.all_foundations()
        self.assertEqual(len(x),1)
        self.assertEqual(x[0].name,'A')

    def test_all_nonprofits(self):
        x = Institution.all_nonprofits()
        self.assertEqual(len(x),1)
        self.assertEqual(x[0].name,'B')


