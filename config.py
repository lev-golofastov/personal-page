from datetime import datetime

current_data = datetime.today().strftime('%Y-%m-%d')

SQLITE_DATABASE_NAME = "database.db"
SQLITE_DATABASE_BACKUP_NAME = 'se_backup_' + current_data + '.db'
