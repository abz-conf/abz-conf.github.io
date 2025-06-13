import requests
from pyquery import PyQuery as pq
import json
import os
import time


def process_conference(conference):
    # Create the content directory if it doesn't exist
    content_dir = f"content/publication/{root_data[conference]['subdirectory']}"
    if not os.path.exists(content_dir):
        os.makedirs(content_dir)
    # Fetch the JSON data
    print(f"Fetching JSON data for {conference}...")
    json_data = fetch_json_data(root_data[conference]["url"])
    # Parse the JSON data
    data = json.loads(json_data)
    publication = root_data[conference]["publication"]
    publication_short = root_data[conference]["publication_short"]
    subdirectory = root_data[conference]["subdirectory"]
    # Create the content directory if it doesn't exist
    # Adjust the slice to get more entries if needed
    for entry in data["result"]["hits"]["hit"][0:-1]:
        # Extract the necessary information from each entry
        print(f"    Processing entry: {entry['info']['key']}")
        (key, title, authors, year, links) = extract_and_format_data(
            entry["info"], root_data[conference]["dblp_path"])

        print(f"         Enhancing data...")
        (abstract, bibtex) = enhance_data(
            key, "DBLP:"+root_data[conference]["dblp_path"], links)
        print(f"         Formatting data...")
        yaml_content = format_yaml(subdirectory, title, authors, year,
                                   publication, publication_short, links, abstract, bibtex)
        # Write the formatted content to a file
        print(f"         Writing to file...")
        filename = f"content/publication/{subdirectory}/{key.lower()}.md"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(yaml_content)




def fetch_json_data(url):
    """
    Fetch JSON data from the given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")



def extract_and_format_data(data, dblp_path):
    """
    Extract and format the necessary information from the JSON data.
    """
    # Extract the necessary information
    title = data["title"][0:-1] # remove the trailing period
    if isinstance(data["authors"]["author"],list): 
        authors = [author["text"] for author in data["authors"]["author"]]
    else:
        authors = [data["authors"]["author"]["text"]]
    year = data["year"]
    key = data["key"].replace(dblp_path, "")
    key_lower = key.lower()
    
    links = [
        {"name": "Digital", "url": f"https://link.springer.com/content/pdf/{data['doi'].replace('/', '%2F')}.pdf", "icon_pack": "fas", "icon": "file-pdf"},
        {"name": "Printed", "url": data["ee"], "icon_pack": "fas", "icon": "book"},
        {"name": "Abstract", "url": f"publication/{key_lower}/#abstract", "icon_pack": "fas", "icon": "file-alt"},
        {"name": "View", "url": f"publication/{key_lower}/#document", "icon_pack": "fas", "icon": "glasses"},
        {"name": "Cite", "url": f"publication/{key_lower}/#reference", "icon_pack": "fas", "icon": "quote-right"},
        {"name": "Source", "url": f"publication/{key_lower}/#sources", "icon_pack": "fas", "icon": "database"} # last entry will be handled separately
    ]

    # Format the extracted information
    return (key, title, authors, year, links)



def enhance_data(key, dblp_prefix, links):
    # get additional data from the links
    abstract_url = links[1]["url"]
    response = requests.get(abstract_url)

    if response.status_code == 200:
        doc = pq(response.text)
        abstract = doc("#Abs1-content").find("p").text()
    else:
        raise Exception(f"Failed to fetch abstract from {abstract_url}, status code: {response.status_code}")

    bibtex_url = f"https://dblp.org/rec/{root_data[conference]["dblp_path"]}{key}.bib?param=1"
    response = requests.get(bibtex_url)
    if response.status_code == 200:
        bibtex = response.text
    else:
        raise Exception(f"Failed to fetch BibTeX from {bibtex_url}, status code: {response.status_code}")
    bibtex = bibtex.replace(dblp_prefix, "")  # Shorten the BibTeX key
    # Return the abstract and bibtex
    return (abstract, bibtex)




def format_yaml(case_study, title, authors, year, publication, publication_short, links, abstract, bibtex):
    # Format the extracted information into the desired YAML-like format
    yaml_content = f"""---
title: "{title}"

authors:
{"".join(f"  - {author}\n" for author in authors)}

date: {year}-01-01

# Legend (see /data/publication_types.yaml and e.g. i18n/en.yaml): 
#   0 = "pub_uncat"
#   1 = "pub_conf"
#   2 = "pub_journal"
#   3 = "pub_preprint"
#   4 = "pub_report"
#   5 = "pub_book"
#   6 = "pub_book_section"
#   7 = "pub_thesis"
#   8 = "pub_patent"
#   9 = "pub_case_study_descr"
#  10 = "pub_case_study_contrib"
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
#  14 = "pub_phd_symposium"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

publication: "{publication}"
publication_short: "{publication_short}"

tags:
  - {publication_short}

categories: []

featured: false

# enable this for case studies
# projects:
#   - {case_study}

links:
{"".join(f"  - name: {link['name']}\n    url: {link['url']}\n    icon_pack: {link['icon_pack']}\n    icon: {link['icon']}\n" for link in links[0:-1])}
{"".join(f"#   - name: {links[-1]['name']}\n#     url: {links[-1]['url']}\n#     icon_pack: {links[-1]['icon_pack']}\n#     icon: {links[-1]['icon']}\n")}

---

## Abstract

{abstract}

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="{links[0]["url"]}">link</a>.

{{{{< embed-pdf url="{links[0]["url"]}" >}}}}

## Reference

```
% BibTex
{bibtex}
```

<!-- # add information for case study papers (if available)
## Sources

- **Used formal method:**
  [ASM](/method/asm)
- **Resources and tools:**
  Asmeta

For more information, please contact the <a href ="mailto:silvia.bonfanti@unibg.it;arcaini@nii.ac.jp;angelo.gargantini@unibg.it;scandurra@unibg.it;elvinia.riccobene@unimi.it">authors</a>-->

"""

    return yaml_content



root_data = {
              'abz08':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2008.bht%3A&h=1000&format=json",
                    "publication": "1st International Conference on ASM, B, and Z (ABZ'08)",
                    "publication_short": "ABZ'08",
                    "subdirectory": "abz08",
                    "dblp_path": "conf/asm/"
                },
              'abz10':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2010.bht%3A&h=1000&format=json",
                    "publication": "2nd International Conference on ASM, Alloy, B, and Z (ABZ'10)",
                    "publication_short": "ABZ'10",
                    "subdirectory": "abz10",
                    "dblp_path": "conf/asm/" 
                },
              'abz12':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2012.bht%3A&h=1000&format=json",
                    "publication": "3rd International Conference on ASM, Alloy, B, VDM, and Z (ABZ'12)",
                    "publication_short": "ABZ'12",
                    "subdirectory": "abz12",
                    "dblp_path": "conf/asm/" 
                },
              'abz14': 
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2014.bht%3A&h=1000&format=json",
                    "publication": "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)",
                    "publication_short": "ABZ'14",
                    "subdirectory": "abz14",
                    "dblp_path": "conf/asm/"
                },
             'abz16':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2016.bht%3A&h=1000&format=json",
                    "publication": "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)",
                    "publication_short": "ABZ'16",
                    "subdirectory": "abz16",
                    "dblp_path": "conf/asm/"
                }, 
             'abz18':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2018.bht%3A&h=1000&format=json",
                    "publication": "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)",
                    "publication_short": "ABZ'18",
                    "subdirectory": "abz18",
                    "dblp_path": "conf/asm/" 
                },   
             'abz20': 
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2020.bht%3A&h=1000&format=json",
                    "publication": "7th International Conference on Rigorous State Based Methods (ABZ'20)",
                    "publication_short": "ABZ'20",
                    "subdirectory": "abz20",
                    "dblp_path": "conf/asm/"
                },
             'abz21':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/asm/abz2021.bht%3A&h=1000&format=json",
                    "publication": "8th International Conference on Rigorous State Based Methods (ABZ'21)",
                    "publication_short": "ABZ'21",
                    "subdirectory": "abz21",
                    "dblp_path": "conf/asm/"
                },
             'abz23':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/zum/abz2023.bht%3A&h=1000&format=json",
                    "publication": "9th International Conference on Rigorous State Based Methods (ABZ'23)",
                    "publication_short": "ABZ'23",
                    "subdirectory": "abz23",
                    "dblp_path": "conf/zum/"
                },
             'abz24':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/zum/abz2024.bht%3A&h=1000&format=json",
                    "publication": "10th International Conference on Rigorous State Based Methods (ABZ'24)",
                    "publication_short": "ABZ'24",
                    "subdirectory": "abz24",
                    "dblp_path": "conf/zum/"
                },
              'abz25':
                { "url": "https://dblp.org/search/publ/api?q=toc%3Adb/conf/zum/abz2025.bht%3A&h=1000&format=json",
                    "publication": "11th International Conference on Rigorous State Based Methods (ABZ'25)",
                    "publication_short": "ABZ'25",
                    "subdirectory": "abz25",
                    "dblp_path": "conf/zum/"
                }
            }


conferences = list(root_data.keys())  # Get all conference keys
# Specify the subset of conferences to process
conferences = ['abz10', 'abz12', 'abz14', 'abz16', 'abz18', 'abz20', 'abz21', 'abz23']    

for conference in conferences:  # List all available conferences
    print(f"Processing conference: {conference}")
    process_conference(conference)  # Call the function to process the conference data
    time.sleep(10)  # Sleep for 10 seconds to avoid overwhelming the server
print("All conferences processed successfully.")