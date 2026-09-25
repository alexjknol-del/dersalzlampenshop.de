# -*- coding: utf-8 -*-
"""Statischer Website-Generator für dersalzlampenshop.de."""
import os
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

import content as c
from blog_content import POSTS

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(ROOT, "src", "templates")
STATIC_DIR = os.path.join(ROOT, "src", "static")
OUT_DIR = os.path.join(ROOT, "public")

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=False)
base_tpl = env.get_template("base.html")

MONTHS_DE = {
    1: "Januar", 2: "Februar", 3: "März", 4: "April", 5: "Mai", 6: "Juni",
    7: "Juli", 8: "August", 9: "September", 10: "Oktober", 11: "November", 12: "Dezember",
}


def fmt_date(iso):
    d = datetime.strptime(iso, "%Y-%m-%d")
    return "{}. {} {}".format(d.day, MONTHS_DE[d.month], d.year)


def write_page(path, title, description, content_html, og_type="website", extra_head=None):
    """path z.B. '/' oder '/ueber-uns/'"""
    html = base_tpl.render(
        title=title,
        description=description,
        path=path,
        content=content_html,
        year=2026,
        og_type=og_type,
        extra_head=extra_head,
    )
    if path == "/":
        out_path = os.path.join(OUT_DIR, "index.html")
    else:
        out_dir = os.path.join(OUT_DIR, path.strip("/"))
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def post_card_html(post):
    return """
      <article class="post-card">
        <div class="post-meta">{date} &middot; {tags}</div>
        <h3><a href="/neuigkeiten/{slug}/">{title}</a></h3>
        <p class="excerpt">{excerpt}</p>
        <a class="read-more" href="/neuigkeiten/{slug}/">Weiterlesen &rarr;</a>
      </article>
    """.format(
        date=fmt_date(post["date"]),
        tags=", ".join(post["tags"]),
        slug=post["slug"],
        title=post["title"],
        excerpt=post["excerpt"],
    )


def build():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR)

    # Statische Assets kopieren
    shutil.copytree(STATIC_DIR, os.path.join(OUT_DIR, "static"))

    posts_sorted = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    preview_html = "\n".join(post_card_html(p) for p in posts_sorted[:4])

    # Startseite
    home_body = c.HOME["body"].replace("{{POSTS_PREVIEW}}", preview_html)
    write_page("/", c.HOME["title"], c.HOME["description"], home_body)

    # Über uns
    write_page(c.PAGE_UEBER_UNS["path"], c.PAGE_UEBER_UNS["title"], c.PAGE_UEBER_UNS["description"], c.PAGE_UEBER_UNS["body"])

    # Ratgeber hub
    ratgeber_body = c.PAGE_RATGEBER["body"].replace("{{POSTS_PREVIEW}}", preview_html)
    write_page(c.PAGE_RATGEBER["path"], c.PAGE_RATGEBER["title"], c.PAGE_RATGEBER["description"], ratgeber_body)

    # Größen-Guide
    write_page(c.PAGE_GROESSEN["path"], c.PAGE_GROESSEN["title"], c.PAGE_GROESSEN["description"], c.PAGE_GROESSEN["body"])

    # Pflege & Wartung
    write_page(c.PAGE_PFLEGE["path"], c.PAGE_PFLEGE["title"], c.PAGE_PFLEGE["description"], c.PAGE_PFLEGE["body"])

    # FAQ
    faq_html = "\n".join(
        '<div class="faq-item"><h3>{}</h3><p>{}</p></div>'.format(q, a) for q, a in c.FAQ_ITEMS
    )
    faq_body = c.PAGE_FAQ["body"].replace("__FAQ_ITEMS__", faq_html)
    write_page(c.PAGE_FAQ["path"], c.PAGE_FAQ["title"], c.PAGE_FAQ["description"], faq_body)

    # Autorin
    autorin_body = c.PAGE_AUTORIN["body"].replace("__BIO_LONG__", c.AUTHOR["bio_long"])
    write_page(c.PAGE_AUTORIN["path"], c.PAGE_AUTORIN["title"], c.PAGE_AUTORIN["description"], autorin_body)

    # Kontakt
    write_page(c.PAGE_KONTAKT["path"], c.PAGE_KONTAKT["title"], c.PAGE_KONTAKT["description"], c.PAGE_KONTAKT["body"])
    write_page(c.PAGE_PARTNER["path"], c.PAGE_PARTNER["title"], c.PAGE_PARTNER["description"], c.PAGE_PARTNER["body"])

    # Impressum / Datenschutz / Cookies
    write_page(c.PAGE_IMPRESSUM["path"], c.PAGE_IMPRESSUM["title"], c.PAGE_IMPRESSUM["description"], c.PAGE_IMPRESSUM["body"])
    write_page(c.PAGE_DATENSCHUTZ["path"], c.PAGE_DATENSCHUTZ["title"], c.PAGE_DATENSCHUTZ["description"], c.PAGE_DATENSCHUTZ["body"])
    write_page(c.PAGE_COOKIES["path"], c.PAGE_COOKIES["title"], c.PAGE_COOKIES["description"], c.PAGE_COOKIES["body"])

    # Blog-Index (Neuigkeiten)
    cards_html = "\n".join(post_card_html(p) for p in posts_sorted)
    blog_index_body = """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Neuigkeiten</div>
    <div class="article-head">
      <h1>Neuigkeiten</h1>
      <p class="lead">Aktuelle Beiträge rund um Himalaya-Salzlampen: Hintergrund, Pflege, Einrichtung und Nachhaltigkeit.</p>
    </div>
    <div class="post-grid">
      {cards}
    </div>
  </div>
</section>
""".format(cards=cards_html)
    write_page("/neuigkeiten/", "Neuigkeiten: Beiträge rund um Salzlampen | Der Salzlampenshop",
               "Aktuelle Beiträge von Der Salzlampenshop: Hintergrund, Pflege, Einrichtung und Nachhaltigkeit rund um Himalaya-Salzlampen.",
               blog_index_body, og_type="website")

    # Einzelne Blogartikel
    for i, post in enumerate(posts_sorted):
        body = """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; <a href="/neuigkeiten/">Neuigkeiten</a> &rsaquo; {title}</div>
    <div class="article-head">
      <h1>{title}</h1>
      <div class="byline">
        <img src="{avatar}" alt="{author}" width="46" height="46">
        <div>
          <div class="name">{author}</div>
          <div class="date">{date}</div>
        </div>
      </div>
      <div>{tags_html}</div>
    </div>
    <div class="article-body">
      {body}
    </div>
  </div>
</section>
""".format(
            title=post["title"],
            avatar=c.AUTHOR["avatar"],
            author=c.AUTHOR["name"],
            date=fmt_date(post["date"]),
            tags_html="".join('<span class="tag">{}</span>'.format(t) for t in post["tags"]),
            body=post["body"],
        )
        write_page(
            "/neuigkeiten/{}/".format(post["slug"]),
            "{} | Der Salzlampenshop".format(post["title"]),
            post["excerpt"].replace("&ndash;", "-").replace("&rsaquo;", ">"),
            body,
            og_type="article",
        )

    # robots.txt & sitemap.xml
    all_paths = ["/", "/ueber-uns/", "/ratgeber/", "/groessen-guide/", "/pflege-und-wartung/",
                 "/haeufig-gestellte-fragen/", "/autorin/", "/kontakt/", "/partner/", "/neuigkeiten/",
                 "/impressum/", "/datenschutz/", "/cookie-richtlinie/"]
    all_paths += ["/neuigkeiten/{}/".format(p["slug"]) for p in posts_sorted]

    sitemap_entries = "\n".join(
        "  <url><loc>{}{}</loc></url>".format(c.DOMAIN, p) for p in all_paths
    )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{}\n</urlset>\n'.format(sitemap_entries)
    with open(os.path.join(OUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    robots = "User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(c.DOMAIN)
    with open(os.path.join(OUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # _headers voor Cloudflare Pages (kleine security headers)
    headers_content = """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
"""
    with open(os.path.join(OUT_DIR, "_headers"), "w", encoding="utf-8") as f:
        f.write(headers_content)

    print("Build klaar: {} pagina's + {} artikelen in {}".format(len(all_paths) - len(posts_sorted), len(posts_sorted), OUT_DIR))


if __name__ == "__main__":
    build()
