# from celery.schedules import crontab
#
# broker_url = 'redis://localhost'
# result_backend = 'redis://localhost'
#
# task_serializer = 'json'
#
# task_routes = {
#     'simple_tasks.add': 'low_priority',
#     'simple_tasks.long': 'long_running',
# }
#
# task_annotations = {
#     'simple_tasks.add': {
#         'rate_limit': '10/m',
#     }
# }
#
# timezone = 'Europe/Kiev'
#
#
# beat_schedule = {
#     'add-every-5-sec': {
#         'task': 'simple_tasks.add',
#         'schedule': crontab(minute=2),
#         'args': (2, 2)
#     }
# }
