FROM aquasec/trivy:latest

RUN mkdir -p .cache
RUN chmod -R 777 .cache
RUN mkdir -p .contrib
RUN chmod -R 777 .contrib

RUN apk update
RUN apk --no-cache add curl
RUN curl -o .contrib/html.tpl https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl



ENTRYPOINT []
