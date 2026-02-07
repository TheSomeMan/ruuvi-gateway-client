## Changelog

### [Unreleased]
* Added support for token-based (Bearer) authentication in `fetch_data`
* Made authentication optional — `fetch_data` now works without credentials for gateways with open access
* Made `username` and `password` parameters optional in `fetch_data`
* Added validation: either token or username/password can be provided, not both
* Improved error handling in `get_auth_info` (detects when gateway doesn't require authentication)
* Improved error propagation in `get_authenticate_cookies`
* Updated example and README with all three access modes (no auth, username/password, token)

## [0.1.0] - 2022-05-26
* First release