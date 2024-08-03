docker build -t flask-app .
docker run -p 5000:5000 flask-app

#git remote add origin https://github.com/aaronsuns/pytest.git
git remote set-url origin git@github.com:aaronsuns/pytest.git
git push -u origin master

