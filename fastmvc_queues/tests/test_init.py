"""Tests for fastmvc_queues."""

import pytest


def test_imports():
    from fastmvc_queues import (
        IQueueBackend,
        QueueBroker,
        QueueMessage,
        QueuesConfiguration,
        QueuesConfigurationDTO,
    )
    assert QueueBroker is not None
    assert QueuesConfiguration is not None
