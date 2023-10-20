FROM python:3.12-bookworm
EXPOSE 8000
WORKDIR /api
COPY requirements.txt /api
RUN pip3 install -r requirements.txt
COPY . /api
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# FROM builder as dev-envs
# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]