from datetime import date
from io import BytesIO
import tempfile

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import Actors


class ActorViewTests(TestCase):
    def setUp(self):
        self.media_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.media_dir.cleanup)
        media_settings = override_settings(MEDIA_ROOT=self.media_dir.name)
        media_settings.enable()
        self.addCleanup(media_settings.disable)
        user = User.objects.create_superuser(
            username="actor-test",
            email="actor-test@example.com",
            password="test-password",
        )
        self.client.force_login(user)

    def make_photo(self):
        image_buffer = BytesIO()
        Image.new("RGB", (2, 2), color="purple").save(image_buffer, format="PNG")
        return SimpleUploadedFile(
            "actor.png",
            image_buffer.getvalue(),
            content_type="image/png",
        )

    def test_create_and_update_actor_through_cbvs(self):
        response = self.client.post(
            reverse("add_actor"),
            {
                "name": "Ava Actor",
                "place": "London",
                "about": "A sample biography.",
                "dob": "1990-04-12",
                "picture": self.make_photo(),
            },
        )

        actor = Actors.objects.get(name="Ava Actor")
        self.assertRedirects(response, reverse("list_actors"))
        self.assertEqual(actor.dob, date(1990, 4, 12))

        response = self.client.get(reverse("list_actors"))
        self.assertContains(response, "Meet the Actors")
        self.assertContains(response, "Photo of Ava Actor")

        response = self.client.get(reverse("actor_detail", args=[actor.pk]))
        self.assertContains(response, "ACTOR PROFILE")

        response = self.client.post(
            reverse("update_actor", args=[actor.pk]),
            {
                "name": "Ava Updated",
                "place": "Bristol",
                "about": "Updated biography.",
                "dob": "1990-04-12",
            },
        )

        actor.refresh_from_db()
        self.assertRedirects(response, reverse("list_actors"))
        self.assertEqual(actor.name, "Ava Updated")
        self.assertEqual(actor.place, "Bristol")
        self.assertTrue(actor.picture.name)

    def test_invalid_actor_form_shows_validation_errors(self):
        response = self.client.post(reverse("add_actor"), {})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, 'class="form-control"')

    def test_delete_cbv_renders_confirmation_and_deletes_on_post(self):
        actor = Actors.objects.create(
            name="Ava Actor",
            place="London",
            about="A sample biography.",
            dob=date(1990, 4, 12),
            picture="actors/actor.png",
        )
        delete_url = reverse("delete_actor", args=[actor.pk])

        response = self.client.get(delete_url)

        self.assertContains(response, "Delete Ava Actor?")
        self.assertContains(response, "CONFIRM ACTION")

        response = self.client.post(delete_url)

        self.assertRedirects(response, reverse("list_actors"))
        self.assertFalse(Actors.objects.filter(pk=actor.pk).exists())

    def test_regular_user_has_read_only_actor_permission(self):
        actor = Actors.objects.create(
            name="Readonly Actor",
            place="London",
            about="A read-only profile.",
            dob=date(1990, 4, 12),
        )
        regular_user = User.objects.create_user(
            username="actor-reader",
            password="test-password",
        )
        self.client.force_login(regular_user)

        detail_response = self.client.get(
            reverse("actor_detail", args=[actor.pk])
        )
        add_response = self.client.get(reverse("add_actor"))
        update_response = self.client.get(
            reverse("update_actor", args=[actor.pk])
        )
        delete_response = self.client.get(
            reverse("delete_actor", args=[actor.pk])
        )

        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(add_response.status_code, 403)
        self.assertEqual(update_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
        self.assertContains(detail_response, "All Actors")
        self.assertNotContains(detail_response, "Update Actor")
        self.assertNotContains(detail_response, "Delete Actor")
