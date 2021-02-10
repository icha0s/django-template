import os

import structlog
from structlog import processors
from structlog.contextvars import merge_contextvars
from structlog.stdlib import BoundLogger, LoggerFactory

renderer_kv = processors.KeyValueRenderer(key_order=["timestamp", "severity", "message"], drop_missing=True)
renderer_json = processors.JSONRenderer()
logging_renderer = {"kv": renderer_kv, "json": renderer_json}.get(
    os.environ.get("LOGGING_RENDERER", "json"), renderer_json
)

structlog.configure(
    processors=[
        merge_contextvars,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(),
        structlog.stdlib.PositionalArgumentsFormatter(),
        logging_renderer,
    ],
    wrapper_class=BoundLogger,
    context_class=dict,
    logger_factory=LoggerFactory(),
    cache_logger_on_first_use=True,
)
