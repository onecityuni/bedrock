# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.history import HistoryPage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_slideshow_displayed(base_url, selenium):
    page = HistoryPage(base_url, selenium).open()
    assert page.is_slideshow_displayed
    assert page.is_previous_button_displayed
    assert page.is_next_button_displayed


@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.viewport('mobile')
def test_list_displayed(base_url, selenium):
    page = HistoryPage(base_url, selenium).open()
    assert not page.is_slideshow_displayed
    assert not page.is_previous_button_displayed
    assert not page.is_next_button_displayed
