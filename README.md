docker build -t flask-app .
docker run -p 5000:5000 flask-app

#git remote add origin https://github.com/aaronsuns/testpy.git
git remote set-url origin git@github.com:aaronsuns/testpy.git
git push -u origin master

git config --global --edit
git commit --amend --reset-author

git config --global core.editor vim
