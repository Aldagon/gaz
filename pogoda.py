# .gitlab-ci.yml

# Этап настройки
stages:
  - build
  - deploy

# Определение переменных окружения
variables:
  APP_NAME: "my-app"
  SSH_PRIVATE_KEY: "$SSH_PRIVATE_KEY"

# Сборка приложения
build:
  stage: build
  script:
    - echo "Building the application..."
    # Здесь могут быть шаги по установке зависимостей и компиляции кода
  only:
    - master # Запускать пайплайн только для ветки master

# Развертывание приложения на сервере
deploy:
  stage: deploy
  script:
    - echo "Deploying the application..."
    # SSH-ключ должен быть добавлен в настройках CI/CD проекта на GitLab
    - mkdir -p ~/.ssh
    - echo "$SSH_PRIVATE_KEY" | tr -d '\r' > ~/.ssh/id_rsa
    - chmod 600 ~/.ssh/id_rsa
    # Копирование собранного приложения на сервер
    - scp -r ./my-app/* user@server:/path/to/deployment
  only:
    - master # Запускать пайплайн только для ветки master
