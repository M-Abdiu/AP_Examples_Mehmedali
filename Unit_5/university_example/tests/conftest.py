"""
conftest.py
===========
pytest discovers this file automatically.
Fixtures defined here are available to ALL test files without importing.
"""
import pytest
from university.module import Module
from university.student import Student


@pytest.fixture
def ap_module():
    return Module("Advanced Programming", "Advanced Python concepts", 6)


@pytest.fixture
def math_module():
    return Module("Mathematics", "Calculus and linear algebra", 4)


@pytest.fixture
def student_anna():
    return Student("Anna", "Zimmermann", "100001")


@pytest.fixture
def student_ben():
    return Student("Ben", "Andersen", "100002")
