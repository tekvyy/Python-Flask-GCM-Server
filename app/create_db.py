__author__ = 'tekvy'
from app import db
from app.usermodel import User


db.create_all()

# insert

db.session.add(User("Divgun Singh", "divgun.gta2@gmail.com", "1234", "APA91bFsP-Lv-e_Umy74f1yZ0MZXywGNStJ8n8UdsAwixaIGF1ILjSuVV8yyoGw3jTDSo-eTv1G63nyQ5rV-IgsbaLU_SdCR1QiqW-kWZ___Kcq_b-ZbWC3AzMHpDODZMMX8zmK_clGZPfrA9yWcDITNwi0hJG_DqQ"))

db.session.add(User("Sween", "sween@gmail.com", "1234", "APA91bH4NTGgB4R9yPbkrkPdE_4QCDJwd8ZsNOS3cdVf-CNRH8z3nj-pgqvqdTjOWbDqNn5IhjufKvePJJj-QrVpn98t10Sz6-jeujiSWaQGm-n5M1ZtLcv2uwj_V6a-YQlfKq2uSjNbY4TTQxkzLNJtB2YazxdrGQ"))
# commit the changes
db.session.commit()




