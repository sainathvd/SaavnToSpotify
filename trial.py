dict = {'tracks': {'href': 'https://api.spotify.com/v1/search?query=Udd+Gaye&type=track&market=IN&offset=0&limit=1',
                   'items': [{'album': {'album_type': 'single', 'artists': [
                       {'external_urls': {'spotify': 'https://open.spotify.com/artist/72beYOeW2sb2yfcS4JsRvb'},
                        'href': 'https://api.spotify.com/v1/artists/72beYOeW2sb2yfcS4JsRvb',
                        'id': '72beYOeW2sb2yfcS4JsRvb', 'name': 'Ritviz', 'type': 'artist',
                        'uri': 'spotify:artist:72beYOeW2sb2yfcS4JsRvb'}],
                                        'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO',
                                                              'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE',
                                                              'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR',
                                                              'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL',
                                                              'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT',
                                                              'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL',
                                                              'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT',
                                                              'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH',
                                                              'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'],
                                        'external_urls': {
                                            'spotify': 'https://open.spotify.com/album/3w4IGs3MgYRrHrVuC6QGAu'},
                                        'href': 'https://api.spotify.com/v1/albums/3w4IGs3MgYRrHrVuC6QGAu',
                                        'id': '3w4IGs3MgYRrHrVuC6QGAu', 'images': [
                           {'height': 640, 'url': 'https://i.scdn.co/image/059ae316b169e118d4513c1696d8d1f2dc95462d',
                            'width': 640},
                           {'height': 300, 'url': 'https://i.scdn.co/image/74fb706ac04629806e6da3dbcf1eb99561f48ff7',
                            'width': 300},
                           {'height': 64, 'url': 'https://i.scdn.co/image/fc8f9e1293929cc35750bae810a66910aec9400b',
                            'width': 64}], 'name': 'Udd Gaye (Bacardi House Party Sessions)',
                                        'release_date': '2017-11-27', 'release_date_precision': 'day',
                                        'total_tracks': 1, 'type': 'album',
                                        'uri': 'spotify:album:3w4IGs3MgYRrHrVuC6QGAu'}, 'artists': [
                       {'external_urls': {'spotify': 'https://open.spotify.com/artist/72beYOeW2sb2yfcS4JsRvb'},
                        'href': 'https://api.spotify.com/v1/artists/72beYOeW2sb2yfcS4JsRvb',
                        'id': '72beYOeW2sb2yfcS4JsRvb', 'name': 'Ritviz', 'type': 'artist',
                        'uri': 'spotify:artist:72beYOeW2sb2yfcS4JsRvb'}],
                              'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA',
                                                    'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC',
                                                    'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU',
                                                    'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI',
                                                    'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO',
                                                    'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO',
                                                    'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY',
                                                    'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 180413,
                              'explicit': False, 'external_ids': {'isrc': 'FRX201782605'},
                              'external_urls': {'spotify': 'https://open.spotify.com/track/6wZJsut8fjiWiMPaccRAOX'},
                              'href': 'https://api.spotify.com/v1/tracks/6wZJsut8fjiWiMPaccRAOX',
                              'id': '6wZJsut8fjiWiMPaccRAOX', 'is_local': False,
                              'name': 'Udd Gaye - Bacardi House Party Sessions', 'popularity': 55,
                              'preview_url': 'https://p.scdn.co/mp3-preview/2535c7016173205a6490e82db080345df8975c42?cid=841ebcf06a0c4564b8c966522fa447bc',
                              'track_number': 1, 'type': 'track', 'uri': 'spotify:track:6wZJsut8fjiWiMPaccRAOX'}],
                   'limit': 1,
                   'next': 'https://api.spotify.com/v1/search?query=Udd+Gaye&type=track&market=IN&offset=1&limit=1',
                   'offset': 0, 'previous': None, 'total': 7}}

print(dict['tracks']['items'][0]['id'])
