# Diplodoc

Все исходные файлы документации, подлежащие изменению лежат в [*docs*](./docs/)

Структура проекта имеет следующий вид:
```
mekstack/docs/docs
|-- .yfm                      (Файл конфигурации проекта)
|-- toc.yaml                  (Файл конфигурация боковой навигационной панели с оглавлением)
|-- index.yaml                (Скелет разводящей страницы)
|-- quick-start.md            (Контент для страницы Quick Start +Lore)
|-- heat-quick-start.md       (Контент для страницы Quick Start -Lore)
|-- cloud-native.md           (Контент для страницы Cloud Native)
|-- images.md                 (Контент для страницы Linux Autobuilds)
|-- admin.md                  (Контент для страницы Admin Guides)
|-- glossary.md               (Контент для страницы Glossary)
|-- services.md               (Контент для страницы Services)
|-- index.md                  (Контент для главной страницы)
|-- faq.md                    (Контент для страницы FAQ)
|-- images                    (Каталог с изображениями для страниц)
    |-- l2.jpg
    |-- l3-lore.png
    |-- sneedaas.png
|-- files                     (Прочее)
    |-- heat-quick-start.yaml (Манифест для разворачивания виртуалок)
```

Если нужно что-то добавить, то открываем нужный .md файл, редактируем его в синтаксисее MarkDown и создаем Pull Request. После, получившаяся документация появится на *pr-#.docs.mekstack.ru* где #-номер вашего Pull Request'a. После ревизии и merg'a изменения появятся на *master.docs.mekstack.ru*
