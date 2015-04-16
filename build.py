import codecs, pystache, markdown

with codecs.open("readme.md", encoding="utf-8") as src:
    parsed = markdown.markdown(src.read())

with codecs.open("template.html", encoding="utf-8") as templ:
    with codecs.open("build/readme.html", "w", encoding="utf-8") as dest:
        dest.write(pystache.render(templ.read(), {"content": parsed}))
