import tempfile

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Profile


class RegistrationTests(TestCase):
    def test_registration_creates_profile_with_submitted_fields(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            response = self.client.post(
                reverse("register"),
                {
                    "first_name": "Ava",
                    "last_name": "Example",
                    "email": "ava@example.com",
                    "password": "safe-test-password",
                    "confirm_password": "safe-test-password",
                    "place": "London",
                    "dob": "1995-04-12",
                    "profile_pic": SimpleUploadedFile(
                        "avatar.jpg",
                        b"test image content",
                        content_type="image/jpeg",
                    ),
                },
            )

            self.assertRedirects(response, reverse("login"))
            user = User.objects.get(username="ava@example.com")
            profile = Profile.objects.get(user=user)
            self.assertEqual(profile.place, "London")
            self.assertEqual(profile.dob.isoformat(), "1995-04-12")
            self.assertEqual(profile.profile_pic.name, "users/avatar.jpg")
