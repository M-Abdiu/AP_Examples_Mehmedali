"""
test_person.py
==============
Concept: Basic Unit Tests — Happy Paths & Edge Cases
------------------------------------------------------
A "unit" is the smallest testable piece of code (here: a single class).
Each test method covers exactly ONE behaviour.

Run with:  pytest tests/test_person.py -v
"""

import pytest
from university.person import Person


# ======================================================================
# Fixtures  — shared setup reused across tests
# ======================================================================

@pytest.fixture
def alice() -> Person:
    """A valid Person instance used as a baseline in many tests."""
    return Person("Alice", "Müller")


# ======================================================================
# Happy-path tests  — the system works as intended with valid input
# ======================================================================

class TestPersonCreation:
    def test_stores_firstname(self, alice):
        assert alice.firstname == "Alice"

    def test_stores_lastname(self, alice):
        assert alice.lastname == "Müller"

    def test_str_representation(self, alice):
        assert str(alice) == "Alice Müller"

    def test_repr_contains_class_name(self, alice):
        assert "Person" in repr(alice)

    def test_repr_contains_firstname(self, alice):
        assert "Alice" in repr(alice)


class TestPersonMutation:
    def test_update_firstname(self, alice):
        alice.firstname = "Alicia"
        assert alice.firstname == "Alicia"

    def test_update_lastname(self, alice):
        alice.lastname = "Schmidt"
        assert alice.lastname == "Schmidt"

    def test_str_updates_after_name_change(self, alice):
        alice.firstname = "Bob"
        assert str(alice) == "Bob Müller"


# ======================================================================
# Edge-case tests  — boundary conditions and unusual (but valid) input
# ======================================================================

class TestPersonEdgeCases:
    def test_single_character_firstname(self):
        p = Person("A", "Nguyen")
        assert p.firstname == "A"

    def test_name_with_hyphen(self):
        p = Person("Jean-Pierre", "Dupont")
        assert p.firstname == "Jean-Pierre"

    def test_name_with_unicode(self):
        p = Person("Ångström", "Björk")
        assert p.firstname == "Ångström"

    def test_numeric_string_is_accepted(self):
        """Setters cast to str; numeric strings are technically non-empty."""
        p = Person("123", "456")
        assert p.firstname == "123"


# ======================================================================
# Error / validation tests  — the system rejects invalid input
# ======================================================================

class TestPersonValidation:
    def test_empty_firstname_raises(self):
        with pytest.raises(ValueError, match="firstname"):
            Person("", "Müller")

    def test_empty_lastname_raises(self):
        with pytest.raises(ValueError, match="lastname"):
            Person("Alice", "")

    def test_setter_empty_firstname_raises(self, alice):
        with pytest.raises(ValueError):
            alice.firstname = ""

    def test_setter_empty_lastname_raises(self, alice):
        with pytest.raises(ValueError):
            alice.lastname = ""
