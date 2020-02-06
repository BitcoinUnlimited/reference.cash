from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class ReferenceCashPlugin(BasePlugin):

    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("code",class_="mermaid")
        for mermaid in mermaids:
            # replace code with div
            mermaid.name="div"
            # replace <pre>
            mermaid.parent.replace_with(mermaid)

        cwikmeta = soup.find_all("div", class_="cwikmeta")
        for meta in cwikmeta:
            # remove meta tags
            meta.clear()

        # cwik wants links to end with .md
        links = soup.find_all("a")
        for a in links:
            try:
                # ignore external URLs
                if a['href'].startswith("http"):
                    continue

                if a['href'].endswith(".md"):
                    a['href'] = a['href'][:-3]
            except KeyError:
                pass

        return str(soup)
