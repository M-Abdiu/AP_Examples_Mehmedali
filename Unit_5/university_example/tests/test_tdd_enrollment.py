"""
test_tdd_enrollment.py
======================
Concept: Test-Driven Development (TDD)
---------------------------------------
TDD cycle:  RED → GREEN → REFACTOR

This file was written BEFORE EnrollmentService existed.
The comments mark each TDD step so you can replay the process live.

  Step 1 (RED):    write a failing test first
  Step 2 (GREEN):  write the minimum code to make it pass
  Step 3 (REFACTOR): clean up without breaking tests

After running through all steps below, the full EnrollmentService
implementation appears at the bottom of this file.

Run with:  pytest tests/test_tdd_enrollment.py -v
"""

import pytest
from university.module import Module
from university.student import Student


# ======================================================================
# The class we are TDD-ing  (would normally live in its own file)
# ======================================================================

class EnrollmentService:
    """
    Manages enrollment rules on top of the basic Student.enroll() method.

    Rules:
    - A student may not exceed MAX_MODULES enrolled modules at once.
    - A module may not exceed MAX_CAPACITY students.
    - Duplicate enrollment attempts are silently ignored (idempotent).
    """

    MAX_MODULES = 5
    MAX_CAPACITY = 30

    def __init__(self) -> None:
        # { module_name: [student, ...] }
        self._rosters: dict[str, list[Student]] = {}

    def enroll(self, student: Student, module: Module) -> None:
        """Enroll a student in a module, enforcing business rules."""
        # Idempotent: already enrolled → do nothing
        if module in student.modules:
            return

        # Rule 1: student module limit
        if len(student.modules) >= self.MAX_MODULES:
            raise ValueError(
                f"{student} already has {self.MAX_MODULES} modules (limit reached)."
            )

        # Rule 2: module capacity
        roster = self._rosters.setdefault(module.name, [])
        if len(roster) >= self.MAX_CAPACITY:
            raise ValueError(
                f"Module '{module}' is full ({self.MAX_CAPACITY} students)."
            )

        student.enroll(module)
        roster.append(student)

    def roster(self, module: Module) -> list[Student]:
        """Return the list of students enrolled in a module."""
        return list(self._rosters.get(module.name, []))

    def drop(self, student: Student, module: Module) -> None:
        """Remove a student from a module roster (does NOT touch student._modules)."""
        roster = self._rosters.get(module.name, [])
        if student in roster:
            roster.remove(student)


# ======================================================================
# TDD Step 1 (RED) → Step 2 (GREEN): basic enrollment
# ======================================================================

class TestEnrollmentBasic:
    """
    TDD iteration 1 — write these tests first, watch them fail,
    then add the minimal EnrollmentService skeleton.
    """

    def test_student_is_enrolled_in_module(self):
        service = EnrollmentService()
        student = Student("Anna", "Müller", "200001")
        module = Module("Advanced Programming", "AP", 6)

        service.enroll(student, module)

        assert module in student.modules

    def test_enrolled_student_appears_on_roster(self):
        service = EnrollmentService()
        student = Student("Ben", "Keller", "200002")
        module = Module("Math", "Calculus", 4)

        service.enroll(student, module)

        assert student in service.roster(module)

    def test_empty_roster_for_unknown_module(self):
        service = EnrollmentService()
        module = Module("Physics", "Mechanics", 3)
        assert service.roster(module) == []


# ======================================================================
# TDD Step 2 (GREEN): idempotency
# ======================================================================

class TestEnrollmentIdempotency:
    """
    TDD iteration 2 — after basic enrollment works, drive out the
    duplicate-enrollment rule with these tests.
    """

    def test_duplicate_enroll_is_ignored(self):
        service = EnrollmentService()
        student = Student("Cara", "Wang", "200003")
        module = Module("Advanced Programming", "AP", 6)

        service.enroll(student, module)
        service.enroll(student, module)  # second call: should not raise

        assert len(student.modules) == 1

    def test_roster_not_duplicated(self):
        service = EnrollmentService()
        student = Student("Dario", "Senn", "200004")
        module = Module("Advanced Programming", "AP", 6)

        service.enroll(student, module)
        service.enroll(student, module)

        assert service.roster(module).count(student) == 1


# ======================================================================
# TDD Step 3 (REFACTOR): business-rule enforcement
# ======================================================================

class TestEnrollmentBusinessRules:
    """
    TDD iteration 3 — drive out the capacity and module-limit rules.
    These tests define the behaviour BEFORE the rule is implemented.
    """

    def test_student_cannot_exceed_max_modules(self):
        service = EnrollmentService()
        student = Student("Eva", "Bauer", "200005")
        modules = [Module(f"Module{i}", "Desc", 3) for i in range(EnrollmentService.MAX_MODULES)]

        for m in modules:
            service.enroll(student, m)

        extra_module = Module("OneModuleTooMany", "Desc", 3)
        with pytest.raises(ValueError, match="limit reached"):
            service.enroll(student, extra_module)

    def test_module_cannot_exceed_max_capacity(self):
        service = EnrollmentService()
        module = Module("Tiny Module", "Very small class", 3)

        # Fill the module to capacity
        for i in range(EnrollmentService.MAX_CAPACITY):
            s = Student("Name", f"Student{i}", str(100000 + i))
            service.enroll(s, module)

        overflow_student = Student("Late", "Joiner", "999999")
        with pytest.raises(ValueError, match="full"):
            service.enroll(overflow_student, module)

    def test_exactly_at_capacity_is_accepted(self):
        service = EnrollmentService()
        module = Module("Full Module", "Desc", 3)

        # Enroll MAX_CAPACITY - 1 students, then one more → should be fine
        for i in range(EnrollmentService.MAX_CAPACITY - 1):
            s = Student("Name", f"Student{i}", str(100000 + i))
            service.enroll(s, module)

        last = Student("Last", "Student", "888888")
        service.enroll(last, module)  # should NOT raise
        assert len(service.roster(module)) == EnrollmentService.MAX_CAPACITY


# ======================================================================
# Drop functionality
# ======================================================================

class TestDrop:
    def test_drop_removes_from_roster(self):
        service = EnrollmentService()
        student = Student("Frank", "Huber", "200006")
        module = Module("Advanced Programming", "AP", 6)

        service.enroll(student, module)
        service.drop(student, module)

        assert student not in service.roster(module)

    def test_drop_nonexistent_student_does_not_raise(self):
        service = EnrollmentService()
        student = Student("Ghost", "User", "200007")
        module = Module("Advanced Programming", "AP", 6)

        service.drop(student, module)  # should not raise
