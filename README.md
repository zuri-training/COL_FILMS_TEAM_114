# COL_FILMS_TEAM_114
My team and I will be creating a streaming platform for college students.

# Documentation Link
https://docs.google.com/document/d/185dgJovxd9ESLktB6qRdgKDNmYTTbgji_wV9UVoMr4E/edit

# Designer's Figma Link
https://www.figma.com/file/PAhnmLoO7tZTieCo4zc8Nl/Approved-designs-for-team-114?node-id=177%3A285

# Deployment
1. Create a folder: `mkdir team114`
2. Change directory to the folder: `cd team114`
3. Clone main branch to folder: `git clone --branch main https://github.com/zuri-training/COL_FILMS_TEAM_114.git .`
4. Create virtual environment: `python3 -m venv m_env`
5. Activate virtual environment: `source venv/bin/activate`
6. Install Packages: `pip install -r requirements.txt`
7. Run database migration: `python manage.py makemigrations` and `python manage.py migrate`
8. For more information: 
- `Users are found in accounts app.`
- `Main app is fount in movies app.`
- `Static folder hold all static files`
9. Using Default Templating, all pages are in the templates of each folder.
