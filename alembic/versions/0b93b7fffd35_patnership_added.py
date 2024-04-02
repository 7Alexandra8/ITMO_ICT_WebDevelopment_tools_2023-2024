"""patnership added

Revision ID: 0b93b7fffd35
Revises: 39a6e9e7ad59
Create Date: 2024-04-02 23:04:27.251725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b93b7fffd35'
down_revision: Union[str, None] = '39a6e9e7ad59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
