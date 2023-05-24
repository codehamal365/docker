# [docker] https://www.keycloak.org/server/containers
# [doc quick start] https://www.keycloak.org/getting-started/getting-started-docker
# [another sso platform] https://github.com/casdoor/casdoor
FROM quay.io/keycloak/keycloak:20.0.1

ENV KEYCLOAK_ADMIN=admin \
    KEYCLOAK_ADMIN_PASSWORD=admin

EXPOSE 8080

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]