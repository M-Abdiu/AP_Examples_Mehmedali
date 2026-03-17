"""
test_module.py
==============
Concept: Parametrized Tests
----------------------------
Instead of writing ten nearly-identical test methods, pytest.mark.parametrize
lets you describe a table of inputs + expected outcomes in one place.
pytest generates one test case per row — all shown individually in the report.

Run with:  pytest tests/test_module.py -v
"""

import pytest
from university.module import Module


# ======================================================================
# Fixtures
# ======================================================================

@pytest.fixture
def adv_prog() -> Module:
    return Module("Advanced Programming", "Advanced Python concepts", 6)


# ======================================================================
# Happy paths
# ======================================================================

class TestModuleCreation:
    def test_stores_name(self, adv_prog):
        assert adv_prog.name == "Advanced Programming"

    def test_stores_ects(self, adv_prog):
        assert adv_prog.ects == 6

    def test_str_format(self, adv_prog):
        assert str(adv_prog) == "Advanced Programming (6 ECTS)"

    def test_equality_by_name(self):
        m1 = Module("Math", "Numbers", 4)
        m2 = Module("Math", "Different description", 3)
        assert m1 == m2  # equality is name-based

    def test_inequality_different_name(self):
        m1 = Module("Math", "Numbers", 4)
        m2 = Module("Physics", "Numbers", 4)
        assert m1 != m2


# ======================================================================
# Parametrized validation — valid ECTS values
# ======================================================================

@pytest.mark.parametrize("ects", [1, 3, 6, 10, 30])
def test_valid_ects_values(ects):
    """Any positive integer should be accepted."""
    m = Module("Test", "Desc", ects)
    assert m.ects == ects


# ======================================================================
# Parametrized validation — invalid ECTS values
# ======================================================================

@pytest.mark.parametrize("bad_ects", [0, -1, -100])
def test_invalid_ects_raises(bad_ects):
    """Zero and negative values must raise ValueError."""
    with pytest.raises(ValueError, match="ects must be positive"):
        Module("Test", "Desc", bad_ects)


# ======================================================================
# Parametrized validation — invalid name / description
# ======================================================================

@pytest.mark.parametrize("field,kwargs", [
    ("name",        {"name": "",    "description": "ok",  "ects": 3}),
    ("description", {"name": "ok", "description": "",    "ects": 3}),
])
def test_empty_string_fields_raise(field, kwargs):
    """Both name and description must be non-empty."""
    with pytest.raises(ValueError, match=field):
        Module(**kwargs)
