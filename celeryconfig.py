broker_url = 'redis://localhost'
result_backend = 'redis://localhost'

task_serializer = 'json'

task_routes = {
    'simple_tasks.add': 'low_priority',
    'simple_tasks.long': 'long_running',
}

task_annotations = {
    'simple_tasks.add': {
        'rate_limit': '10/m',
    }
}
