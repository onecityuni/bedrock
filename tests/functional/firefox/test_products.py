# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.products import ProductsPage


@pytest.mark.skip_if_firefox
@pytest.mark.nondestructive
def test_download_bar_displayed(base_url, selenium):
    page = ProductsPage(base_url, selenium).open()
    download_bar = page.download_bar
    assert download_bar.is_download_firefox_message_displayed
    download_bar.close()
    assert not download_bar.is_displayed
