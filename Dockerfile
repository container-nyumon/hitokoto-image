# ---- 1段目：作る
FROM python:3.14 AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---- 2段目：動かす（一般のユーザー 10001 で動く）
FROM python:3.14-slim
COPY --from=build /install /usr/local
WORKDIR /app
COPY main.py .
COPY templates ./templates
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
RUN useradd --uid 10001 --create-home appuser
# Kubernetes の runAsNonRoot が確かめられるように、ユーザーは番号で指定する
USER 10001
EXPOSE 8000
CMD ["fastapi", "run", "main.py", "--port", "8000"]
