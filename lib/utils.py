from pathfinder.lib.i18n import tr


class PathfinderMaps:
    # platform specific commands to open the system's *most likely* file explorer
    COMMANDS = {  # noqa: RUF012
        'Windows': 'explorer',
        'Linux': 'xdg-open',
        'Darwin': 'open'
    }

    # map combobox label to actual character
    MAPPINGS = {  # noqa: RUF012
        'quote_char': {
            '"': '"',
            "'": "'",
            '´': '´',
            '`': '`',
            tr('Space'): ' ',
            tr('None'): '',
        },
        'separ_char': {
            tr('Space'): ' ',
            tr('Tab'): '\t',
            tr('New Line'): '\n',
            ',': ',',
            ';': ';',
        }
    }

    # reasonable defaults for pathfinder settings
    DEFAULTS = {  # noqa: RUF012
        'quote_char': '"',
        'separ_char': tr('Space'),
        'quote_char_custom': '',
        'separ_char_custom': '',
        'prefix': '',
        'postfix': '',
        'single_path_quote': 0,
        'single_path_affix': 0,
        'incl_file_name': 2,
        'incl_layer_name': 0,
        'incl_subset_str': 0,
        'show_notification': 0,
        'paths_on_new_line': 0,
        'original_vrt_ds': 0,
        'notify_duration': 5
    }

