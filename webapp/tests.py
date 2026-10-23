from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import CreateRecordForm
from .models import Category, Record


class RecordAccessTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password='Pass12345!x')
        self.bob = User.objects.create_user('bob', password='Pass12345!x')
        self.category = Category.objects.create(name='GYM')
        self.record = Record.objects.create(
            owner=self.alice, first_name='Ali', last_name='Hassan',
            category=self.category, phone='01012345678', address='Zagazig',
        )

    def test_owner_can_view_record(self):
        self.client.login(username='alice', password='Pass12345!x')
        response = self.client.get(reverse('viewrecord', args=[self.record.id]))
        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_view_record(self):
        self.client.login(username='bob', password='Pass12345!x')
        response = self.client.get(reverse('viewrecord', args=[self.record.id]))
        self.assertEqual(response.status_code, 404)

    def test_other_user_cannot_delete_record(self):
        self.client.login(username='bob', password='Pass12345!x')
        self.client.post(reverse('deleterecord', args=[self.record.id]))
        self.assertTrue(Record.objects.filter(id=self.record.id).exists())

    def test_owner_can_delete_record_with_post(self):
        self.client.login(username='alice', password='Pass12345!x')
        self.client.post(reverse('deleterecord', args=[self.record.id]))
        self.assertFalse(Record.objects.filter(id=self.record.id).exists())

    def test_delete_with_get_is_not_allowed(self):
        self.client.login(username='alice', password='Pass12345!x')
        response = self.client.get(reverse('deleterecord', args=[self.record.id]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Record.objects.filter(id=self.record.id).exists())

    def test_anonymous_user_is_redirected_from_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_create_sets_owner_to_current_user(self):
        self.client.login(username='bob', password='Pass12345!x')
        self.client.post(reverse('createrecord'), {
            'first_name': 'Sara',
            'last_name': 'Nabil',
            'category': self.category.id,
            'phone': '01112345678',
            'address': 'Cairo',
            'status': 'new',
        })
        record = Record.objects.get(first_name='Sara')
        self.assertEqual(record.owner, self.bob)


class RecordFormTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='GYM')

    def _data(self, **overrides):
        data = {
            'first_name': 'Ali',
            'last_name': 'Hassan',
            'category': self.category.id,
            'phone': '01012345678',
            'address': 'Zagazig',
            'status': 'new',
        }
        data.update(overrides)
        return data

    def test_valid_egyptian_phone_is_accepted(self):
        form = CreateRecordForm(data=self._data())
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_phone_is_rejected(self):
        form = CreateRecordForm(data=self._data(phone='12345'))
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_email_is_optional(self):
        form = CreateRecordForm(data=self._data(email=''))
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_status_is_rejected(self):
        form = CreateRecordForm(data=self._data(status='banana'))
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)