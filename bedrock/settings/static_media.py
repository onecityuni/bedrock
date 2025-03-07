# Static media bundle definitions.

PIPELINE_CSS = {
    'csrf-failure': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/csrf-failure.less',
        ),
        'output_filename': 'css/csrf-failure-bundle.css',
    },
    'about': {
        'source_filenames': (
            'css/sandstone/video-resp.less',
            'css/mozorg/about-base.less',
            'css/mozorg/mosaic.less',
        ),
        'output_filename': 'css/about-bundle.css',
    },
    'about-base': {
        'source_filenames': (
            'css/mozorg/about-base.less',
        ),
        'output_filename': 'css/about-base-bundle.css',
    },
    'credits-faq': {
        'source_filenames': (
            'css/mozorg/credits-faq.less',
        ),
        'output_filename': 'css/credits-faq-bundle.css',
    },
    'commit-access-policy': {
        'source_filenames': (
            'css/mozorg/commit-access-policy.less',
        ),
        'output_filename': 'css/commit-access-policy-bundle.css',
    },
    'commit-access-requirements': {
        'source_filenames': (
            'css/mozorg/commit-access-requirements.less',
        ),
        'output_filename': 'css/commit-access-requirements.css',
    },
    'about-forums': {
        'source_filenames': (
            'css/mozorg/about-forums.less',
        ),
        'output_filename': 'css/about-forums-bundle.css',
    },
    'about-patents': {
        'source_filenames': (
            'css/mozorg/about-patents.less',
            'css/base/mozilla-accordion.less',
        ),
        'output_filename': 'css/about-patents-bundle.css',
    },
    'foundation': {
        'source_filenames': (
            'css/foundation/foundation.less',
        ),
        'output_filename': 'css/foundation-bundle.css',
    },
    'gigabit': {
        'source_filenames': (
            'css/gigabit/gigabit.less',
        ),
        'output_filename': 'css/gigabit-bundle.css',
    },
    'grants': {
        'source_filenames': (
            'css/grants/grants.less',
        ),
        'output_filename': 'css/grants-bundle.css',
    },
    'lightbeam': {
        'source_filenames': (
            'css/lightbeam/lightbeam.less',
        ),
        'output_filename': 'css/lightbeam-bundle.css',
    },
    'itu': {
        'source_filenames': (
            'css/mozorg/itu.less',
        ),
        'output_filename': 'css/itu-bundle.css',
    },
    'common': {
        'source_filenames': (
            'css/sandstone/sandstone.less',
            'css/tabzilla/tabzilla-static.less',
        ),
        'output_filename': 'css/common-bundle.css',
    },
    'responsive': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/tabzilla/tabzilla-static.less',
        ),
        'output_filename': 'css/responsive-bundle.css',
    },
    'oldIE': {
        'source_filenames': (
            'css/sandstone/oldIE.less',
        ),
        'output_filename': 'css/oldIE-bundle.css',
    },
    'newsletter': {
        'source_filenames': (
            'css/newsletter/newsletter.less',
        ),
        'output_filename': 'css/newsletter-bundle.css',
    },
    'contact-spaces': {
        'source_filenames': (
            'css/libs/mapbox-2.1.5.css',
            'css/libs/magnific-popup.css',
            'css/base/mozilla-video-poster.less',
            'css/mozorg/contact-spaces.less',
        ),
        'output_filename': 'css/contact-spaces-bundle.css',
    },
    'contact-spaces-ie7': {
        'source_filenames': (
            'css/mozorg/contact-spaces-ie7.less',
        ),
        'output_filename': 'css/contact-spaces-ie7-bundle.css',
    },
    'contribute-old': {
        'source_filenames': (
            'css/mozorg/contribute/contribute-form.less',
            'css/mozorg/contribute/contribute-old.less',
            'css/sandstone/video-resp.less',
        ),
        'output_filename': 'css/contribute-old-bundle.css',
    },
    'contribute-friends': {
        'source_filenames': (
            'css/mozorg/contribute/friends.less',
        ),
        'output_filename': 'css/contribute-friends-bundle.css',
    },
    'contribute-studentambassadors-landing': {
        'source_filenames': (
            'css/base/social-widgets.less',
            'css/mozorg/contribute/studentambassadors/landing.less',
        ),
        'output_filename': 'css/contribute-studentambassadors-landing-bundle.css',
    },
    'contribute-studentambassadors-join': {
        'source_filenames': (
            'css/mozorg/contribute/studentambassadors/join.less',
        ),
        'output_filename': 'css/contribute-studentambassadors-join-bundle.css',
    },
    'dnt': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/base/mozilla-accordion.less',
            'css/firefox/dnt.less',
        ),
        'output_filename': 'css/dnt-bundle.css',
    },
    'firefox_accounts': {
        'source_filenames': (
            'css/firefox/sync-animation.less',
            'css/firefox/accounts.less',
        ),
        'output_filename': 'css/firefox_accounts-bundle.css',
    },
    'firefox_all': {
        'source_filenames': (
            'css/base/mozilla-share-cta.less',
            'css/base/menu-resp.less',
            'css/firefox/all.less',
        ),
        'output_filename': 'css/firefox_all-bundle.css',
    },
    'firefox_android': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/base/mozilla-modal.less',
            'css/base/send-to-device.less',
            'css/base/mozilla-accordion.less',
            'css/firefox/android.less',
        ),
        'output_filename': 'css/firefox_android-bundle.css',
    },
    'firefox_android_all': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/android/all.less',
        ),
        'output_filename': 'css/firefox-android-all.css',
    },
    'firefox_unsupported': {
        'source_filenames': (
            'css/firefox/unsupported.less',
        ),
        'output_filename': 'css/firefox_unsupported-bundle.css',
    },
    'firefox_unsupported_systems': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/unsupported-systems.less',
        ),
        'output_filename': 'css/firefox_unsupported_systems-bundle.css',
    },
    'firefox_channel': {
        'source_filenames': (
            'css/sandstone/sandstone.less',
            'css/tabzilla/tabzilla-static.less',
            'css/base/menu.less',
            'css/firefox/channel.less',
        ),
        'output_filename': 'css/firefox_channel-bundle.css',
    },
    'firefox-dashboard': {
        'source_filenames': (
            'css/base/mozilla-accordion.less',
            'css/base/menu-resp.less',
            'css/firefox/dashboard.less',
        ),
        'output_filename': 'css/firefox-dashboard-bundle.css',
    },
    'firefox_desktop': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/desktop/intro-anim.less',
            'css/base/svg-animation-check.less',
            'css/firefox/desktop/index.less',
        ),
        'output_filename': 'css/firefox_desktop-bundle.css',
    },
    'firefox_desktop_fast': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/desktop/fast.less',
        ),
        'output_filename': 'css/firefox_desktop_fast-bundle.css',
    },
    'firefox_desktop_customize': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/desktop/customize.less',
        ),
        'output_filename': 'css/firefox_desktop_customize-bundle.css',
    },
    'firefox_desktop_tips': {
        'source_filenames': (
            'css/base/mozilla-share-cta.less',
            'css/firefox/desktop/tips.less',
        ),
        'output_filename': 'css/firefox_desktop_tips-bundle.css',
    },
    'firefox_desktop_trust': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/desktop/trust.less',
        ),
        'output_filename': 'css/firefox_desktop_trust-bundle.css',
    },
    'firefox-interest-dashboard': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/interest-dashboard.less',
        ),
        'output_filename': 'css/firefox-interest-dashboard-bundle.css',
    },
    'firefox-tiles': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/tiles.less',
        ),
        'output_filename': 'css/firefox-tiles-bundle.css',
    },
    'firefox_family': {
        'source_filenames': (
            'css/firefox/family/index.less',
        ),
        'output_filename': 'css/firefox-family-bundle.css',
    },
    'firefox_family_ie': {
        'source_filenames': (
            'css/firefox/family/index-ie.less',
        ),
        'output_filename': 'css/firefox-family-ie-bundle.css',
    },
    'firefox_faq': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/faq.less',
            'css/base/mozilla-accordion.less',
        ),
        'output_filename': 'css/firefox_faq-bundle.css',
    },
    'firefox_fx38_0_5_firstrun': {
        'source_filenames': (
            'css/firefox/australis/fx38_0_5/firstrun.less',
        ),
        'output_filename': 'css/firefox_fx38_0_5_firstrun-bundle.css',
    },
    'firefox_developer_firstrun': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/firefox/dev-firstrun.less',
        ),
        'output_filename': 'css/firefox_developer_firstrun-bundle.css',
    },
    'nightly_firstrun': {
        'source_filenames': (
            'css/firefox/nightly_firstrun.less',
        ),
        'output_filename': 'css/nightly_firstrun-bundle.css',
    },
    'firefox_firstrun': {
        'source_filenames': (
            'css/sandstone/sandstone.less',
            'css/tabzilla/tabzilla-static.less',
            'css/firefox/firstrun/firstrun.less',
        ),
        'output_filename': 'css/firefox_firstrun-bundle.css',
    },
    'firefox_feedback': {
        'source_filenames': (
            'css/base/mozilla-share-cta.less',
            'css/firefox/feedback.less',
        ),
        'output_filename': 'css/firefox_feedback-bundle.css',
    },
    'firefox_geolocation': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/base/mozilla-accordion.less',
            'css/base/mozilla-modal.less',
            'css/libs/mapbox-2.1.5.css',
            'css/firefox/geolocation.less'
        ),
        'output_filename': 'css/firefox_geolocation-bundle.css',
    },
    'firefox_developer': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/base/mozilla-share-cta.less',
            'css/base/menu-resp.less',
            'css/firefox/developer.less',
        ),
        'output_filename': 'css/firefox_developer-bundle.css',
    },
    'firefox_hello_start': {
        'source_filenames': (
            'css/firefox/hello/start.less',
        ),
        'output_filename': 'css/firefox_hello_start-bundle.css',
    },
    'firefox_hello': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/base/mozilla-modal.less',
            'css/base/svg-animation-check.less',
            'css/base/mozilla-share-cta.less',
            'css/firefox/hello/index.less',
        ),
        'output_filename': 'css/firefox_hello-bundle.css',
    },
    'firefox_ios': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/base/mozilla-modal.less',
            'css/base/send-to-device.less',
            'css/firefox/ios.less',
        ),
        'output_filename': 'css/firefox_ios-bundle.css',
    },
    'firefox_mobile_download': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/tabzilla/tabzilla-static.less',
            'css/base/simple_footer-resp.less',
            'css/firefox/mobile-download.less',
        ),
        'output_filename': 'css/firefox_mobile_download.css',
    },
    'firefox_new': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/tabzilla/tabzilla-static.less',
            'css/base/simple_footer-resp.less',
            'css/firefox/new.less',
        ),
        'output_filename': 'css/firefox_new-bundle.css',
    },
    'firefox_organizations': {
        'source_filenames': (
            'css/firefox/organizations.less',
        ),
        'output_filename': 'css/firefox_organizations-bundle.css',
    },
    'firefox_os': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/base/mozilla-modal.less',
            'css/tabzilla/tabzilla-static.less',
            'css/libs/jquery.pageslide.css',
            'css/firefox/family-nav.less',
            'css/firefox/os/get_device.less',
            'css/firefox/os/in-the-news.less',
            'css/firefox/os/firefox-os.less',
        ),
        'output_filename': 'css/firefox_os-bundle.css',
    },
    'firefox_os_2_5': {
        'source_filenames': (
            'css/sandstone/sandstone-resp.less',
            'css/tabzilla/tabzilla-static.less',
            'css/firefox/family-nav.less',
            'css/firefox/os/in-the-news.less',
            'css/firefox/os/firefox-os-2-5.less',
        ),
        'output_filename': 'css/firefox_os_2_5-bundle.css',
    },
    'firefox_os_ie': {
        'source_filenames': (
            'css/firefox/os/firefox-os-ie.less',
        ),
        'output_filename': 'css/firefox_os_ie-bundle.css',
    },
    'firefox_os_devices': {
        'source_filenames': (
            'css/libs/tipsy.css',
            'css/firefox/family-nav.less',
            'css/base/mozilla-modal.less',
            'css/firefox/os/get_device.less',
            'css/firefox/os/devices.less',
        ),
        'output_filename': 'css/firefox_os_devices-bundle.css',
    },
    'firefox_os_devices_ie': {
        'source_filenames': (
            'css/firefox/os/devices-ie.less',
        ),
        'output_filename': 'css/firefox_os_devices_ie-bundle.css',
    },
    'firefox_os_mwc_2015_preview': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/firefox/family-nav.less',
            'css/firefox/os/mwc-2015-preview.less',
        ),
        'output_filename': 'css/firefox_os_mwc_2015_preview-bundle.css',
    },
    'firefox_os_tv': {
        'source_filenames': (
            'css/firefox/os/tv.less',
        ),
        'output_filename': 'css/firefox_os_tv-bundle.css',
    },
    'firefox_private_browsing': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/tracking-protection-animation.less',
            'css/firefox/private_browsing/private-browsing-conditionals.less',
            'css/firefox/private_browsing/private-browsing.less',
        ),
        'output_filename': 'css/firefox_private_browsing-bundle.css',
    },
    'firefox_releases_index': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/releases-index.less',
        ),
        'output_filename': 'css/firefox_releases_index-bundle.css',
    },
    'firefox_tour': {
        'source_filenames': (
            'css/firefox/australis/australis-ui-tour.less',
            'css/firefox/hello-animation.less',
            'css/firefox/australis/fx36/common.less',
        ),
        'output_filename': 'css/firefox_tour-bundle.css',
    },
    'firefox_tour_none': {
        'source_filenames': (
            'css/firefox/australis/australis-page-common.less',
            'css/firefox/sync-animation.less',
            'css/firefox/australis/australis-page-stacked.less',
        ),
        'output_filename': 'css/firefox_tour_none-bundle.css',
    },
    'firefox_whatsnew_38_video': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/firefox/whatsnew_38/common.less',
            'css/firefox/whatsnew_38/whatsnew-video.less',
        ),
        'output_filename': 'css/firefox_whatsnew_38_video-bundle.css',
    },
    'firefox_whatsnew_38_pocket': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/firefox/whatsnew_38/common.less',
            'css/firefox/whatsnew_38/whatsnew-pocket.less',
        ),
        'output_filename': 'css/firefox_whatsnew_38_pocket-bundle.css',
    },
    'firefox_whatsnew_42_a': {
        'source_filenames': (
            'css/firefox/tracking-protection-animation.less',
            'css/firefox/whatsnew_42/common.less',
            'css/firefox/whatsnew_42/variant-a.less',
        ),
        'output_filename': 'css/firefox_whatsnew_42_a-bundle.css',
    },
    'firefox_win10_welcome': {
        'source_filenames': (
            'css/firefox/win10-welcome.less',
        ),
        'output_filename': 'css/firefox_win10_welcome-bundle.css',
    },
    'firefox_win10_welcome_variants': {
        'source_filenames': (
            'css/firefox/win10-welcome.less',
            'css/firefox/win10-welcome-variants.less',
        ),
        'output_filename': 'css/firefox_win10_welcome_variants-bundle.css',
    },
    'firefox_pocket': {
        'source_filenames': (
            'css/firefox/pocket.less',
        ),
        'output_filename': 'css/firefox_pocket-bundle.css',
    },
    'firefox_releasenotes_firefox': {
        'source_filenames': (
            'css/firefox/releasenotes-firefox.less',
        ),
        'output_filename': 'css/firefox_releasenotes_firefox-bundle.css',
    },
    'firefox_releasenotes': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/releasenotes.less',
        ),
        'output_filename': 'css/firefox_releasenotes-bundle.css',
    },
    'firefox_sync': {
        'source_filenames': (
            'css/firefox/family-nav.less',
            'css/firefox/sync.less',
        ),
        'output_filename': 'css/firefox_sync-bundle.css',
    },
    'firefox_sync_anim': {
        'source_filenames': (
            'css/firefox/sync-animation.less',
        ),
        'output_filename': 'css/firefox_sync_anim-bundle.css',
    },
    'firefox_choose': {
        'source_filenames': (
            'css/base/simple_footer-resp.less',
            'css/firefox/choose.less',
        ),
        'output_filename': 'css/firefox_choose-bundle.css',
    },
    'installer_help': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/base/mozilla-modal.less',
            'css/firefox/installer-help.less',
        ),
        'output_filename': 'css/installer_help-bundle.css',
    },
    'history-slides': {
        'source_filenames': (
            'css/mozorg/history-slides.less',
        ),
        'output_filename': 'css/history-slides-bundle.css',
    },
    'home': {
        'source_filenames': (
            'css/mozorg/home/home.less',
            'css/mozorg/home/home-promo.less',
        ),
        'output_filename': 'css/home-bundle.css',
    },
    'home-ie8': {
        'source_filenames': (
            'css/mozorg/home/home-ie8.less',
        ),
        'output_filename': 'css/home-ie8-bundle.css',
    },
    'legal': {
        'source_filenames': (
            'css/legal/legal.less',
        ),
        'output_filename': 'css/legal-bundle.css',
    },
    'legal-eula': {
        'source_filenames': (
            'css/legal/eula.less',
        ),
        'output_filename': 'css/legal-eula-bundle.css',
    },
    'legal-impressum': {
        'source_filenames': (
            'css/legal/impressum.less',
        ),
        'output_filename': 'css/legal-impressum-bundle.css',
    },
    'legal_fraud_report': {
        'source_filenames': (
            'css/legal/fraud-report.less',
        ),
        'output_filename': 'css/legal_fraud_report-bundle.css',
    },
    'manifesto': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/base/mozilla-share-cta.less',
            'css/mozorg/mosaic.less',
            'css/mozorg/manifesto.less',
        ),
        'output_filename': 'css/manifesto-bundle.css',
    },
    'mission': {
        'source_filenames': (
            'css/sandstone/video-resp.less',
            'css/mozorg/mosaic.less',
            'css/mozorg/mission.less',
        ),
        'output_filename': 'css/mission-bundle.css',
    },
    'mpl': {
        'source_filenames': (
            'css/mozorg/mpl.less',
        ),
        'output_filename': 'css/mpl-bundle.css',
    },
    'mozilla_accordion': {
        'source_filenames': (
            'css/base/mozilla-accordion.less',
        ),
        'output_filename': 'css/mozilla_accordion-bundle.css',
    },
    'partnerships': {
        'source_filenames': (
            'css/mozorg/partnerships.less',
        ),
        'output_filename': 'css/partnerships-bundle.css',
    },
    'persona': {
        'source_filenames': (
            'css/persona/persona.less',
        ),
        'output_filename': 'css/persona-bundle.css',
    },
    'powered-by': {
        'source_filenames': (
            'css/mozorg/powered-by.less',
        ),
        'output_filename': 'css/powered-by-bundle.css',
    },
    'plugincheck': {
        'source_filenames': (
            'css/base/mozilla-share-cta.less',
            'css/plugincheck/plugincheck.less',
        ),
        'output_filename': 'css/plugincheck-bundle.css',
    },
    'press': {
        'source_filenames': (
            'css/press/press.less',
        ),
        'output_filename': 'css/press-bundle.css',
    },
    'privacy': {
        'source_filenames': (
            'css/privacy/privacy.less',
        ),
        'output_filename': 'css/privacy-bundle.css',
    },
    'fb_privacy': {
        'source_filenames': (
            'css/privacy/fb-privacy.less',
        ),
        'output_filename': 'css/fb_privacy-bundle.css',
    },
    'projects_mozilla_based': {
        'source_filenames': (
            'css/mozorg/projects/mozilla-based.less',
        ),
        'output_filename': 'css/projects_mozilla_based-bundle.css',
    },
    'projects-calendar': {
        'source_filenames': (
            'css/mozorg/projects/calendar.less',
        ),
        'output_filename': 'css/projects-calendar-bundle.css',
    },
    'research': {
        'source_filenames': (
            'css/research/research.less',
        ),
        'output_filename': 'css/research-bundle.css',
    },
    'security': {
        'source_filenames': (
            'css/security/security.less',
        ),
        'output_filename': 'css/security-bundle.css',
    },
    'security-bug-bounty-hall-of-fame': {
        'source_filenames': (
            'css/security/hall-of-fame.less',
            'css/base/mozilla-accordion.less',
        ),
        'output_filename': 'css/security-bug-bounty-hall-of-fame-bundle.css',
    },
    'security-tld-idn': {
        'source_filenames': (
            'css/mozorg/security-tld-idn.less',
        ),
        'output_filename': 'css/security-tld-idn-bundle.css',
    },
    'smarton': {
        'source_filenames': (
            'css/base/mozilla-share-cta.less',
            'css/teach/smarton.less',
        ),
        'output_filename': 'css/smarton-bundle.css',
    },
    'smarton-ie': {
        'source_filenames': (
            'css/teach/smarton-ie.less',
        ),
        'output_filename': 'css/smarton-ie-bundle.css',
    },
    'styleguide': {
        'source_filenames': (
            'css/sandstone/fonts.less',
            'css/styleguide/styleguide.less',
            'css/styleguide/websites-sandstone.less',
            'css/styleguide/identity-mozilla.less',
            'css/styleguide/identity-firefox.less',
            'css/styleguide/identity-firefox-family.less',
            'css/styleguide/identity-firefoxos.less',
            'css/styleguide/identity-marketplace.less',
            'css/styleguide/identity-thunderbird.less',
            'css/styleguide/identity-webmaker.less',
            'css/styleguide/communications.less',
            'css/styleguide/products-firefox-os.less',
        ),
        'output_filename': 'css/styleguide-bundle.css',
    },
    'styleguide-docs-mozilla-accordion': {
        'source_filenames': (
            'css/base/mozilla-accordion.less',
        ),
        'output_filename': 'css/styleguide-docs-mozilla-accordion-bundle.css',
    },
    'styleguide-docs-mozilla-pager': {
        'source_filenames': (
            'css/styleguide/docs/mozilla-pager.less',
        ),
        'output_filename': 'css/styleguide-docs-mozilla-pager-bundle.css',
    },
    'styleguide-docs-send-to-device': {
        'source_filenames': (
            'css/base/send-to-device.less',
        ),
        'output_filename': 'css/styleguide-docs-send-to-device-bundle.css',
    },
    # no longer used on bedrock. possibly referenced on external sites? should investigate.
    'tabzilla': {
        'source_filenames': (
            'css/tabzilla/tabzilla.less',
        ),
        'output_filename': 'css/tabzilla-min.css',
    },
    'tracking-protection-tour': {
        'source_filenames': (
            'css/firefox/tracking-protection-tour.less',
        ),
        'output_filename': 'css/tracking-protection-tour-bundle.css',
    },
    'contribute-2015': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/mozorg/contribute/contribute-2015.less',
        ),
        'output_filename': 'css/contribute-2015-bundle.css',
    },
    'video': {
        'source_filenames': (
            'css/sandstone/video.less',
        ),
        'output_filename': 'css/video-bundle.css',
    },
    'video-resp': {
        'source_filenames': (
            'css/sandstone/video-resp.less',
        ),
        'output_filename': 'css/video-resp-bundle.css',
    },
    'page_not_found': {
        'source_filenames': (
            'css/base/page-not-found.less',
        ),
        'output_filename': 'css/page_not_found-bundle.css',
    },
    'annual_2011': {
        'source_filenames': (
            'css/foundation/annual2011.less',
        ),
        'output_filename': 'css/annual_2011-bundle.css',
    },
    'annual_2012': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/foundation/annual2012.less',
        ),
        'output_filename': 'css/annual_2012-bundle.css',
    },
    'annual_2013': {
        'source_filenames': (
            'css/base/mozilla-modal.less',
            'css/foundation/annual2013.less',
        ),
        'output_filename': 'css/annual_2013-bundle.css',
    },
    'annual_2014': {
        'source_filenames': (
            'css/foundation/annual2013.less',
            'css/foundation/annual2014.less',
        ),
        'output_filename': 'css/annual_2014-bundle.css',
    },
    'thunderbird-features': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/thunderbird/features.less',
        ),
        'output_filename': 'css/thunderbird-features-bundle.css',
    },
    'thunderbird-landing': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/base/simple_footer-resp.less',
            'css/thunderbird/landing.less',
        ),
        'output_filename': 'css/thunderbird-landing-bundle.css',
    },
    'thunderbird-organizations': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/firefox/organizations.less',
        ),
        'output_filename': 'css/thunderbird-organizations-bundle.css',
    },
    'thunderbird-channel': {
        'source_filenames': (
            'css/base/menu-resp.less',
            'css/thunderbird/channel.less',
        ),
        'output_filename': 'css/thunderbird-channel-bundle.css',
    },
    'thunderbird-start': {
        'source_filenames': (
            'css/sandstone/fonts.less',
            'css/thunderbird/start.less',
        ),
        'output_filename': 'css/thunderbird-start-bundle.css',
    },
}

PIPELINE_JS = {
    'site': {
        'source_filenames': (
            'js/base/site.js',  # this is automatically included on every page
            'js/base/dnt-helper.js',
        ),
        'output_filename': 'js/site-bundle.js',
    },
    'projects-calendar': {
        'source_filenames': (
            'js/mozorg/calendar.js',
        ),
        'output_filename': 'js/projects-calendar-bundle.js',
    },
    # Served to most pages.
    # nav-main-resp.js isn't used on a handful of pages, but caching a single
    # bundle should offset the extra weight.
    'common': {
        'source_filenames': (
            'js/libs/jquery-1.11.3.min.js',
            'js/libs/spin.min.js',  # used by js/newsletter/form.js
            'js/base/global.js',
            'js/base/global-init.js',
            'js/newsletter/form.js',
            'js/base/mozilla-client.js',
            'js/base/mozilla-input-placeholder.js',
            'js/base/mozilla-image-helper.js',
            'js/base/nav-main-resp.js',
        ),
        'output_filename': 'js/common-bundle.js',
    },
    'contact-spaces': {
        'source_filenames': (
            'js/libs/mapbox-2.1.5.js',
            'js/libs/jquery.history.js',
            'js/mozorg/contact-data.js',
            'js/libs/jquery.magnific-popup.min.js',
            'js/base/mozilla-video-poster.js',
            'js/mozorg/contact-spaces.js',
        ),
        'output_filename': 'js/contact-spaces-bundle.js',
    },
    'contact-spaces-ie7': {
        'source_filenames': (
            'js/mozorg/contact-spaces-ie7.js',
        ),
        'output_filename': 'js/contact-spaces-ie7-bundle.js',
    },
    'contribute-faces': {
        'source_filenames': (
            'js/mozorg/contribute/contribute-faces.js',
        ),
        'output_filename': 'js/contribute-faces-bundle.js',
    },
    'contribute-form': {
        'source_filenames': (
            'js/mozorg/contribute/contribute-form.js',
            'js/base/mozilla-input-placeholder.js',
        ),
        'output_filename': 'js/contribute-form-bundle.js',
    },
    'contribute-friends': {
        'source_filenames': (
            'js/libs/jquery-1.11.3.min.js',
            'js/mozorg/contribute/friends.js',
        ),
        'output_filename': 'js/contribute-friends-bundle.js'
    },
    'contribute-studentambassadors-join': {
        'source_filenames': (
            'js/mozorg/contribute/contribute-studentambassadors-join.js',
            'js/base/mozilla-input-placeholder.js',
        ),
        'output_filename': 'js/contribute-studentambassadors-join-bundle.js',
    },
    'existing': {
        'source_filenames': (
            'js/newsletter/existing.js',
        ),
        'output_filename': 'js/existing-bundle.js',
    },
    'accordion': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-accordion-gatrack.js',
        ),
        'output_filename': 'js/accordion-bundle.js',
    },
    'dnt': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-accordion-gatrack.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
        ),
        'output_filename': 'js/firefox_dnt-bundle.js',
    },
    'firefox_accounts': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/sync-animation.js',
            'js/firefox/accounts.js',
        ),
        'output_filename': 'js/firefox_accounts-bundle.js',
    },
    'firefox_all': {
        'source_filenames': (
            'js/base/mozilla-share-cta.js',
            'js/base/mozilla-pager.js',
            'js/firefox/firefox-language-search.js',
        ),
        'output_filename': 'js/firefox_all-bundle.js',
    },
    'firefox_android': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-smoothscroll.js',
            'js/base/mozilla-accordion-gatrack.js',
            'js/libs/jquery.cycle2.min.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/sync-animation.js',
            'js/base/mozilla-modal.js',
            'js/base/send-to-device.js',
            'js/firefox/android.js',
        ),
        'output_filename': 'js/firefox_android-bundle.js',
    },
    'firefox_channel': {
        'source_filenames': (
            'js/base/mozilla-pager.js',
            'js/firefox/channel.js',
        ),
        'output_filename': 'js/firefox_channel-bundle.js',
    },
    'firefox_desktop_customize': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/sync-animation.js',
            'js/firefox/desktop/common.js',
            'js/firefox/desktop/customize.js',
        ),
        'output_filename': 'js/firefox_desktop_customize-bundle.js',
    },
    'firefox_desktop_fast': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/desktop/common.js',
            'js/firefox/desktop/speed-graph.js',
            'js/firefox/desktop/fast.js',
        ),
        'output_filename': 'js/firefox_desktop_fast-bundle.js',
    },
    'firefox_desktop_index': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/desktop/common.js',
            'js/firefox/desktop/speed-graph.js',
            'js/base/svg-animation-check.js',
            'js/firefox/desktop/intro-anim.js',
            'js/firefox/desktop/index.js',
        ),
        'output_filename': 'js/firefox_desktop_index-bundle.js',
    },
    'firefox_desktop_tips': {
        'source_filenames': (
            'js/base/mozilla-pager.js',
            'js/libs/hammer.1.1.2.min.js',
            'js/base/mozilla-share-cta.js',
            'js/firefox/desktop/tips.js',
        ),
        'output_filename': 'js/firefox_desktop_tips-bundle.js',
    },
    'firefox_desktop_trust': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/desktop/common.js',
        ),
        'output_filename': 'js/firefox_desktop_trust-bundle.js',
    },
    'firefox_developer': {
        'source_filenames': (
            'js/firefox/developer.js',
            'js/base/mozilla-modal.js',
            'js/base/mozilla-share-cta.js',
        ),
        'output_filename': 'js/firefox_developer-bundle.js',
    },
    'firefox_fx38_0_5_firstrun': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/australis/fx38_0_5/firstrun.js',
        ),
        'output_filename': 'js/firefox_fx38_0_5_firstrun-bundle.js',
    },
    'firefox_firstrun': {
        'source_filenames': (
            'js/firefox/firstrun/firstrun.js',
        ),
        'output_filename': 'js/firefox_firstrun-bundle.js',
    },
    'firefox_developer_firstrun': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-modal.js',
            'js/firefox/dev-firstrun.js',
        ),
        'output_filename': 'js/firefox_developer_firstrun-bundle.js',
    },
    'firefox_developer_whatsnew': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/firefox/dev-whatsnew.js',
        ),
        'output_filename': 'js/firefox_developer_whatsnew-bundle.js',
    },
    'firefox_new': {
        'source_filenames': (
            'js/base/search-params.js',
            'js/firefox/new.js',
        ),
        'output_filename': 'js/firefox_new-bundle.js',
    },
    'firefox_pocket': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/pocket.js',
        ),
        'output_filename': 'js/firefox_pocket-bundle.js',
    },
    'firefox_private_browsing': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-highlight-target.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/private-browsing.js'
        ),
        'output_filename': 'js/firefox_private_browsing-bundle.js',
    },
    'firefox_os': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/libs/script.js',
            'js/firefox/family-nav.js',
            'js/firefox/os/firefox-os.js',
        ),
        'output_filename': 'js/firefox_os-bundle.js',
    },
    'firefox_os_2_5': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/os/firefox-os-2.5.js',
        ),
        'output_filename': 'js/firefox_os_2_5-bundle.js',
    },

    'firefox_os_devices': {
        'source_filenames': (
            'js/libs/jquery.tipsy.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/base/mozilla-pager.js',
            'js/base/mozilla-modal.js',
            'js/base/mozilla-smoothscroll.js',
            'js/firefox/family-nav.js',
            'js/firefox/os/partner_data.js',
            'js/firefox/os/devices.js',
        ),
        'output_filename': 'js/firefox_os_devices-bundle.js',
    },
    'firefox_os_mwc_2015_preview': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/mwc-2015-map.js',
            'js/firefox/os/mwc-2015-preview.js',
        ),
        'output_filename': 'js/firefox_os_mwc_2015_preview-bundle.js',
    },
    'firefox_os_tv': {
        'source_filenames': (
            'js/base/mozilla-pager.js',
        ),
        'output_filename': 'js/firefox_os_tv-bundle.js',
    },
    'firefox_interest_dashboard': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-accordion-gatrack.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
        ),
        'output_filename': 'js/firefox_interest_dashboard-bundle.js',
    },
    'firefox_tiles': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
        ),
        'output_filename': 'js/firefox_tiles-bundle.js',
    },
    'firefox_family_index': {
        'source_filenames': (
            'js/firefox/family-index.js',
        ),
        'output_filename': 'js/firefox_family_index-bundle.js',
    },
    'firefox_faq': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-accordion-gatrack.js',
        ),
        'output_filename': 'js/firefox_faq-bundle.js',
    },
    'firefox_sync': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/sync-animation.js',
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/sync.js',
        ),
        'output_filename': 'js/firefox_sync-bundle.js',
    },
    'firefox_tour': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/australis/browser-tour.js',
            'js/firefox/australis/fx36/tour.js',
        ),
        'output_filename': 'js/firefox_tour-bundle.js',
    },
    'firefox_feedback': {
        'source_filenames': (
            'js/base/mozilla-share-cta.js',
        ),
        'output_filename': 'js/firefox_feedback-bundle.js',
    },
    'firefox_hello_start': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/hello/hello-ftu.js',
            'js/firefox/hello/start-ftu.js',
        ),
        'output_filename': 'js/firefox_hello_start-bundle.js',
    },
    'firefox_hello_start_minimal': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/hello/hello-ftu-minimal.js',
            'js/firefox/hello/start-minimal.js',
        ),
        'output_filename': 'js/firefox_hello_start_minimal-bundle.js',
    },
    'firefox_hello': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-modal.js',
            'js/base/svg-animation-check.js',
            'js/base/mozilla-share-cta.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/hello/index.js',
        ),
        'output_filename': 'js/firefox_hello-bundle.js',
    },
    'firefox_hello_ie9': {
        'source_filenames': (
            'js/libs/matchMedia.js',
            'js/libs/matchMedia.addListener.js',
        ),
        'output_filename': 'js/firefox_hello_ie9-bundle.js',
    },
    'firefox_ios': {
        'source_filenames': (
            'js/libs/script.js',
            'js/base/mozilla-modal.js',
            'js/base/send-to-device.js',
            'js/firefox/australis/australis-uitour.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/family-nav.js',
            'js/firefox/ios.js',
        ),
        'output_filename': 'js/firefox_ios-bundle.js',
    },
    'firefox_tour_none': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/australis/common.js',
            'js/firefox/australis/no-tour.js',
        ),
        'output_filename': 'js/firefox_tour_none-bundle.js',
    },
    'firefox_whatsnew_38_video': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/firefox/whatsnew_38/whatsnew-video.js',
        ),
        'output_filename': 'js/firefox_whatsnew_38_video-bundle.js',
    },
    'firefox_whatsnew_38_pocket': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/whatsnew_38/pocket-uitour.js',
            'js/firefox/whatsnew_38/whatsnew-pocket.js',
        ),
        'output_filename': 'js/firefox_whatsnew_38_pocket-bundle.js',
    },
    'firefox_whatsnew_42_a': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-highlight-target.js',
            'js/firefox/whatsnew_42/variant-a.js',
        ),
        'output_filename': 'js/firefox_whatsnew_42_a-bundle.js',
    },
    'firefox_firstrun_42_learnmore': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-highlight-target.js',
            'js/firefox/whatsnew_42/learnmore.js',
        ),
        'output_filename': 'js/firefox_firstrun_42_learnmore-bundle.js',
    },
    'firefox_win10_welcome': {
        'source_filenames': (
            'js/firefox/australis/australis-uitour.js',
            'js/base/mozilla-firefox-default.js',
            'js/firefox/win10-welcome.js',
            'js/firefox/win10-welcome-init.js',
        ),
        'output_filename': 'js/firefox_win10_welcome-bundle.js',
    },
    'geolocation': {
        'source_filenames': (
            'js/libs/mapbox-2.1.5.js',
            'js/base/mozilla-accordion.js',
            'js/base/mozilla-accordion-gatrack.js',
            'js/firefox/geolocation-demo.js',
            'js/base/mozilla-modal.js',
        ),
        'output_filename': 'js/geolocation-bundle.js',
    },
    'home': {
        'source_filenames': (
            'js/mozorg/home/home.js',
            'js/mozorg/home/ga-tracking.js',
        ),
        'output_filename': 'js/home-bundle.js',
    },
    'history-slides': {
        'source_filenames': (
            'js/libs/jquery.sequence.js',
            'js/mozorg/history-slides.js',
        ),
        'output_filename': 'js/history-slides-bundle.js',
    },
    'installer_help': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/firefox/installer-help.js',
        ),
        'output_filename': 'js/installer_help-bundle.js',
    },
    'legal_fraud_report': {
        'source_filenames': (
            'js/libs/jquery.validate.js',
            'js/legal/fraud-report.js',
        ),
        'output_filename': 'js/legal_fraud_report-bundle.js',
    },
    'manifesto': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/base/mozilla-share-cta.js',
            'js/mozorg/manifesto.js',
        ),
        'output_filename': 'js/manifesto-bundle.js',
    },
    'partnerships': {
        'source_filenames': (
            'js/libs/jquery.validate.js',
            'js/base/mozilla-form-helper.js',
            'js/mozorg/partnerships.js',
            'js/base/mozilla-input-placeholder.js',
        ),
        'output_filename': 'js/partnerships-bundle.js',
    },
    'plugincheck': {
        'source_filenames': (
            'js/plugincheck/lib/mustache.js',
            'js/base/mozilla-share-cta.js',
            'js/plugincheck/tmpl/plugincheck.ui.tmpl.js',
            'js/plugincheck/lib/utils.js',
            'js/plugincheck/lib/version-compare.js',
            'js/plugincheck/lib/plugincheck.js',
            'js/plugincheck/check-plugins.js',
        ),
        'output_filename': 'js/plugincheck-bundle.js',
    },
    'press_speaker_request': {
        'source_filenames': (
            'js/libs/jquery.validate.js',
            'js/libs/modernizr.custom.inputtypes.js',
            'js/press/speaker-request.js',
        ),
        'output_filename': 'js/press_speaker_request-bundle.js',
    },
    'privacy': {
        'source_filenames': (
            'js/privacy/privacy.js',
        ),
        'output_filename': 'js/privacy-bundle.js',
    },
    'smarton': {
        'source_filenames': (
            'js/base/mozilla-share-cta.js',
            'js/base/mozilla-smoothscroll.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/libs/circles.min.js',
            'js/teach/smarton.js',
        ),
        'output_filename': 'js/smarton-bundle.js',
    },
    'smarton-landing': {
        'source_filenames': (
            'js/base/mozilla-share-cta.js',
            'js/libs/snap.svg.min.js',
            'js/teach/smarton-landing.js',
        ),
        'output_filename': 'js/smarton-landing-bundle.js',
    },
    'styleguide': {
        'source_filenames': (
            'js/styleguide/styleguide.js',
        ),
        'output_filename': 'js/styleguide-bundle.js',
    },
    'styleguide-docs-mozilla-accordion': {
        'source_filenames': (
            'js/base/mozilla-accordion.js',
            'js/styleguide/docs/mozilla-accordion.js',
        ),
        'output_filename': 'js/styleguide-docs-mozilla-accordion-bundle.js',
    },
    'styleguide-docs-mozilla-pager': {
        'source_filenames': (
            'js/base/mozilla-pager.js',
            'js/styleguide/docs/mozilla-pager.js',
        ),
        'output_filename': 'js/styleguide-docs-mozilla-pager-bundle.js',
    },
    'styleguide-docs-send-to-device': {
        'source_filenames': (
            'js/base/send-to-device.js',
            'js/styleguide/docs/send-to-device.js',
        ),
        'output_filename': 'js/styleguide-docs-send-to-device-bundle.js',
    },
    'tracking-protection-tour': {
        'source_filenames': (
            'js/libs/jquery-1.11.3.min.js',
            'js/firefox/australis/australis-uitour.js',
            'js/firefox/tracking-protection-tour.js',
            'js/firefox/tracking-protection-tour-init.js',
        ),
        'output_filename': 'js/tracking-protection-tour-bundle.js',
    },
    'video': {
        'source_filenames': (
            'js/base/mozilla-video-tools.js',
        ),
        'output_filename': 'js/video-bundle.js',
    },
    'contribute-2015': {
        'source_filenames': (
            'js/mozorg/contribute/contribute-2015-ga.js',
            'js/mozorg/contribute/contribute-2015.js',
        ),
        'output_filename': 'js/contribute-2015-bundle.js',
    },
    'contribute-2015-landing': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.cycle2.min.js',
            'js/base/mozilla-modal.js',
        ),
        'output_filename': 'js/contribute-2015-landing-bundle.js',
    },
    'mosaic': {
        'source_filenames': (
            'js/libs/modernizr.custom.26887.js',
            'js/libs/jquery.transit.min.js',
            'js/libs/jquery.gridrotator.js',
        ),
        'output_filename': 'js/mosaic-bundle.js',
    },
    'annual_2011': {
        'source_filenames': (
            'js/libs/jquery.hoverIntent.minified.js',
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.jcarousel.min.js',
            'js/foundation/annual2011.js',
        ),
        'output_filename': 'js/annual_2011-bundle.js',
    },
    'annual_2012': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/foundation/annual2012.js',
        ),
        'output_filename': 'js/annual_2012-bundle.js',
    },
    'annual_2013': {
        'source_filenames': (
            'js/base/mozilla-modal.js',
            'js/foundation/annual2013.js',
        ),
        'output_filename': 'js/annual_2013-bundle.js',
    },
    'logo-prototype': {
        'source_filenames': (
            'js/styleguide/logo-prototype/vendor/raf.polyfill.js',
            'js/styleguide/logo-prototype/vendor/tween.js',
            'js/styleguide/logo-prototype/vendor/lodash.compat.min.js',
            'js/styleguide/logo-prototype/vendor/perlin.js',
            'js/styleguide/logo-prototype/vendor/dat.gui.js',
            'js/libs/jquery-1.11.3.min.js',
            'js/styleguide/logo-prototype/clock-data.js',
        ),
        'output_filename': 'js/logo-prototype-bundle.js',
    },
    'releasenotes': {
        'source_filenames': (
            'js/libs/jquery.waypoints.min.js',
            'js/libs/jquery.waypoints-sticky.min.js',
            'js/firefox/releasenotes.js',
        ),
        'output_filename': 'js/releasenotes-bundle.js',
    },
    'thunderbird-all': {
        'source_filenames': (
            'js/base/mozilla-pager.js',
            'js/firefox/firefox-language-search.js',
        ),
        'output_filename': 'js/thunderbird_all-bundle.js',
    },
    'newsletter_form': {
        'source_filenames': (
            'js/libs/jquery-1.11.3.min.js',
            'js/libs/spin.min.js',
            'js/newsletter/form.js',
        ),
        'output_filename': 'js/newsletter_form-bundle.js',
    },
    'matchmedia_addlistener': {
        'source_filenames': (
            'js/libs/matchMedia.addListener.js',
        ),
        'output_filename': 'js/matchmedia_addlistener-bundle.js',
    },
}
