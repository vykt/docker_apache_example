# Using alpine running apache
FROM debian:stable
MAINTAINER castile

RUN apt update
RUN apt install -y curl
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt install -y python3-pip
RUN pip install Flask
RUN pip install Flask-RESTful

EXPOSE 80
ENTRYPOINT ["apache2ctl"]
CMD ["-DFOREGROUND"]
