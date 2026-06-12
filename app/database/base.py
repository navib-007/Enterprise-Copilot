from __future__ import annotations

from sqlmodel import SQLModel

from app import models  # noqa: F401


def get_metadata() -> SQLModel.metadata.__class__:
    return SQLModel.metadata
