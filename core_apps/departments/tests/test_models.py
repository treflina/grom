import pytest


@pytest.mark.django_db
def test_str_department(department_factory):
    """Test department's string representation"""
    department = department_factory(name="Test Name")

    assert str(department) == "Test Name"
