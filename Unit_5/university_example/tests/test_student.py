"""
test_student.py
===============
Concept: Testing Inheritance & Composite Behaviour
----------------------------------------------------
Student inherits from Person, so we verify:
  1. Inherited behaviour still works (don't assume)
  2. New behaviour works (enrollment, ordering, equality)
  3. Interactions between the two layers work correctly

Run with:  pytest tests/test_student.py -v
"""

import pytest
from university.module import Module
from university.student import Student


# ======================================================================
# Fixtures
# ======================================================================

@pytest.fixture
def ap_module() -> Module:
    return Module("Advanced Programming", "Advanced Python", 6)

@pytest.fixture
def math_module() -> Module:
    return Module("Mathematics", "Linear algebra & calculus", 4)

@pytest.fixture
def student_a() -> Student:
    return Student("Anna", "Zimmermann", "100001")

@pytest.fixture
def student_b() -> Student:
    return Student("Ben", "Andersen", "100002")


# ======================================================================
# Inherited behaviour — still tested explicitly
# ======================================================================

class TestStudentInheritance:
    def test_firstname_stored(self, student_a):
        assert student_a.firstname == "Anna"

    def test_lastname_stored(self, student_a):
        assert student_a.lastname == "Zimmermann"

    def test_str_includes_student_id(self, student_a):
        assert "100001" in str(student_a)

    def test_str_format(self, student_a):
        assert str(student_a) == "Anna Zimmermann (100001)"


# ======================================================================
# Student-specific validation
# ======================================================================

class TestStudentValidation:
    def test_non_digit_student_id_raises(self):
        with pytest.raises(ValueError, match="student_id"):
            Student("Anna", "Müller", "ABC123")

    def test_empty_student_id_raises(self):
        with pytest.raises(ValueError):
            Student("Anna", "Müller", "")

    @pytest.mark.parametrize("valid_id", ["1", "000001", "999999"])
    def test_valid_student_ids(self, valid_id):
        s = Student("Test", "User", valid_id)
        assert s.student_id == valid_id


# ======================================================================
# Enrollment behaviour
# ======================================================================

class TestStudentEnrollment:
    def test_enroll_adds_module(self, student_a, ap_module):
        student_a.enroll(ap_module)
        assert ap_module in student_a.modules

    def test_enroll_same_module_twice_is_idempotent(self, student_a, ap_module):
        student_a.enroll(ap_module)
        student_a.enroll(ap_module)
        assert len(student_a.modules) == 1

    def test_enroll_multiple_modules(self, student_a, ap_module, math_module):
        student_a.enroll(ap_module)
        student_a.enroll(math_module)
        assert len(student_a.modules) == 2

    def test_modules_returns_tuple(self, student_a, ap_module):
        student_a.enroll(ap_module)
        assert isinstance(student_a.modules, tuple)

    def test_modules_immutable_from_outside(self, student_a, ap_module):
        """Direct mutation of the returned tuple should not affect the student."""
        student_a.enroll(ap_module)
        modules_copy = student_a.modules
        # Tuples are immutable — this would raise AttributeError if someone
        # tried modules_copy.append(...)
        assert not hasattr(modules_copy, "append")


# ======================================================================
# Equality and ordering (from @total_ordering)
# ======================================================================

class TestStudentOrdering:
    def test_equality_by_student_id(self, student_a):
        clone = Student("Different", "Name", "100001")
        assert student_a == clone

    def test_inequality_different_id(self, student_a, student_b):
        assert student_a != student_b

    def test_sort_by_lastname_then_firstname(self, student_a, student_b):
        # Andersen < Zimmermann alphabetically
        assert student_b < student_a

    def test_sorted_list(self):
        students = [
            Student("Zara", "Weber", "300001"),
            Student("Anna", "Andersen", "300002"),
            Student("Mark", "Andersen", "300003"),
        ]
        result = sorted(students)
        # Andersen (Anna) < Andersen (Mark) < Weber (Zara)
        assert result[0].firstname == "Anna"
        assert result[1].firstname == "Mark"
        assert result[2].lastname == "Weber"
