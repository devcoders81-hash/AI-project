from celery import Celery

from app.core.config import settings

celery = Celery(
    "interview_ai",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        "app.task.resume_tasks",
    ],
)



celery.conf.update(

    task_serializer="json",

    accept_content=["json"],

    result_serializer="json",

    timezone="UTC",

    enable_utc=True,

    task_track_started=True,

    worker_prefetch_multiplier=1,
    worker_concurrency=1
)

celery.autodiscover_tasks(
    ["app.task"]
)