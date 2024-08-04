docker build -t flask-app .
docker run --network host -p 5000:5000 flask-app
