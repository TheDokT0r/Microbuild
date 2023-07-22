def get_configs():
    config = {}
    with open('configs.txt', 'r') as f:

        for line in f.readlines():
            key, value = line.split('=')
            if key == 'res':
                config['res'] = value

    return config

def set_configs(configs):
    pass