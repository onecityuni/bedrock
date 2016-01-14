# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class AboutPage(BasePage):

    _url = '{base_url}/{locale}/about'

    _mosaic_locator = (By.ID, 'mosaic')
    _video_overlay_locator = (By.CSS_SELECTOR, '.video .mozilla-video-control-overlay')
    _video_locator = (By.CSS_SELECTOR, '.video video')

    @property
    def is_mosaic_displayed(self):
        return self.is_element_displayed(self._mosaic_locator)

    @property
    def is_video_overlay_displayed(self):
        return self.is_element_displayed(self._video_overlay_locator)

    @property
    def is_video_displayed(self):
        return self.is_element_displayed(self._video_locator)

    def play_video(self):
        assert self.is_video_overlay_displayed, 'Video is already displayed'
        self.find_element(self._video_overlay_locator).click()
        self.wait.until(lambda s: not self.is_video_overlay_displayed)
