import json

bun_names = ['bun', 'bunjs', 'bun.js', 'bun-js', 'bun_js']
node_names = ['node', 'npm', 'ts', 'js', 'javascript', 'typescript', 'nodejs', 'node.js', 'node-js', 'node_js']
python_names = ['py', 'python', 'py3', 'py2', 'python3', 'python2', 'python-3', 'python-2', 'python_3', 'python_2']


def get_microservices_settings():
    with open('configs.json', 'r') as f:
        return json.loads(f.read())


# Returns the build command for the microservice
def get_build_command(microservice_name):
    settings = get_microservices_settings()

    if settings['specials'].includes(microservice_name):
        return settings['specials'][microservice_name]['build']

    elif node_names.__contains__(settings['language']):
        return 'npm run build'

    elif python_names.__contains__(settings['language']):
        return 'python setup.py build'

    elif bun_names.__contains__(settings['language']):
        return 'bun build'

    else:
        return 'echo "No build command found for this language"'


def get_test_command(microservice_name):
    settings = get_microservices_settings()

    if settings['specials'].includes(microservice_name):
        return settings['specials'][microservice_name]['build']

    elif node_names.__contains__(settings['language']):
        return 'npm test'

    elif python_names.__contains__(settings['language']):
        return 'python setup.py test'

    elif bun_names.__contains__(settings['language']):
        return 'bun test'

    else:
        return 'echo "No test command found for this language"'
