# fastmvc_queues

Queue backends for FastMVC: RabbitMQ, Amazon SQS, Azure Service Bus, NATS.

Uses `fastmvc_core` for configuration (`config/queues/config.json`). Install optional backends:

- `pip install fastmvc_queues[rabbitmq]` – pika
- `pip install fastmvc_queues[sqs]` – boto3
- `pip install fastmvc_queues[service-bus]` – azure-servicebus
- `pip install fastmvc_queues[nats]` – nats-py

## Usage

```python
from fastmvc_queues import QueueBroker, QueuesConfiguration

broker = QueueBroker()  # builds from QueuesConfiguration
await broker.publish("rabbitmq", b"payload", routing_key="orders.created")
await broker.publish("sqs", '{"event": "signup"}')
```
