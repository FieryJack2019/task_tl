## Стек
  * **django 4.1**
  * **django-mptt 0.14**
  * **psycopg2 2.9**
  * **django-ajax-datatable 4**

## Тестирование
  * Для запуска тестов введите команду `python3 manage.py test`

## Сборка и запуск
  * Клонируем репозитория git clone https://github.com/FieryJack2019/task-tl-group
  * Заполняем файл **.env** на основе **.env_template** в папке *src*
  * Собираем докер образ `docker-compose up -d --build`
  
### Примечание:
Докер может долго собирать образ из-за генерации 50 000 сотрудников
