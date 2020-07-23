from unittest.mock import patch


from django.test import TestCase
from django.contrib.auth import get_user_model

from snippets import models
from snippets.models import Profile


class ModelTests(TestCase):

    def test_create_profile(self):
        """Test creating a new profile"""
        type = 'A'
        name = 'idealiste'
        description = 'lorem ipsum'
        profile = Profile.objects.create(
            type=type,
            name=name,
            description=description,
        )

        self.assertEqual(profile.type, type)
        self.assertEqual(profile.name, name)
        self.assertEqual(profile.description, description)
        