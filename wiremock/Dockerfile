FROM wiremock/wiremock:2.32.0-alpine

COPY wiremock/mappings /home/wiremock/mappings

EXPOSE 8080

CMD ["--verbose", "--global-response-templating"]