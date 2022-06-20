# docker_apache_example
Example Dockerfile running Apache2 on Debian stable.
It is probably possible to port it to Debian stable-slim, reducing image size to 25Mb.


 --- BUILD CONTAINER:

docker build -t example-apache:debian-stable .


 --- GET IP OF CONTAINER (obsolete):

docker inspect <container name> | grep IP


 --- INTERACT W/ API:

Apache server is bound to port 5080 on host. Flask API is bound to port 5001 on host.

curl -X POST localhost:5001/push=<value>	- Push to page
curl -X DELETE localhost:5001/				- Pop from page

To view the page/stack, connect to localhost on port 5080. Apache should send the page.
