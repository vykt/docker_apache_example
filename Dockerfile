#Using alpine running apache
FROM debian:stable
MAINTAINER castile

# Installs
RUN apt update
RUN apt install -y curl
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt install -y python3-pip
RUN pip install Flask
RUN pip install Flask-RESTful
RUN apt install -y supervisor

ADD api.py /api.py
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup
RUN echo '' > /var/www/html/index.html
EXPOSE 80 5000

# Run
ENTRYPOINT ["/usr/bin/supervisord"]

#ENTRYPOINT ["apache2ctl"]
#CMD ["-DFOREGROUND"]
