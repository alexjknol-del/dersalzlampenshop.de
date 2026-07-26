# -*- coding: utf-8 -*-
"""Alle redaktionellen Inhalte für dersalzlampenshop.de."""

SITE_NAME = "Der Salzlampenshop"
DOMAIN = "https://dersalzlampenshop.de"
PARTNER_URL = "https://himalayastyling.de/"
PARTNER_NAME = "HimalayaStyling"

AUTHOR = {
    "name": "Lina Ahrens",
    "role": "Redakteurin für Wohnen &amp; Wellness",
    "avatar": "/static/img/autorin-lina.svg",
    "bio_short": "Lina schreibt seit Jahren über natürliche Wohnaccessoires, Raumgestaltung und nachhaltigen Alltag. Bei Der Salzlampenshop kümmert sie sich um Ratgeber und Neuigkeiten rund um Himalaya-Salzlampen.",
    "bio_long": """
      <p>Lina Ahrens beschäftigt sich seit über acht Jahren mit Wohnthemen, die zwischen Ästhetik und Alltagstauglichkeit liegen: natürliche Materialien, ruhige Beleuchtung und Einrichtungsgegenstände, die länger als eine Saison überzeugen. Bevor sie für Der Salzlampenshop schrieb, veröffentlichte sie Beiträge zu nachhaltigem Wohnen und Raumklima für mehrere deutschsprachige Wohnmagazine.</p>
      <p>Ihr Zugang zu Himalaya-Salzlampen ist bewusst nüchtern: Sie schätzt sie in erster Linie als warmes, dekoratives Licht mit einer angenehmen Optik aus Naturstein &ndash; und schreibt genauso offen darüber, welche Wirkungen wissenschaftlich belegt sind und welche eher zum Erfahrungsschatz vieler Nutzer gehören, ohne dass es dafür bislang eindeutige Studien gibt.</p>
      <p>Auf Der Salzlampenshop testet und vergleicht sie Größen, Formen und Pflegehinweise, damit Leserinnen und Leser eine Lampe finden, die tatsächlich zu ihrem Raum und ihren Erwartungen passt.</p>
    """,
}

NAV_PAGES = [
    ("/", "Startseite"),
    ("/ueber-uns/", "Über uns"),
    ("/ratgeber/", "Ratgeber"),
    ("/neuigkeiten/", "Neuigkeiten"),
    ("/kontakt/", "Kontakt"),
]

# ---------------------------------------------------------------------------
# STARTSEITE
# ---------------------------------------------------------------------------

HOME = {
    "title": "Himalaya-Salzlampen: Ratgeber, Größen &amp; Kaufberatung | Der Salzlampenshop",
    "description": "Unabhängiger deutschsprachiger Ratgeber zu Himalaya-Salzlampen: Wirkung, Größen, Pflege und ehrliche Kaufberatung. Empfehlung für den Kauf: HimalayaStyling.",
    "path": "/",
    "body": """
<section class="hero">
  <div class="container">
    <div>
      <span class="hero-eyebrow">Unabhängiger Ratgeber</span>
      <h1>Alles über Himalaya-Salzlampen &ndash; verständlich, ehrlich, ohne Übertreibung</h1>
      <p class="lead">Der Salzlampenshop erklärt, wie Himalaya-Salzlampen entstehen, welche Größe zu welchem Raum passt, wie man sie pflegt &ndash; und was an den vielen Versprechen rund um ihre Wirkung wirklich dran ist.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/ratgeber/">Zum Ratgeber</a>
        <a class="btn btn-secondary" href="https://himalayastyling.de/" rel="noopener">Salzlampen ansehen bei HimalayaStyling</a>
      </div>
    </div>
    <div class="hero-visual">
      <h3>Was Sie hier finden</h3>
      <ul>
        <li>Größen-Guide für jeden Raum, von 3 bis 140&nbsp;kg</li>
        <li>Pflege- und Reinigungstipps, damit die Lampe lange schön bleibt</li>
        <li>Aktuelle Beiträge zu Wirkung, Feng Shui und nachhaltigem Wohnen</li>
        <li>Ehrliche Einordnung: Was ist belegt, was ist Erfahrungswert?</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Warum ein eigener Ratgeber für Salzlampen?</h2>
      <p>Rund um Himalaya-Salzlampen kursieren viele Behauptungen &ndash; von seriös bis fragwürdig. Der Salzlampenshop ordnet ein, was tatsächlich bekannt ist, und was eher Erfahrungswissen vieler Nutzerinnen und Nutzer ist.</p>
    </div>
    <div class="grid">
      <div class="card">
        <span class="icon">&#127960;&#65039;</span>
        <h3>Herkunft &amp; Herstellung</h3>
        <p>Woher das Salz stammt, wie eine Lampe entsteht und woran man Qualität erkennt.</p>
      </div>
      <div class="card">
        <span class="icon">&#128207;</span>
        <h3>Größe &amp; Raumwahl</h3>
        <p>Von der kompakten 3-kg-Lampe auf dem Nachttisch bis zur XL-Lampe für offene Wohnräume.</p>
      </div>
      <div class="card">
        <span class="icon">&#10024;</span>
        <h3>Pflege &amp; Haltbarkeit</h3>
        <p>Warum Salz Feuchtigkeit zieht, wie man das vermeidet und die Lampe jahrelang nutzt.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Aktuelle Beiträge</h2>
      <p>Neues aus dem Ratgeber &ndash; frisch, saisonal und ohne Fülltext.</p>
    </div>
    <div class="post-grid" id="home-posts">
      {{POSTS_PREVIEW}}
    </div>
    <p class="text-center" style="margin-top:30px;">
      <a class="btn btn-secondary" href="/neuigkeiten/">Alle Beiträge lesen</a>
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band">
      <h2>Salzlampe gefunden &ndash; wo kaufen?</h2>
      <p>Der Salzlampenshop verkauft selbst nicht. Für den Kauf empfehlen wir <a href="https://himalayastyling.de/" rel="noopener" style="color:#fff;text-decoration-color:rgba(255,255,255,0.6);">HimalayaStyling</a>, spezialisiert auf natürliche Salzlampen von handlichen Modellen bis zu außergewöhnlichen XL-Lampen bis 140&nbsp;kg.</p>
      <a class="btn btn-primary" href="https://himalayastyling.de/" rel="noopener">Zu HimalayaStyling</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Kurz erklärt</h2>
    </div>
    <div class="grid">
      <div class="card">
        <h3>Was ist eine Himalaya-Salzlampe?</h3>
        <p>Ein aus Steinsalzblöcken gefertigter Lampenkörper, meist aus der Region des Punjab in Pakistan, mit integrierter Glühbirne. Das Licht scheint durch das Salz und erzeugt den charakteristischen warmen, orange-rosa Schein.</p>
      </div>
      <div class="card">
        <h3>Wofür wird sie genutzt?</h3>
        <p>Vor allem als stimmungsvolles Ambientelicht in Wohn- und Schlafräumen, häufig auch in Praxen für Massage, Yoga oder Wellness &ndash; wegen der ruhigen Optik, nicht als Ersatz für medizinische Behandlung.</p>
      </div>
      <div class="card">
        <h3>Was sollte man vor dem Kauf wissen?</h3>
        <p>Gewicht und Größe passend zum Raum wählen, auf einen stabilen Holzsockel achten und wissen, dass die Lampe bei hoher Luftfeuchtigkeit Wasser anziehen kann. Mehr dazu im <a href="/pflege-und-wartung/">Pflege-Ratgeber</a>.</p>
      </div>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# ÜBER UNS
# ---------------------------------------------------------------------------

PAGE_UEBER_UNS = {
    "title": "Über uns | Der Salzlampenshop",
    "description": "Der Salzlampenshop ist ein unabhängiges deutschsprachiges Informationsportal rund um Himalaya-Salzlampen. Erfahren Sie, wer hinter der Seite steht und was sie bezweckt.",
    "path": "/ueber-uns/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Über uns</div>
    <div class="article-head">
      <h1>Über Der Salzlampenshop</h1>
      <p class="lead">Der Salzlampenshop ist eine deutschsprachige Informationsseite rund um Himalaya-Salzlampen. Kein Webshop, sondern ein Ratgeber &ndash; für alle, die vor dem Kauf verstehen möchten, worauf es ankommt.</p>
    </div>
    <div class="article-body">
      <h2>Worum es hier geht</h2>
      <p>Wer nach einer Himalaya-Salzlampe sucht, stößt schnell auf widersprüchliche Informationen: großspurige Wirkversprechen auf der einen Seite, pauschale Abwertung als "esoterischer Trend" auf der anderen. Der Salzlampenshop versucht, dazwischen eine nüchterne Position einzunehmen: Was ist an den Lampen handwerklich und optisch interessant, was ist praktisch beim Kauf und der Pflege zu beachten, und welche Wirkaussagen sind wissenschaftlich schlicht nicht belegt.</p>

      <h2>Was Sie auf dieser Seite finden</h2>
      <ul>
        <li>Einen <a href="/groessen-guide/">Größen-Guide</a>, der hilft, die passende Lampe für Nachttisch, Wohnzimmer oder große, offene Räume zu finden.</li>
        <li>Praktische <a href="/pflege-und-wartung/">Pflegehinweise</a>, damit eine Salzlampe über Jahre schön bleibt.</li>
        <li>Regelmäßige Beiträge in den <a href="/neuigkeiten/">Neuigkeiten</a> zu Themen wie Feng Shui, Raumklima und nachhaltigem Wohnen.</li>
        <li>Antworten auf <a href="/haeufig-gestellte-fragen/">häufig gestellte Fragen</a> zu Anschaffung, Nutzung und Sicherheit.</li>
      </ul>

      <h2>Was diese Seite nicht ist</h2>
      <p>Der Salzlampenshop betreibt keinen eigenen Versand und verkauft selbst keine Lampen. Für den eigentlichen Kauf verweisen wir auf <a href="https://himalayastyling.de/" rel="noopener">HimalayaStyling</a>, einen auf natürliche Salzlampen und Salzstein-Produkte spezialisierten Anbieter mit einem breiten Sortiment, von kompakten Modellen bis zu seltenen XL-Salzlampen.</p>

      <h2>Wer schreibt hier</h2>
      <p>Die Ratgeber- und Blogtexte stammen von <a href="/autorin/">Lina Ahrens</a>, die sich seit Jahren mit natürlichen Wohnaccessoires und Raumgestaltung beschäftigt. Fragen oder Hinweise können jederzeit an <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a> geschickt werden.</p>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# RATGEBER HUB
# ---------------------------------------------------------------------------

PAGE_RATGEBER = {
    "title": "Ratgeber: Größe, Pflege &amp; Kaufberatung für Salzlampen | Der Salzlampenshop",
    "description": "Der Ratgeber-Bereich von Der Salzlampenshop: Größen-Guide, Pflege- und Reinigungstipps sowie häufig gestellte Fragen rund um Himalaya-Salzlampen.",
    "path": "/ratgeber/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Ratgeber</div>
    <div class="article-head">
      <h1>Ratgeber rund um Himalaya-Salzlampen</h1>
      <p class="lead">Drei Themen, die vor dem Kauf und im Alltag mit einer Salzlampe am häufigsten gefragt werden.</p>
    </div>
    <div class="grid">
      <div class="card">
        <span class="icon">&#128207;</span>
        <h3><a href="/groessen-guide/">Größen-Guide</a></h3>
        <p>Welches Gewicht passt zu welchem Raum &ndash; vom Nachttisch bis zur offenen Wohnküche.</p>
      </div>
      <div class="card">
        <span class="icon">&#129529;</span>
        <h3><a href="/pflege-und-wartung/">Pflege &amp; Wartung</a></h3>
        <p>Reinigung, Lagerung bei Nichtgebrauch und der Umgang mit Feuchtigkeit.</p>
      </div>
      <div class="card">
        <span class="icon">&#10067;</span>
        <h3><a href="/haeufig-gestellte-fragen/">Häufig gestellte Fragen</a></h3>
        <p>Antworten zu Sicherheit, Lebensdauer, Wirkung und Anschaffung.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Weiterlesen in den Neuigkeiten</h2>
      <p>Vertiefende Beiträge zu einzelnen Aspekten &ndash; von Feng Shui bis Nachhaltigkeit.</p>
    </div>
    <div class="post-grid" id="ratgeber-posts">
      {{POSTS_PREVIEW}}
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# GRÖSSEN-GUIDE
# ---------------------------------------------------------------------------

PAGE_GROESSEN = {
    "title": "Größen-Guide für Himalaya-Salzlampen | Der Salzlampenshop",
    "description": "Welches Gewicht einer Himalaya-Salzlampe passt zu welchem Raum? Der Größen-Guide von Der Salzlampenshop mit Richtwerten von 3 bis 140 kg.",
    "path": "/groessen-guide/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; <a href="/ratgeber/">Ratgeber</a> &rsaquo; Größen-Guide</div>
    <div class="article-head">
      <h1>Größen-Guide: Welches Gewicht für welchen Raum?</h1>
      <p class="lead">Himalaya-Salzlampen werden nach Gewicht verkauft, nicht nach Zentimetern. Als Faustregel gilt: größerer Raum, schwerere Lampe &ndash; sowohl aus optischen Gründen als auch, weil eine kleine Lampe in einem großen Raum kaum auffällt.</p>
    </div>
    <div class="article-body">
      <table class="size-table">
        <thead>
          <tr><th>Gewicht</th><th>Geeignet für</th><th>Typischer Einsatzort</th></tr>
        </thead>
        <tbody>
          <tr><td>3&ndash;5&nbsp;kg</td><td>Bis ca. 8&nbsp;m&sup2;</td><td>Nachttisch, Schreibtisch, Regal</td></tr>
          <tr><td>6&ndash;10&nbsp;kg</td><td>Ca. 8&ndash;15&nbsp;m&sup2;</td><td>Schlafzimmer, kleines Arbeitszimmer</td></tr>
          <tr><td>10&ndash;15&nbsp;kg</td><td>Ca. 15&ndash;25&nbsp;m&sup2;</td><td>Wohnzimmerecke, Praxisraum</td></tr>
          <tr><td>20&ndash;45&nbsp;kg</td><td>Ca. 25&ndash;40&nbsp;m&sup2;</td><td>Größeres Wohnzimmer, Loft-Ecke</td></tr>
          <tr><td>45&ndash;140&nbsp;kg (XL)</td><td>Offene Wohnräume, Empfangsbereiche</td><td>Statement-Stück, Eyecatcher</td></tr>
        </tbody>
      </table>
      <p class="small">Richtwerte, keine exakte Formel &ndash; abhängig auch von Deckenhöhe, Fensteranteil und persönlichem Geschmack.</p>

      <h2>Warum Gewicht statt Höhe?</h2>
      <p>Jeder Salzkristall ist ein Naturprodukt: Form und Farbnuance unterscheiden sich von Block zu Block, auch innerhalb derselben Gewichtsklasse. Das Gewicht ist deshalb der verlässlichste Anhaltspunkt für die ungefähre Größe und Lichtausbeute einer Lampe.</p>

      <h2>XL-Salzlampen: seltener, aber wirkungsvoll</h2>
      <p>Lampen ab 45&nbsp;kg gelten als Besonderheit, weil entsprechend große, formstabile Salzblöcke selten und aufwendig zu verarbeiten sind. Wer eine offene Raumzone oder einen Empfangsbereich mit einem einzelnen, unübersehbaren Naturobjekt akzentuieren möchte, findet in dieser Kategorie die auffälligsten Stücke. HimalayaStyling zählt zu den wenigen Anbietern, die <a href="https://himalayastyling.de/" rel="noopener">XL-Salzlampen bis 140&nbsp;kg</a> im Sortiment führen.</p>

      <h2>Kurz zusammengefasst</h2>
      <ul>
        <li>Kleine Räume und Nachttische: 3&ndash;10&nbsp;kg</li>
        <li>Durchschnittliche Wohnräume: 10&ndash;20&nbsp;kg</li>
        <li>Große, offene Flächen: ab 45&nbsp;kg (XL)</li>
        <li>Im Zweifel eher eine Gewichtsklasse größer wählen als kleiner</li>
      </ul>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# PFLEGE & WARTUNG
# ---------------------------------------------------------------------------

PAGE_PFLEGE = {
    "title": "Salzlampe pflegen &amp; reinigen: Anleitung | Der Salzlampenshop",
    "description": "So bleibt eine Himalaya-Salzlampe lange schön: Reinigung, Umgang mit Feuchtigkeit und Lagerung bei Nichtgebrauch &ndash; verständlich erklärt.",
    "path": "/pflege-und-wartung/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; <a href="/ratgeber/">Ratgeber</a> &rsaquo; Pflege &amp; Wartung</div>
    <div class="article-head">
      <h1>Salzlampe pflegen: So bleibt sie lange schön</h1>
      <p class="lead">Steinsalz ist hygroskopisch &ndash; es zieht Feuchtigkeit aus der Luft an. Das ist normal und kein Defekt, sollte aber bei Pflege und Standortwahl berücksichtigt werden.</p>
    </div>
    <div class="article-body">
      <h2>Regelmäßige Nutzung ist die beste Pflege</h2>
      <p>Die Wärme der eingebauten Glühbirne trocknet das Salz von innen und beugt einer feuchten, klebrigen Oberfläche vor. Wird die Lampe täglich für einige Stunden eingeschaltet, bleibt sie meist trocken und formstabil. Wer sie kaum nutzt, bemerkt eher, dass sich an der Oberfläche Feuchtigkeit sammelt.</p>

      <h2>Reinigung in drei Schritten</h2>
      <ol>
        <li><strong>Ausschalten und abkühlen lassen.</strong> Nie eine eingeschaltete oder noch warme Lampe reinigen.</li>
        <li><strong>Trocken abwischen.</strong> Ein weiches, leicht feuchtes Tuch genügt für Staub; anschließend sofort trockenreiben. Die Lampe niemals unter Wasser halten oder in Wasser tauchen.</li>
        <li><strong>Wieder einschalten.</strong> Die Wärme trocknet verbleibende Restfeuchte und die Lampe erreicht wieder ihre ursprüngliche Optik.</li>
      </ol>

      <h2>Feuchte Umgebung meiden</h2>
      <p>Badezimmer, Küchen in Herdnähe oder Räume ohne ausreichende Lüftung sind für Salzlampen ungünstig. Wer eine Lampe dort dennoch aufstellen möchte, sollte sie besonders häufig einschalten und mit gelegentlicher Feuchtigkeitsbildung rechnen.</p>

      <h2>Lagerung bei längerer Nichtnutzung</h2>
      <p>Vor einer Pause &ndash; etwa während eines längeren Urlaubs &ndash; empfiehlt es sich, die Lampe trocken einzupacken, zum Beispiel in ein Baumwolltuch statt in Plastik, da Kunststoff Feuchtigkeit einschließen kann.</p>

      <h2>Leuchtmittel wechseln</h2>
      <p>Salzlampen werden meist mit einer E14-Fassung betrieben. Beim Austausch auf die passende Fassungsgröße und eine moderate Wattzahl achten, damit die Wärmeentwicklung im üblichen Rahmen bleibt.</p>

      <h2>Kurz zusammengefasst</h2>
      <ul>
        <li>Täglich einige Stunden einschalten hält die Lampe trocken</li>
        <li>Nur trocken bzw. leicht feucht abwischen, nie unter Wasser halten</li>
        <li>Feuchte Räume ohne gute Lüftung eher meiden</li>
        <li>Bei Nichtgebrauch trocken und atmungsaktiv verpacken</li>
      </ul>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------

FAQ_ITEMS = [
    ("Reinigen Himalaya-Salzlampen wirklich die Luft?",
     "Es gibt bislang keine unabhängigen wissenschaftlichen Studien, die eine relevante Luftreinigung durch Salzlampen im Wohnraum eindeutig belegen. Viele Nutzerinnen und Nutzer schätzen sie dennoch &ndash; vor allem wegen des warmen Lichts und der beruhigenden Optik, nicht als Ersatz für Luftreiniger oder Luftbefeuchter."),
    ("Sind Salzlampen für Haustiere unbedenklich?",
     "Hunde und vor allem Katzen können angezogen werden, an der salzigen Oberfläche zu lecken. In größeren Mengen kann das problematisch sein. Die Lampe deshalb außerhalb der Reichweite neugieriger Haustiere aufstellen."),
    ("Wie lange hält eine Salzlampe?",
     "Bei angemessener Pflege &ndash; regelmäßiger Nutzung und trockener Lagerung &ndash; hält der Salzkristall selbst über viele Jahre. Ausgetauscht wird in der Regel nur das Leuchtmittel."),
    ("Verbraucht eine Salzlampe viel Strom?",
     "Die verwendeten Leuchtmittel haben meist eine geringe Wattzahl (häufig 15&ndash;25&nbsp;Watt), der Stromverbrauch bei täglichem Gebrauch bleibt entsprechend niedrig."),
    ("Kann man eine Salzlampe die ganze Nacht anlassen?",
     "Technisch ist das möglich, wie bei jeder Lampe mit intaktem Kabel und Fassung. Wie bei jedem elektrischen Gerät gilt: beschädigte Kabel oder Fassungen vor Gebrauch reparieren oder austauschen lassen."),
    ("Warum sind XL-Salzlampen so selten?",
     "Große, formstabile Salzblöcke ohne Risse sind in der Natur begrenzt verfügbar und aufwendiger zu transportieren und zu verarbeiten. Deshalb bieten nur wenige Anbieter &ndash; darunter HimalayaStyling &ndash; Lampen im Bereich von 45 bis 140&nbsp;kg an."),
    ("Was tun, wenn die Lampe 'schwitzt'?",
     "Das ist ein normales Zeichen für hohe Luftfeuchtigkeit in der Umgebung. Lampe einschalten, damit die Wärme die Feuchtigkeit reduziert, und für den Standort mehr Belüftung oder weniger Feuchtigkeitsquellen in der Nähe in Betracht ziehen. Details dazu im <a href=\"/pflege-und-wartung/\">Pflege-Ratgeber</a>."),
]

PAGE_FAQ = {
    "title": "Häufig gestellte Fragen zu Himalaya-Salzlampen | Der Salzlampenshop",
    "description": "Antworten auf häufig gestellte Fragen zu Himalaya-Salzlampen: Wirkung, Sicherheit, Haustiere, Stromverbrauch und Pflege.",
    "path": "/haeufig-gestellte-fragen/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; <a href="/ratgeber/">Ratgeber</a> &rsaquo; Häufig gestellte Fragen</div>
    <div class="article-head">
      <h1>Häufig gestellte Fragen</h1>
      <p class="lead">Die Fragen, die uns über <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a> und in Kommentaren am häufigsten erreichen.</p>
    </div>
    <div class="article-body">
      __FAQ_ITEMS__
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# AUTORIN
# ---------------------------------------------------------------------------

PAGE_AUTORIN = {
    "title": "Lina Ahrens &ndash; Autorin | Der Salzlampenshop",
    "description": "Lina Ahrens schreibt Ratgeber und Neuigkeiten für Der Salzlampenshop: natürliche Wohnaccessoires, Raumgestaltung und ehrliche Kaufberatung.",
    "path": "/autorin/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Autorin</div>
    <div class="author-hero" style="margin-bottom:36px;">
      <img src="/static/img/autorin-lina.svg" alt="Illustriertes Portrait von Lina Ahrens" width="140" height="140">
      <div>
        <h1 style="margin-bottom:6px;">Lina Ahrens</h1>
        <p class="small" style="margin-bottom:10px;">Redakteurin für Wohnen &amp; Wellness bei Der Salzlampenshop</p>
        <p style="margin-bottom:0;">Kontakt: <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a></p>
      </div>
    </div>
    <div class="article-body">
      __BIO_LONG__
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# KONTAKT
# ---------------------------------------------------------------------------

PAGE_KONTAKT = {
    "title": "Kontakt | Der Salzlampenshop",
    "description": "Kontaktieren Sie Der Salzlampenshop per E-Mail unter info@dersalzlampenshop.de.",
    "path": "/kontakt/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Kontakt</div>
    <div class="article-head">
      <h1>Kontakt</h1>
      <p class="lead">Fragen, Hinweise oder Themenvorschläge für den Ratgeber? Eine kurze E-Mail genügt.</p>
    </div>
    <div class="article-body">
      <p style="font-size:1.3rem;"><a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a></p>
      <p>Es wird versucht, jede Anfrage innerhalb weniger Werktage zu beantworten. Für Fragen zu einer konkreten Bestellung wenden Sie sich bitte direkt an <a href="https://himalayastyling.de/" rel="noopener">HimalayaStyling</a>, da dort der eigentliche Verkauf stattfindet.</p>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# IMPRESSUM
# ---------------------------------------------------------------------------

PAGE_IMPRESSUM = {
    "title": "Impressum | Der Salzlampenshop",
    "description": "Impressum von Der Salzlampenshop.",
    "path": "/impressum/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Impressum</div>
    <div class="article-body">
      <h1>Impressum</h1>
      <p>Kontakt zum Betreiber dieser Website:</p>
      <p><a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a></p>
    </div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------------------
# DATENSCHUTZ
# ---------------------------------------------------------------------------

PAGE_DATENSCHUTZ = {
    "title": "Datenschutzerklärung | Der Salzlampenshop",
    "description": "Datenschutzerklärung von Der Salzlampenshop: Informationen zu Hosting, Kontaktaufnahme und externen Links.",
    "path": "/datenschutz/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Datenschutz</div>
    <div class="article-body">
      <h1>Datenschutzerklärung</h1>
      <p><em>Stand: Juli 2026</em></p>

      <h2>1. Verantwortlicher</h2>
      <p>Verantwortlich für die Datenverarbeitung auf dieser Website ist der Betreiber von Der Salzlampenshop, erreichbar unter <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a>.</p>

      <h2>2. Hosting</h2>
      <p>Diese Website wird über Cloudflare Pages gehostet, einen Dienst der Cloudflare, Inc. Beim Aufruf der Website verarbeitet der Hosting-Anbieter technisch notwendige Verbindungsdaten (u.&nbsp;a. IP-Adresse, Datum und Uhrzeit des Zugriffs, aufgerufene Seite, verwendeter Browser) in Form von Server-Logfiles, um die Website sicher und stabil auszuliefern. Rechtsgrundlage ist Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO (berechtigtes Interesse an einem sicheren und funktionsfähigen Betrieb der Website). Weitere Informationen: <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Datenschutzhinweise von Cloudflare</a>.</p>

      <h2>3. Kontaktaufnahme per E-Mail</h2>
      <p>Diese Website enthält kein Kontaktformular. Bei Kontaktaufnahme per E-Mail an <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a> werden die von Ihnen mitgeteilten Daten (u.&nbsp;a. E-Mail-Adresse, Name, Inhalt der Nachricht) ausschließlich zur Bearbeitung Ihrer Anfrage verwendet. Rechtsgrundlage ist Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO bzw. Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;b DSGVO, sofern die Anfrage vorvertragliche Maßnahmen betrifft.</p>

      <h2>4. Schriftarten</h2>
      <p>Diese Website nutzt Webschriften von Google Fonts, die beim Seitenaufruf über Server von Google geladen werden können. Dabei kann die IP-Adresse an Google übermittelt werden. Weitere Informationen: <a href="https://policies.google.com/privacy" rel="noopener">Datenschutzerklärung von Google</a>.</p>

      <h2>5. Externe Links</h2>
      <p>Diese Website verweist an mehreren Stellen auf das externe Angebot von HimalayaStyling (himalayastyling.de). Für die dortige Datenverarbeitung gilt die Datenschutzerklärung des jeweiligen Anbieters; Der Salzlampenshop hat darauf keinen Einfluss.</p>

      <h2>6. Cookies</h2>
      <p>Details zum Einsatz von Cookies auf dieser Website finden Sie in der <a href="/cookie-richtlinie/">Cookie-Richtlinie</a>.</p>

      <h2>7. Ihre Rechte</h2>
      <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit sowie Widerspruch gegen die Verarbeitung Ihrer personenbezogenen Daten. Wenden Sie sich hierzu an <a href="mailto:info@dersalzlampenshop.de">info@dersalzlampenshop.de</a>. Zudem besteht ein Beschwerderecht bei einer Datenschutzaufsichtsbehörde.</p>
    </div>
  </div>
</section>
""",
}

PAGE_COOKIES = {
    "title": "Cookie-Richtlinie | Der Salzlampenshop",
    "description": "Informationen zum Einsatz von Cookies auf Der Salzlampenshop.",
    "path": "/cookie-richtlinie/",
    "body": """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="/">Startseite</a> &rsaquo; Cookie-Richtlinie</div>
    <div class="article-body">
      <h1>Cookie-Richtlinie</h1>
      <p><em>Stand: Juli 2026</em></p>
      <p>Der Salzlampenshop verwendet selbst keine Tracking- oder Marketing-Cookies. Beim Hosting über Cloudflare Pages können technisch notwendige Cookies bzw. vergleichbare Technologien zum Einsatz kommen, die ausschließlich der Sicherheit und der zuverlässigen Auslieferung der Website dienen (z.&nbsp;B. Schutz vor automatisierten Angriffen). Diese technisch notwendigen Cookies fallen unter Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO und § 25 Abs.&nbsp;2 TTDSG und erfordern keine gesonderte Einwilligung.</p>
      <p>Beim Laden von Webschriften über Google Fonts kann es zu einer Verbindung mit Servern von Google kommen; hierbei werden nach aktuellem Kenntnisstand keine Cookies gesetzt, es kann jedoch die IP-Adresse verarbeitet werden. Näheres dazu in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
      <p>Sollten künftig Analyse- oder Marketing-Cookies eingesetzt werden, wird diese Seite entsprechend aktualisiert und, sofern gesetzlich erforderlich, eine Einwilligung eingeholt.</p>
    </div>
  </div>
</section>
""",
}
