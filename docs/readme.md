
login
http://127.0.0.1:8000/accounts/login/


1. Recrie as migrações

python manage.py makemigrations

2. Se quiser fazer por app específica:

python manage.py makemigrations core habits tasks reflections reminders users

3. Aplique as migrações no novo banco

python manage.py migrate

Isso vai recriar todas as tabelas no novo banco de dados. 

4. Crie um superusuário

python manage.py createsuperuser

Execute o coletor de arquivos estáticos:
python manage.py collectstatic --noinput

Rodar o server
python manage.py runserver

Rode as migrações
python manage.py makemigrations
python manage.py migrate

Como Criar Apps no Django
python manage.py startapp activities
python manage.py startapp schedules
python manage.py startapp dashboard
python manage.py startapp reflections
python manage.py startapp reminders
python manage.py startapp users