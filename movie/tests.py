from datetime import date

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
            reverse("category_movies", args=[self.action_category.pk]),
        )

    def test_category_link_filters_movie_list(self):
        response = self.client.get(
            reverse("category_movies", args=[self.action_category.pk])
        )

        self.assertContains(response, self.action_movie.movie)
        self.assertNotContains(response, "Drama Movie")
        self.assertContains(response, "Action Movies")
