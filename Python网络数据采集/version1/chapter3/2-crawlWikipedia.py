from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")


'''
Main Page
<p><b><a href="/wiki/Grand_Duchess_Anastasia_Nikolaevna_of_Russia" title="Grand Duchess Anastasia Nikolaevna of Russia">Grand Duchess Anastasia Nikolaevna of Russia</a></b> (18 June 1901 – 17 July 1918) was the youngest daughter of <a href="/wiki/Nicholas_II_of_Russia" title="Nicholas II of Russia">Tsar Nicholas II</a>, the last sovereign of <a class="mw-redirect" href="/wiki/Imperial_Russia" title="Imperial Russia">Imperial Russia</a>, and his wife, <a href="/wiki/Alexandra_Feodorovna_(Alix_of_Hesse)" title="Alexandra Feodorovna (Alix of Hesse)">Tsarina Alexandra Feodorovna</a>. She was <a href="/wiki/Execution_of_the_Romanov_family" title="Execution of the Romanov family">murdered with her family</a> by members of the <a href="/wiki/Cheka" title="Cheka">Cheka</a>, the <a class="mw-redirect" href="/wiki/Bolshevik" title="Bolshevik">Bolshevik</a> secret police. The location of her burial was unknown during the decades of Communist rule, and rumors that she had escaped circulated after her death. A mass grave near <a href="/wiki/Yekaterinburg" title="Yekaterinburg">Yekaterinburg</a> which held the remains of the Tsar, his wife, and three of their daughters was revealed in 1991, and the bodies of the remaining daughter and the <a href="/wiki/Alexei_Nikolaevich,_Tsarevich_of_Russia" title="Alexei Nikolaevich, Tsarevich of Russia">Tsarevitch Alexei</a> were discovered in 2007. Forensic analysis and DNA testing have confirmed that the remains are those of the <a href="/wiki/House_of_Romanov" title="House of Romanov">imperial family</a>, showing that Anastasia and the other grand duchesses were killed in 1918. Several women have claimed to be Anastasia, including <a href="/wiki/Anna_Anderson" title="Anna Anderson">Anna Anderson</a>, who died in 1984, but DNA testing in 1994 showed that she was not related to the Romanov family. (<a href="/wiki/Grand_Duchess_Anastasia_Nikolaevna_of_Russia" title="Grand Duchess Anastasia Nikolaevna of Russia"><b>Full article...</b></a>)
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia
Wikipedia
<p class="mw-empty-elt">
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Protection_policy#semi
Wikipedia:Protection policy
<p class="mw-empty-elt">
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Requests_for_page_protection
Wikipedia:Requests for page protection
<p>This page is for requesting that a page, file or template be <b> fully protected</b>, <b>create protected</b> (<a href="/wiki/Wikipedia:Protection_policy#Creation_protection" title="Wikipedia:Protection policy">salted</a>), <b>extended confirmed protected</b>, <b>semi-protected</b>, added to <b>pending changes</b>, <b>move-protected</b>, <b>template protected</b> (template-specific), <b>upload protected</b> (file-specific), or <b>unprotected</b>. Please read up on the <a href="/wiki/Wikipedia:Protection_policy" title="Wikipedia:Protection policy">protection policy</a>. Full protection is used to stop edit warring between multiple users or to prevent vandalism to <a href="/wiki/Wikipedia:High-risk_templates" title="Wikipedia:High-risk templates">high-risk templates</a>; semi-protection and pending changes are usually used only to prevent IP and new user vandalism (see the <a href="/wiki/Wikipedia:Rough_guide_to_semi-protection" title="Wikipedia:Rough guide to semi-protection">rough guide to semi-protection</a>); and move protection is used to stop <a href="/wiki/Wikipedia:Moving_a_page" title="Wikipedia:Moving a page">pagemove</a> revert wars. Extended confirmed protection is used where semi-protection has proved insufficient (see the <a href="/wiki/Wikipedia:Rough_guide_to_extended_confirmed_protection" title="Wikipedia:Rough guide to extended confirmed protection">rough guide to extended confirmed protection</a>)
</p>
/w/index.php?title=Wikipedia:Requests_for_page_protection&action=edit
----------------
/wiki/Wikipedia:Requests_for_permissions
Wikipedia:Requests for permissions
<p><span class="sysop-show" id="coordinates"><a href="/wiki/Wikipedia:Requests_for_permissions/Administrator_instructions" title="Wikipedia:Requests for permissions/Administrator instructions">Administrator instructions</a></span>
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Requesting_copyright_permission
Wikipedia:Requesting copyright permission
<p>To use copyrighted material on Wikipedia, it is <i>not enough</i> that we have permission to use it on Wikipedia alone. That's because Wikipedia itself states all its material may be used by anyone, for any purpose. So we have to be sure all material is in fact licensed for that purpose, whoever provided it.
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:User_access_levels
Wikipedia:User access levels
<p class="mw-empty-elt">
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Requests_for_adminship
Wikipedia:Requests for adminship
<p class="mw-empty-elt">
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Protection_policy#extended
Wikipedia:Protection policy
<p class="mw-empty-elt">
</p>
This page is missing something! No worries though!
----------------
/wiki/Wikipedia:Lists_of_protected_pages
'''