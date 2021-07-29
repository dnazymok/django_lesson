# from celery import Celery
#
# app = Celery('tasks')
# app.config_from_object('celeryconfig')
#
# # app.conf.update(
# #     task_serializer='json',
# #     result_serializer='json',
# # )
#
#
# @app.task
# def add(x, y):
#     return x + y
#
#
# @app.task
# def long(x, y):
#     import time
#     time.sleep(10)
#     return x + y
