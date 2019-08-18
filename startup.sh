sudo docker build -t webimage .
sudo docker run -d -p 80:2000 --name todoserver --mount type=bind,source="${PWD}",target=/code/ webimage