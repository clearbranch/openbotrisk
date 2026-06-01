# Browser and device fingerprinting

## Plain explanation

Browser fingerprinting means collecting details about a browser, device, and environment, then combining them into a profile.

Each detail may be ordinary on its own. But the combination can become distinctive.

Examples include:

- browser type and version
- operating system
- screen size
- timezone
- language
- fonts
- plugins
- graphics/WebGL behaviour
- audio/canvas rendering
- CPU or hardware hints
- touch support
- installed features
- JavaScript API behaviour

## Why the combination matters

One signal usually does not identify a browser.

For example, many people use Chrome. Many people have the same screen size. Many people are in the same timezone.

But the combination of browser version, screen size, language, timezone, fonts, graphics behaviour, and other details can be much more distinctive.

This is why fingerprinting is sometimes described as “many weak signals becoming one stronger signal”.

## How this differs from cookies

Cookies are stored identifiers. A website gives the browser a value and asks for it back later.

Fingerprinting is different. It tries to recognise the browser from its observable properties, even if cookies are absent or deleted.

In practice, websites and anti-bot systems may use both.

## Why this matters for bot detection

Bot detection systems can use fingerprinting to check whether a browser looks real and internally consistent.

Suspicious signs can include:

- browser claims Chrome but JavaScript behaviour does not match Chrome
- WebGL or canvas output looks unusual
- `navigator.webdriver` or automation markers are present
- plugins/codecs/fonts do not match the claimed platform
- screen, timezone, language, IP location, and headers do not line up
- the same fingerprint appears across many accounts or IPs
- too many “new” fingerprints appear in a short time

## Why fingerprinting is not perfect

Fingerprints can change when users update browsers, change settings, use privacy tools, install fonts, switch devices, use private browsing, or change networks.

Bots can also try to spoof or randomise fingerprints.

That means fingerprinting is useful but not certain. A good bot-detection system should treat it as one part of a broader risk judgement.

## Project use

Use this note before discussing:

- FP-Inspector
- Andriamilanto browser fingerprint study
- FP-Inconsistent
- browser fingerprint inconsistencies
- stealth plugins
- anti-detect browsers
- Cloudflare JA3/JA4 and browser signals
- ScrapFly/Bright Data fingerprint management

## Sources

- Wikipedia, “Device fingerprint”: https://en.wikipedia.org/wiki/Device_fingerprint
- EFF, “Cover Your Tracks”: https://coveryourtracks.eff.org/
- MDN, “Browser detection using the user agent”: https://developer.mozilla.org/en-US/docs/Web/HTTP/Browser_detection_using_the_user_agent
