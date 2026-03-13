from abc import ABC, abstractmethod


class TaxableItem(ABC):
    """
    Abstract base class for items that can calculate VAT.
    """

    def __init__(self, name: str, net_price: float):
        self.name = name
        self.net_price = net_price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def net_price(self) -> float:
        return self._net_price

    @net_price.setter
    def net_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Net price cannot be negative.")
        self._net_price = value

    @abstractmethod
    def calculate_vat(self) -> float:
        """
        Calculate the VAT for this item.
        Must be implemented by subclasses.
        """
        pass

    def gross_price(self) -> float:
        """
        Total price including VAT.
        """
        return self.net_price + self.calculate_vat()


class RegularProduct(TaxableItem):
    """
    Regular products with the standard VAT rate (e.g., 8.1% in Switzerland).
    """
    VAT_RATE = 0.081

    def calculate_vat(self) -> float:
        return (
            self.net_price *
            RegularProduct.VAT_RATE
        )


class ReducedProduct(TaxableItem):
    """
    Products with a reduced VAT rate (e.g., food with 2.6% VAT).
    """
    VAT_RATE = 0.026

    def calculate_vat(self) -> float:
        return (
            self.net_price *
            ReducedProduct.VAT_RATE
        )


class TaxFreeProduct(TaxableItem):
    """
    Products that are exempt from VAT.
    """

    def calculate_vat(self) -> float:
        return 0.0
