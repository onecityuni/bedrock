# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.firefox.os.version.all import FirefoxOSBasePage


class FirefoxOSPage(FirefoxOSBasePage):

    _url = '{base_url}/{locale}/firefox/os/2.5'

    _primary_download_locator = (By.CSS_SELECTOR, '.hero-content .cta-button')
    _secondary_download_locator = (By.CSS_SELECTOR, '.fxos-try .cta-button')

    @property
    def is_primary_download_button_displayed(self):
        return self.is_element_displayed(self._primary_download_locator)

    @property
    def is_secondary_download_button_displayed(self):
        return self.is_element_displayed(self._secondary_download_locator)
