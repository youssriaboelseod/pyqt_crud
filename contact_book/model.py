"""This module provides a model to manage the contacts table."""

from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlTableModel


class ContactsModel:
    def __init__(self,tablename,*columnsname):
        self.model = self._createModel(self,tablename,columnsname)
        
    @staticmethod
    def _createModel(self,tablename,*columnsname):

        """Create and set up the model."""
        tableModel = QSqlTableModel()
        #tableModel.setTable("contacts")
        tableModel.setTable(tablename)
        tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        tableModel.select()

        #headers = ("ID", "Name", "Job", "Email")
        headers = columnsname
        for columnIndex, header in enumerate(headers):
            
            tableModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return tableModel

    def addContact(self, data):

        """Add a contact to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def deleteContact(self, row):

        """Remove a contact from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearContacts(self):

        """Remove all contacts in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()