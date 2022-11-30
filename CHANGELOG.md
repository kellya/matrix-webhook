# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v3.5.0] - 2022-09-07

- Add formatter for grafana 9
  in [#45](https://github.com/nim65s/matrix-webhook/pull/45)
  by [@svenseeberg](https://github.com/svenseeberg)

## [v3.4.0] - 2022-08-12

- fix tests
- add `matrix-webhook` script
  in [#25](https://github.com/nim65s/matrix-webhook/pull/25)
  and [#35](https://github.com/nim65s/matrix-webhook/pull/35)
  by [@a7p](https://github.com/a7p)
- publish linux/arm64 image
  in [#37](https://github.com/nim65s/matrix-webhook/pull/35)
  by [@kusold](https://github.com/kusold)
- update badges
- setup dependabot
- misc upgrades from poetry update, pre-commit.ci, and dependabot

## [v3.3.0] - 2022-03-04

- add pyupgrade
- add gitlab formatter for google chat & microsoft teams
  in [#21](https://github.com/nim65s/matrix-webhook/pull/21)
  by [@GhislainC](https://github.com/GhislainC)
- join room before sending message
  in [#12](https://github.com/nim65s/matrix-webhook/pull/12)
  by [@bboehmke](https://github.com/bboehmke)
- Changed --api-key and envvar API_KEY to --api-keys and API_KEYS respectively
- Changed handling of api key to use a list instead of single value
    can be used
- Changed the formatters to a more plugin-based approach where each formatter is
    its own <formattername>.py file in formatters directory
- Added pingdom formatter (currently handling http, dns, and tcp probe types)

## [v3.2.1] - 2021-08-28

- fix changelog

## [v3.2.0] - 2021-08-27

- add github & grafana formatters
- add formatted_body to bypass markdown with direct
  [matrix-custom-HTML](https://matrix.org/docs/spec/client_server/r0.6.1#m-room-message-msgtypes)
- allow "key" to be passed as a parameter
- allow to use a sha256 HMAC hex digest with the key instead of the raw key
- allow "room_id" to be passed as a parameter or with the data
- rename "text" to "body".
- Publish releases also on github from github actions
- fix tests for recent synapse docker image

## [v3.1.1] - 2021-07-18

## [v3.1.0] - 2021-07-18

- Publish on PyPI & Docker Hub with Github Actions
  in [#10](https://github.com/nim65s/matrix-webhook/pull/10)
  by [@nim65s](https://github.com/nim65s)

## [v3.0.0] - 2021-07-18

- Simplify code
  in [#1](https://github.com/nim65s/matrix-webhook/pull/1)
  by [@homeworkprod](https://github.com/homeworkprod)
- Update aiohttp use and docs
  in [#5](https://github.com/nim65s/matrix-webhook/pull/5)
  by [@svenseeberg](https://github.com/svenseeberg)
- Setup Tests, Coverage & CI ; update tooling
  in [#7](https://github.com/nim65s/matrix-webhook/pull/7)
  by [@nim65s](https://github.com/nim65s)
- Setup argparse & logging
  in [#8](https://github.com/nim65s/matrix-webhook/pull/8)
  by [@nim65s](https://github.com/nim65s)
- Setup packaging
  in [#9](https://github.com/nim65s/matrix-webhook/pull/9)
  by [@nim65s](https://github.com/nim65s)

## [v2.0.0] - 2020-03-14
- Update to matrix-nio & aiohttp & markdown

## [v1.0.0] - 2020-02-14
- First release with matrix-client & http.server

[Unreleased]: https://github.com/nim65s/matrix-webhook/compare/v3.5.0...master
[v3.5.0]: https://github.com/nim65s/matrix-webhook/compare/v3.4.0...v3.5.0
[v3.4.0]: https://github.com/nim65s/matrix-webhook/compare/v3.3.0...v3.4.0
[v3.3.0]: https://github.com/nim65s/matrix-webhook/compare/v3.2.1...v3.3.0
[v3.2.1]: https://github.com/nim65s/matrix-webhook/compare/v3.2.0...v3.2.1
[v3.2.0]: https://github.com/nim65s/matrix-webhook/compare/v3.1.1...v3.2.0
[v3.1.1]: https://github.com/nim65s/matrix-webhook/compare/v3.1.0...v3.1.1
[v3.1.0]: https://github.com/nim65s/matrix-webhook/compare/v3.0.0...v3.1.0
[v3.0.0]: https://github.com/nim65s/matrix-webhook/compare/v2.0.0...v3.0.0
[v2.0.0]: https://github.com/nim65s/matrix-webhook/compare/v1.0.0...v2.0.0
[v1.0.0]: https://github.com/nim65s/matrix-webhook/releases/tag/v1.0.0
