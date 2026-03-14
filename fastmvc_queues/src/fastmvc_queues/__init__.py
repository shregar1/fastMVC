"""
fastmvc_queues – Queue backends (RabbitMQ, SQS, Azure Service Bus, NATS) for FastMVC.
"""

from fastmvc_core import QueuesConfiguration, QueuesConfigurationDTO

from fastmvc_core.services.queues import (
    IQueueBackend,
    QueueBroker,
    QueueMessage,
)

__version__ = "0.1.0"

__all__ = [
    "IQueueBackend",
    "QueueBroker",
    "QueueMessage",
    "QueuesConfiguration",
    "QueuesConfigurationDTO",
]
