docker build -t dockerfile:v1 .

docker save dockerfile:v1 > my_image.tar 

docker run dockerfile:v1

docker compose up (converts .yml into an image and builds it)

