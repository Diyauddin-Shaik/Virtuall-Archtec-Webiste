1️⃣ Clone Project from CMD

Open Command Prompt and run:

git clone <your-github-repo-url>

Example:

git clone https://github.com/username/interior-design-project.git

Then go inside the project folder:

cd interior-design-project
2️⃣ Open Project in VS Code

Run:

code .

This opens the project in VS Code.

3️⃣ Open VS Code Terminal

In VS Code press:

Ctrl + `

or go to:

Terminal → New Terminal

Now all commands will run inside VS Code.

4️⃣ Create Virtual Environment

Run:

python -m venv venv

This creates:

venv/
5️⃣ Activate Virtual Environment

Windows:

venv\Scripts\activate

Now terminal will show:

(venv)
6️⃣ Install Required Packages

Since your project uses Django + Pillow (image upload):

pip install django
pip install pillow

Better method (recommended if you uploaded requirements.txt):

pip install -r requirements.txt
7️⃣ Run Migrations

Because cloned projects don’t contain a database.

Run:

python manage.py makemigrations

Then:

python manage.py migrate

This creates:

db.sqlite3
8️⃣ Create Admin User (Optional)

If they want to access admin panel:

python manage.py createsuperuser

Example:

Username: admin
Email: admin@gmail.com
Password: ********
9️⃣ Run Django Server
python manage.py runserver

Server will start:

http://127.0.0.1:8000/
🔟 Open Website

User website:

http://127.0.0.1:8000

Admin panel:

http://127.0.0.1:8000/admin
⭐ Complete Commands (VS Code Terminal)

After opening VS Code:

python -m venv venv

venv\Scripts\activate

pip install django
pip install pillow

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
⚠️ One Important GitHub Tip

Do NOT upload these folders to GitHub:

venv/
__pycache__/
db.sqlite3

Create a .gitignore file containing:

venv/
__pycache__/
db.sqlite3
*.pyc
🚀 Your Project is Now Fully Shareable

Your friend can:

Clone → Setup → Run

