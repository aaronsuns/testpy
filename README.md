docker build -t flask-app .
docker run -p 5000:5000 flask-app

#git remote add origin https://github.com/aaronsuns/testpy.git
git remote set-url origin git@github.com:aaronsuns/testpy.git
git push -u origin master

git config --global --edit
git commit --amend --reset-author

git config --global core.editor vim


#start database
podman run --name mypostgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres:13
#start app
DATABASE_URL=postgresql://postgres:password@localhost:5432/mydatabase python app.py
#or
python app.py