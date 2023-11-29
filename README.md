# GC Data site keywords

analysis.ipynb contains the parsing script to use canada-tbs-links.json.
canada-tbs-links.json is available upon request or via Slack group.

config.py [NOT SHARED] contains the credentials for the neo4j instance either online or locally, organized:

```{python}
remote = {}
remote["uri"] = 
remote["user"] = "neo4j"
remote["password"] = ""

## For local instance, must have a neo4j instance running! ##
localhost = {}
localhost["uri"] = "bolt://localhost:7687"
localhost["user"] = "neo4j"
localhost["password"] = ""
```

keywords_all.csv contains the extracted list of all keywords [Eng / French] from the above analysis
sel_data.csv contains the parsed data in a csv (tab-delimited) format, incl:

* tstamp
* host
* url
* description_str
* title
* keywords_split

TODO:
- [ ] Create graph of all linked keywords and pages
- [ ] Push initial repo to github: @KrishnaUdaiwal
- [ ] Process keywords from contents of pages
