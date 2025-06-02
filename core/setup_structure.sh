#!/bin/bash

# Cria diretórios
mkdir -p templates/registration
mkdir -p ../project

# Cria arquivos de templates
touch templates/registration/login.html
touch templates/registration/logout.html
touch templates/registration/signup.html
touch templates/registration/password_reset_form.html
touch templates/registration/password_reset_done.html
touch templates/registration/password_reset_confirm.html
touch templates/registration/password_reset_complete.html

# Cria arquivos Python na app core
touch urls.py
touch views.py
touch forms.py
touch models.py

# Cria arquivos do projeto principal
touch ../project/settings.py
touch ../project/urls.py

# Cria o manage.py na raiz do projeto
touch ../manage.py

echo "✅ Estrutura criada com sucesso!"
