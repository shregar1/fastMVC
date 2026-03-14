"""
fastmvc_payments – Payments config and base abstractions for FastMVC.
"""

from .base import CheckoutSession, IPaymentGateway
from .config import PaymentsConfiguration
from .dto import (
    LinkConfigDTO,
    PayUConfigDTO,
    PaypalConfigDTO,
    PaymentsConfigurationDTO,
    RazorpayConfigDTO,
    StripeConfigDTO,
)

__version__ = "0.1.0"

__all__ = [
    "CheckoutSession",
    "IPaymentGateway",
    "PaymentsConfiguration",
    "PaymentsConfigurationDTO",
    "StripeConfigDTO",
    "RazorpayConfigDTO",
    "PaypalConfigDTO",
    "PayUConfigDTO",
    "LinkConfigDTO",
]
