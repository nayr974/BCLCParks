"""adding capacity type enum pt2

Revision ID: 03f44cb281a6
Revises: 0ec17b648f68
Create Date: 2021-05-14 17:41:08.013057

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '03f44cb281a6'
down_revision = '0ec17b648f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    capacitytype = postgresql.ENUM('Trail', 'Vehicle', name='capacitytype')
    capacitytype.create(op.get_bind())
    op.add_column('trailhead', sa.Column('capacity_type', sa.Enum('Trail', 'Vehicle', name='capacitytype'), nullable=False))
    # ### end Alembic commands ###

    op.execute('''INSERT INTO trailhead (park_name, trailhead_name, capacity_type, am_capacity, pm_capacity) 
                    VALUES 
                    ('Cypress', 'Howe Sound Crest Trail', 'Trail', 380, 270), 
                    ('Cypress', 'Black Mountain Loop, Cabin Lake Trail', 'Trail', 550, 385),
                    ('Cypress', 'Yew Lake/Bowen Lookout', 'Trail', 275, 220),
                    ('Cypress', 'Hollyburn Peak, Four Lake Loop, Hollyburn Trails', 'Trail', 385 , 275),
                    ('Mount Seymour', 'Mystery Lake', 'Trail', 165, 110),
                    ('Mount Seymour', 'Goldie Flower Lake Loop Trials', 'Trail', 220, 165),
                    ('Mount Seymour', 'Dog Mountain, First Lake Loop, Dinky Peak', 'Trail', 440, 275),
                    ('Mount Seymour', 'Mt Seymour Trail, Elsay Lake', 'Trail', 440, 275),
                    ('Golden Ears', 'Boat Launch', 'Vehicle', 100, 0),
                    ('Golden Ears', 'East Canyon Trail, Lower Falls and Gold Creek', 'Vehicle', 110, 60),
                    ('Golden Ears', 'West Canyon Creek', 'Vehicle', 55, 30),
                    ('Golden Ears', 'Alouette Lake (South beach)', 'Vehicle', 790, 385),
                    ('Joffre Lakes', 'Joffre Lakes', 'Vehicle', 1650, 0),
                    ('Stawamus Chief', 'Backside Trail', 'Trail', 385, 440),
                    ('Garibaldi', 'Diamondhead', 'Vehicle', 44, 0),
                    ('Garibaldi', 'Rubble Creek', 'Vehicle', 220, 0),
                    ('Garibaldi', 'Cheakamus', 'Vehicle', 49, 39),
                    ('Mount Robson', 'Berg Lake Trail', 'Trail', 25, 25);''')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trailhead', 'capacity_type')
    capacitytype = postgresql.ENUM('Trail', 'Vehicle', name='capacitytype')
    capacitytype.drop(op.get_bind())
    # ### end Alembic commands ###