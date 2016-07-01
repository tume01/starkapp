mysqladmin -u root -p  drop starkapp
mysqladmin -u root -p  create starkapp
find -type d -name migrations -exec rm -rf {} \;
git checkout .
python3.4 manage.py makemigrations
python3.4 manage.py migrate
python3.4 manage.py seed_all