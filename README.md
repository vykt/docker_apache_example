# docker_apache_example
Example Dockerfile running Apache2 on Debian stable.
It is probably possible to port it to Debian stable-slim, reducing image size to 25Mb.


 --- BUILD CONTAINER:

docker build -t example-apache:debian-stable .


 --- GET IP OF CONTAINER:

docker inspect <container name> | grep IP


 --- INTERACT W/ API:

Using the IP provided by the above command:

curl -X POST https://<ip>:5000/push=<value>	- Push to page
curl -X DELETE https://<ip>:5000/		- Pop from page

To view the page/stack, connect to <ip> on port 80. Apache should send the page.
