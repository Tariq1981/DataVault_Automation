# DataVault_Automation
Automation for Tables Creation

data_vault.py: Is ascript which automate the tables creation for the Hub,Links and Satellites in Data Vault.
It uses SQLAlchemy for Teradata database. It can be replaced with any driver for any database and will need some minor updates if you target another database.
It creates the tables with all technical columns needed.
data_vault.xlsx: Sample input excel file for the script. It lists only the columns related to the business of the table without any technical columns recomened by Data Vault model.
