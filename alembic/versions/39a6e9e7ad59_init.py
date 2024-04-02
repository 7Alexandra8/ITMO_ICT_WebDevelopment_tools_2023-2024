"""Init

Revision ID: 39a6e9e7ad59
Revises: 38c6f146fd11
Create Date: 2024-04-02 20:52:10.754926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39a6e9e7ad59'
down_revision: Union[str, None] = '38c6f146fd11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
