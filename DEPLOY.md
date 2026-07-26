# Deployment: Cloudflare Pages + Theory7.net

Code staat al op GitHub: https://github.com/alexjknol-del/dersalzlampenshop.de (branch `main`).

## 1. Cloudflare Pages koppelen aan GitHub

1. Inloggen op dash.cloudflare.com
2. **Workers & Pages** &rarr; **Create application** &rarr; tab **Pages** &rarr; **Connect to Git**
3. GitHub-app autoriseren voor het account `alexjknol-del` (indien gevraagd), repo **dersalzlampenshop.de** selecteren
4. Instellingen:
   - Project name: `dersalzlampenshop-de`
   - Production branch: `main`
   - Framework preset: **None**
   - Build command: `pip install -r requirements.txt && python3 gen.py`
   - Build output directory: `public`
5. **Save and Deploy** — na een paar minuten is de site live op `dersalzlampenshop-de.pages.dev`

## 2. Domein toevoegen aan Cloudflare

1. In het Pages-project: **Custom domains** &rarr; **Set up a custom domain** &rarr; `dersalzlampenshop.de` invoeren
2. Staat het domein nog niet als "Website" (zone) in het account: **Websites** &rarr; **Add a site** &rarr; `dersalzlampenshop.de` &rarr; **Free** plan &rarr; **Continue**
3. Cloudflare toont twee nameservers (bijv. `xxx.ns.cloudflare.com` / `yyy.ns.cloudflare.com`) — deze noteren voor stap 3
4. Ook `www.dersalzlampenshop.de` toevoegen als custom domain (optioneel, voor de www-variant)

## 3. Nameservers wijzigen bij Theory7.net

1. Inloggen op het Theory7.net-klantenpaneel
2. Domeininstellingen van `dersalzlampenshop.de` openen &rarr; nameservers wijzigen
3. De twee Cloudflare-nameservers uit stap 2.3 invoeren, opslaan
4. Propagatie duurt meestal enkele minuten tot enkele uren (soms tot 24 uur)

## 4. Afronden

- Zodra de zone in Cloudflare op **Active** staat: terug naar het Pages-project &rarr; **Custom domains** &rarr; domein activeren (SSL-certificaat wordt automatisch aangemaakt, meestal binnen enkele minuten)
- Testen: https://dersalzlampenshop.de moet de site tonen met geldig HTTPS-certificaat

## Lokaal opnieuw bouwen

```
pip install -r requirements.txt
python3 gen.py
```
Output komt in `public/`.
