from sqlmodel import SQLModel

from app.database.base import get_metadata


def test_get_metadata_returns_sqlmodel_metadata() -> None:
    assert get_metadata() is SQLModel.metadata
