# docker_apache_example
Example Dockerfile running Apache2 on Debian stable.
It is probably possible to port it to Debian stable-slim, reducing image size to 25Mb.


Build container:

docker build -t example-apache:debian-stable .


Get IP of container:

docker inspect <container name> | grep IP


Take the IP provided by the above command.




It's supposed to work with just "https://localhost:80", however
it doesn't let me connect & that' all beyond the scope of this.
