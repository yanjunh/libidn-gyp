{
  'targets': [
    {
      'target_name': 'libidn',
      'type': 'shared_library',
      'include_dirs': [
        '<(DEPTH)/third_party/libidn/lib',
        '<(DEPTH)/third_party/libidn/lib/gl',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/third_party/libidn/lib',
          '<(DEPTH)/third_party/libidn/lib/gl',
        ],
      },
      'defines': [
        'HAVE_CONFIG_H',
        'LIBIDN_BUILDING',
      ],
      'sources': [
        'lib/gl/c-ctype.c',
        'lib/gl/c-strcasecmp.c',
        'lib/gl/c-strncasecmp.c',
        'lib/gl/striconv.c',
        'lib/nfkc.c',
        'lib/toutf8.c',
        'lib/version.c',
        'lib/stringprep.c',
        'lib/rfc3454.c',
        'lib/profiles.c',
        'lib/punycode.c',
        'lib/idna.c',
        'lib/pr29.c',
        'lib/idn-free.c',
        'lib/strerror-idna.c',
        'lib/strerror-pr29.c',
        'lib/strerror-punycode.c',
        'lib/strerror-stringprep.c',
        'lib/strerror-tld.c',
        'lib/tld.c',
        'lib/tlds.c',
      ],
      'conditions': [
        ['OS == "win"', {
          'include_dirs': [
            '<(DEPTH)/third_party/libidn/windows/include',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(DEPTH)/third_party/libidn/windows/include',
            ],
          },
          'defines': [
            '_USRDLL',
            'IDNA_EXPORTS',
            '_CRT_NONSTDC_NO_DEPRECATE',
          ],
          'sources': [
            'lib/gl/strverscmp.c',
          ],
        }, {
          'defines': [
            'LOCALEDIR=\"$(localedir)\"',
          ],
          'include_dirs': [
            '<(DEPTH)/third_party/libidn/<(OS)/include',
          ],
          'sources': [
            'gl/progname.c',
            'gl/unistd.c',
            'lib/gl/unistr/u8-mbtoucr.c',
            'lib/gl/unistr/u8-uctomb.c',
            'lib/gl/unistr/u8-uctomb-aux.c',
          ]
        }],
        ['OS == "mac"', {
          'include_dirs': [
            '<(DEPTH)/third_party/libidn/gl',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(DEPTH)/third_party/libidn/mac/include',
            ],
          },
          'sources': [
            'lib/gl/strverscmp.c',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/usr/lib/libiconv.dylib',
            ],
          },
        }],
      ],  
    },
  ],
}
