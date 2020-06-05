##### Description:
```
Monster Fight
```
---
Requirements
```
python > 3.5.2

```
Notes
```
This is a sample of a text based adventure game.
Generally requiring commands with two to three words like 'unlock door' or 'go west door'.
It could use a little refining and error handling.
Sometimes unexpected death occurs - just an fyi.

```
Usage
```bash
cd monster_fight
python3 app/monster_fight.py

```
Containerization
```bash
cd monster_fight
docker build -t <custom_image_name>:<tag> .
docker run -it ---name <custom_app_name> <custom_image_name>:<tag>

