# Overviewer config

Наш конфиг для рендера карты Overviewer.

## Как добавлять станции метро

См. [stations.py](stations.py). Достаточно добавить там строчку с названием станции, координатами и цветом ветки метро.

После следующего рендера карты можно будет увидеть новые станции.

## Как запустить рендер карты

Нужно залогиниться на сервер и выполнить там скрипт, см. https://github.com/dq-server/scripts

## Как использовать на сервере

Достаточно скачать ZIP архив со всем кодом в этой репе и положить в папку с установкой Overviewer и выполнить:

```sh
export MINECRAFT_WORLD_DIR="<путь до папки мира>"
export MINECRAFT_MAP_DIR="<путь куда рендерить; если там уже карта, повторый рендер быстрее>"
export MINECRAFT_CLIENT_PATH="<Путь до client.jar, скачать: https://overviewer.org/textures/1.14.4>"

cd <overviewer>/config
python3 ../overviewer.py --config=config.py
python3 ../overviewer.py --config=config.py --genpoi --skip-scan
cp -r icons/* ../map/icons
```

У нас это всё происходит автоматически, см. https://github.com/dq-server/scripts
