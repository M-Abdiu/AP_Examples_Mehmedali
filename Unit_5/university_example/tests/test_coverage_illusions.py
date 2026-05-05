"""
test_coverage_illusions.py
==========================
Concept: Test Coverage Illusions
----------------------------------
Coverage reports show which LINES were executed — not whether your
tests actually verify anything meaningful.

This file demonstrates three classic coverage traps:

  Trap 1 — Covered lines, zero assertions
  Trap 2 — Line coverage hides untested branches (branch coverage)
  Trap 3 — 100% coverage with a latent bug still present

After running:
  pytest tests/test_coverage_illusions.py -v --cov=university --cov-report=term-missing

...notice that coverage can look great even when tests are weak.

Run with:  pytest tests/test_coverage_illusions.py -v
"""

import pytest
from university.module import Module
from university.student import Student


# ======================================================================
# 1.  TRAP: High coverage, but no assertions ("assertion-free tests")
#     Coverage sees these lines as "covered" — but we prove nothing.
# ======================================================================

class TestCoverageWithNoAssertions:
    """
    These tests execute code and raise the coverage percentage,
    but they assert NOTHING — bugs would pass silently.

    This is a real anti-pattern seen in production codebases.
    """

    def test_student_str_UNCHECKED(self):
        s = Student("Anna", "Müller", "100001")
        str(s)                   # line executed ✓ — but output never verified
        # Missing: assert str(s) == "Anna Müller (100001)"


class TestUncoveredBranches:
    """
    These fill the real gaps identified by pytest-cov in the last run:
      - module.py:  __repr__, description property
      - student.py: student_count(), __repr__,
                    NotImplemented branches in __eq__ / __lt__
    """

    # --- Module.__repr__ and description property (previously 0 hits) ---

    def test_module_repr(self):
        m = Module("Math", "Calculus", 4)
        r = repr(m)
        assert "Module(name=" in r
        assert "Calculus" in r

    def test_module_description_getter(self):
        m = Module("Math", "Calculus", 4)
        assert m.description == "Calculus"

    # --- Student.__repr__ ---

    def test_student_repr(self):
        s = Student("Anna", "Müller", "100001")
        r = repr(s)
        assert "Student(student_id=" in r
        assert "100001" in r

    # --- Student.student_count() ---

    def test_student_count_increases(self):
        before = Student._counter
        Student("New", "Student", "555001")
        assert Student._counter == before + 1

    # --- NotImplemented branches ---

    def test_student_eq_with_non_student_returns_not_implemented(self):
        s = Student("Anna", "Müller", "100001")
        # Python calls __eq__ and gets NotImplemented → falls back to id comparison
        assert s.__eq__("not a student") is NotImplemented

    def test_student_lt_with_non_student_returns_not_implemented(self):
        s = Student("Anna", "Müller", "100001")
        assert s.__lt__(42) is NotImplemented

    def test_module_eq_with_non_module_returns_not_implemented(self):
        m = Module("Math", "Calculus", 4)
        assert m.__eq__("not a module") is NotImplemented


# ======================================================================
# Summary discussion points for class
# ======================================================================
#
# Q: We had 95% coverage before adding TestUncoveredBranches.
#    Were our tests good enough?
#
# A: Depends what "good" means.
#    - The uncovered __repr__ methods are low-risk.
#    - The NotImplemented branches protect against type errors in
#      sorted() / comparisons — worth covering.
#    - The is_eligible_for_honours bug NEVER appeared in coverage
#      reports — coverage said 100%, yet the bug survived.
#
# Key insight: coverage is a FLOOR (minimum bar), not a CEILING.
#   High coverage → you haven't skipped obvious paths.
#   High coverage ≠ your tests are correct or complete.
#
# Tools to go further:
#   --cov-branch          branch coverage (catches 'or' vs 'and' bugs)
#   mutmut / cosmic-ray   mutation testing (plants bugs, checks tests catch them)
