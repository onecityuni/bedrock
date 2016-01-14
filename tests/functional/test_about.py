# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.about import AboutPage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_is_mosaic_displayed(base_url, selenium):
    page = AboutPage(base_url, selenium).open()
    assert page.is_mosaic_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_play_video(base_url, selenium):
    page = AboutPage(base_url, selenium).open()
    page.play_video()
    assert not page.is_video_overlay_displayed
    assert page.is_video_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_newsletter_default_values(base_url, selenium):
    page = AboutPage(base_url, selenium).open()
    page.newsletter.expand_form()
    assert '' == page.newsletter.email
    assert 'United States' == page.newsletter.country
    assert not page.newsletter.privacy_policy_accepted
    assert page.newsletter.is_privacy_policy_link_displayed
