from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from movie.models import Category, Movie


class MovieCategoryTests(TestCase):
    def setUp(self):
        self.action_category = Category.objects.create(category="Action")
        self.drama_category = Category.objects.create(category="Drama")
        self.action_movie = Movie.objects.create(
            movie="Action Movie",
            trailer_link="https://example.com/trailer",
            category=self.action_category,
            release_date=date(2024, 1, 1),
            poster="poster/action.jpg",
            description="An action movie.",
            rating=8.0,
        )
        Movie.objects.create(
            movie="Drama Movie",
            trailer_link="https://example.com/trailer",
            category=self.drama_category,
            release_date=date(2024, 1, 1),
            poster="poster/drama.jpg",
            description="A drama movie.",
            rating=7.0,
        )

    def test_category_dropdown_appears_in_site_navigation(self):
        response = self.client.get(reverse("index"))

        self.assertContains(response, "Categories")
        self.assertContains(
            response,
            reverse("category_movies", args=[self.action_category.slug]),
        )

    def test_category_link_filters_movie_list(self):
        user = User.objects.create_user(username="movie-test", password="test-password")
        self.client.force_login(user)
        response = self.client.get(
            reverse("category_movies", args=[self.action_category.slug])
        )

        self.assertContains(response, self.action_movie.movie)
        self.assertNotContains(response, "Drama Movie")
        self.assertContains(response, "Action Movies")

    def test_add_movie_form_receives_categories(self):
        user = User.objects.create_superuser(
            username="movie-form-test",
            email="movie-form-test@example.com",
            password="test-password",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("add_movie"))

        self.assertContains(response, '<option value="{}">'.format(self.action_category.pk))
        self.assertContains(response, self.action_category.category)

    def test_movie_pages_handle_missing_posters(self):
        user = User.objects.create_user(username="movie-poster-test", password="test-password")
        self.client.force_login(user)
        movie = Movie.objects.create(
            movie="Posterless Movie",
            trailer_link="https://example.com/trailer",
            category=self.action_category,
            release_date=date(2024, 1, 1),
            poster="",
            description="A movie without a poster.",
            rating=6.0,
        )

        list_response = self.client.get(reverse("movie_list"))
        detail_response = self.client.get(reverse("movie_detail", args=[movie.pk]))

        self.assertContains(list_response, "No poster available")
        self.assertContains(detail_response, "No poster available")

    def test_regular_user_has_read_only_movie_permission(self):
        regular_user = User.objects.create_user(
            username="movie-reader",
            password="test-password",
        )
        self.client.force_login(regular_user)

        detail_response = self.client.get(
            reverse("movie_detail", args=[self.action_movie.pk])
        )
        add_response = self.client.get(reverse("add_movie"))
        update_response = self.client.get(
            reverse("edit_movie", args=[self.action_movie.pk])
        )
        delete_response = self.client.get(
            reverse("delete_movie", args=[self.action_movie.pk])
        )

        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(add_response.status_code, 403)
        self.assertEqual(update_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
        self.assertContains(detail_response, "Watch Trailer")
        self.assertNotContains(detail_response, "Update Movie")
        self.assertNotContains(detail_response, "Delete Movie")
