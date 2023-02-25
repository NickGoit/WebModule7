"""Added Teachers

Revision ID: f67cb1820876
Revises: aae3bf3d8288
Create Date: 2023-02-24 21:36:49.115042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f67cb1820876'
down_revision = 'aae3bf3d8288'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('disciplines', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'disciplines', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'disciplines', type_='foreignkey')
    op.drop_column('disciplines', 'teacher_id')
    op.drop_table('teachers')
    # ### end Alembic commands ###
