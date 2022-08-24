from django.test import TestCase

from expense.models import Expense, Type


class ExpenseModelTest(TestCase):
    '''
    Test suite for Expense model
    '''

    def setUp(self):
        '''
        Create a expense instance for testing
        '''
        Type.objects.create(
            id=1,
            name='Internet'
        )

        Expense.objects.create(
            id=1,
            name="Wifi bill",
            type=Type.objects.first(),
            amount=500,
            note="Bill has been paid",
        )

    def tearDown(self):
        '''
        Delete expense and type instance after testing
        '''
        Expense.objects.all().delete()
        Type.objects.all().delete()

    def test_expense_id(self):
        ''' Test expense type id '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.id, 1)

    def test_type_id(self):
        ''' Test expense type id '''
        type = Type.objects.get(id=1)
        self.assertEqual(type.id, 1)

    def test_expense_type(self):
        ''' Test expense type '''
        expense = Expense.objects.get(id=1)
        type = Type.objects.first()
        self.assertEqual(expense.type, type)

    def test_expense_amount(self):
        ''' Test expense amount '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.amount, 500)

    def test_expense_amount_not_exact(self):
        ''' Test expense amount not equal '''
        expense = Expense.objects.get(id=1)
        self.assertNotEqual(expense.amount, 400)
