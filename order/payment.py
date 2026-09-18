from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol

@dataclass(frozen=True)
class PaymentResult:
    success: bool
    reference: str
    message: str = ""

class PaymentProvider(Protocol):
    def charge(self, amount: Decimal, email: str) -> PaymentResult: ...

class ManualPaymentProvider:
    def charge(self, amount: Decimal, email: str) -> PaymentResult:
        return PaymentResult(True, f"manual-{email}-{amount}", "Manual payment accepted")
