FROM postgres:14.4-alpine

# [maintenance]-[BEGIN]
#   Add maintenance scripts and make them executable
#ARG SOURCE_DIR=./docker/dev/postgres
ARG SOURCE_DIR=.

ARG TEMP_DIR=/usr/local/bin/maintenance
COPY ${SOURCE_DIR}/maintenance ${TEMP_DIR}
RUN chmod +x ${TEMP_DIR}/* \
    && mv ${TEMP_DIR}/* /usr/local/bin \
    && rmdir ${TEMP_DIR}
# [maintenance]-[END]

#COPY ./docker/dev/postgres/conf/pg_hba.conf /var/lib/postgresql/data/pg_hba.conf
