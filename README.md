# threading-util-light-it-academy

Пример запуска утилиты.

- python util.py --operation move --from /home/user/projects --to /root/]
python util.py --operation copy --from /home/user/projects --to /root/

Возможность копировать файлы которые соответствуют заданной маске.

- python util.py --operation copy --from /home/user/projects/*.md --to /root/

Возможность указать количество одновременно копируемых/переносимых файлов.

- python util.py --operation copy --from /home/user/projects/*.md --to /root/  --threads 5
