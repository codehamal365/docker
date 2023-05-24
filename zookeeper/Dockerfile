FROM bitnami/zookeeper:latest

COPY zookeeper/file /file

COPY zookeeper/init.sh /init.sh
#COPY zookeeper/custom-entrypoint.sh /opt/bitnami/scripts/zookeeper/custom-entrypoint.sh

#ENV line=37
RUN export line="$(cat /opt/bitnami/scripts/zookeeper/entrypoint.sh | wc -l)" \
    && sed "${line} i\zkServer.sh start && sleep 10 && sh /init.sh && zkServer.sh stop" \
    -i /opt/bitnami/scripts/zookeeper/entrypoint.sh


ENTRYPOINT [ "/opt/bitnami/scripts/zookeeper/entrypoint.sh" ]
CMD ["/opt/bitnami/scripts/zookeeper/run.sh"]
