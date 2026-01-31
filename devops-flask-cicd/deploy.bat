@echo off
echo Deploying Flask container...

docker stop flask-app 2>nul
docker rm flask-app 2>nul

docker run -d -p 5000:5000 --name flask-app ankitkashyap845438/flask-cicd

echo Deployment completed.
