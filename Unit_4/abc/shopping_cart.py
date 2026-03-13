from taxable_items import TaxableItem


class ShoppingCart:
    """
    The shopping cart only works with the abstract type TaxableItem.
    It does not need to know the concrete product type.
    """

    def __init__(self):
        self._items: list[TaxableItem] = []

    def add_item(self, item: TaxableItem) -> None:
        self._items.append(item)

    def total_net(self) -> float:
        return sum(item.net_price for item in self._items)

    def total_vat(self) -> float:
        return sum(item.calculate_vat() for item in self._items)

    def total_gross(self) -> float:
        return sum(item.gross_price() for item in self._items)
