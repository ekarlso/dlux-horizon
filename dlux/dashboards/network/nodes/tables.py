from horizon import tables


class NodesTable(tables.DataTable):
    id = tables.Column('id', verbose_name='Identifier')
    type = tables.Column('type')
    properties = tables.Column("properties['tables']")
