# -*- coding: utf-8 -*-
from allauth.socialaccount.providers.canvas.provider import CanvasProvider
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase


class CanvasTests(OAuth2TestsMixin, TestCase):
    provider_id = CanvasProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
            {
              "id": 5670506,
              "name": "Grover Kingrey",
              "short_name": "Grover Kingrey",
              "sortable_name": "Kingrey, Grover",
              "avatar_url": "https://canvas.example.edu/images/messages/avatar-50.png",
              "title": null,
              "bio": null,
              "primary_email": "groverk@example.edu",
              "login_id": "groverk",
              "integration_id": null,
              "time_zone": "America/New_York",
              "locale": null,
              "effective_locale": "en",
              "calendar": {
                "ics": "https://canvas.example.edu/feeds/calendars/user_example.ics"
              }
            }
        """)
