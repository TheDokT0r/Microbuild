def get_settings():
    config = {}
    with open('settings.txt', 'r') as f:

        for line in f.readlines():
            key, value = line.split('=')
            if key == 'res':
                config['res'] = value

    return config


def set_settings(configs):
    pass
