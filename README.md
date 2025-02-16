# electronics_store

## Описание проекта
Этот проект представляет собой веб-приложение с API-интерфейсом сети по продаже электроники. Сеть представляет собой дерево цепочки поставок оборудования и связи оборудования с поставщиками.

## Запуск в Docker
Для запуска проекта в Docker выполните следующие шаги:

1. Убедитесь, что у вас установлен Docker.
2. Перейдите в корневую директорию проекта.
3. Постройте Docker-образ:
    ```sh
    docker build -t electronics_store .
    ```
4. Запустите контейнер:
    ```sh
    docker run -p 8000:8000 electronics_store
    ```
5. Откройте браузер и перейдите по адресу `http://localhost:8000`, чтобы увидеть работающий проект.
