# dersalzlampenshop.de

Statische website (Python/Jinja2) voor dersalzlampenshop.de.

## Build

```
pip install -r requirements.txt
python3 gen.py
```

Output komt in `public/`.

## Deploy

Cloudflare Pages build settings:
- Build command: `python3 gen.py`
- Build output directory: `public`
