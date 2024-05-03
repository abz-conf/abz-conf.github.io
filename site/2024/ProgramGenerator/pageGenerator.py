import yaml

# Read the program.yaml file and Generate the pages based on the program.yaml file
def generatePages():
    webpage = ""
    with open('program.yaml') as file:
        program = yaml.load(file, Loader=yaml.FullLoader)
        for day in program['days']:
#            webpage += "<table style='width:100%; table-layout: fixed; overflow-wrap: break-word;'><tr><th colspan=3><center><h1>" + day['day'] + "</h1></center></th><tr>\n"
#            webpage += "<tr><th style='width:15%; table-layout: fixed;'><b>Time</b></th><th><b>Talk</b></th><th style='width:10%; table-layout: fixed;'><b>Topic</b></th></tr>\n"
#            for papers in day['program']:
#                if "start" in papers and "end" in papers:
#                    time = str(papers['start']) + " - " + str(papers['end'])                
#                    if "abstract" in papers:
#                        webpage += "<tr class='specific'" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td style='width:15%; table-layout: fixed; overflow-wrap: break-word;'>" + time + "</td><td><details><summary><b>" + papers['paper'] + "</b></summary>" + papers['abstract'] + "</details>" + ("<i>" + str(papers['author']) + "<i>" if "author" in papers else "") + "</td><td style='width:10%; table-layout: fixed;'>" + (papers['topic'] if "topic" in papers else "") + "</td></tr>\n"    
#                    else:
#                        webpage += "<tr class='specific'" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td style='width:15%; table-layout: fixed; overflow-wrap: break-word;'>" + time + "</td><td><b>" + papers['paper'] + "</b>" + ("<br><i>" + str(papers['author']) + "<i>" if "author" in papers else "") + "</td><td style='width:10%; table-layout: fixed;'>" + (papers['topic'] if "topic" in papers else "") + "</td></tr>\n"    
#                else:
#                    time = ""
#                    webpage += "<tr class='specific'" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td colspan=3><b>" + papers['paper'] + "</b></td></tr>\n"    
#            webpage += "</table><br>\n"
            
            webpage += "<div style='width:100%; display:inline-block; overflow-wrap: break-word;'><div><div style='display:inline-block; width:100%;'><center><h1>" + day['day'] + "</h1></center></div><div>\n"
            webpage += "<div style='border-bottom: 0.2ex solid gray;'><div style='width:15%; display:inline-block;'><b>Time</b></div><div style='display:inline-block; width:75%;'><b>Talk</b></div><div style='width:10%; display:inline-block;'><b>Topic</b></div></div>\n"
            for papers in day['program']:
                if "start" in papers and "end" in papers:
                    time = str(papers['start']) + " - " + str(papers['end'])                
                    if "abstract" in papers:
                        webpage += "<div style='border-bottom: 0.2ex solid gray;" + (" background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "'><div style='width:15%; display:inline-block; overflow-wrap: break-word;'>" + time + "</div><div style='display:inline-block; width:75%;'><details><summary><b>" + papers['paper'] + "</b></summary>" + papers['abstract'] + "</details>" + ("<i>" + str(papers['author']) + "</i>" if "author" in papers else "") + "</div><div style='width:10%; display:inline-block;'>" + (papers['topic'] if "topic" in papers else "") + "</div></div>\n"    
                    else:
                        webpage += "<div style='border-bottom: 0.2ex solid gray;" + (" background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "'><div style='width:15%; display:inline-block; overflow-wrap: break-word;'>" + time + "</div><div style='display:inline-block; width:75%; '><b>" + papers['paper'] + "</b>" + ("<br><i>" + str(papers['author']) + "<i>" if "author" in papers else "") + "</div><div style='width:10%; display:inline-block;'>" + (papers['topic'] if "topic" in papers else "") + "</div></div>\n"    
                else:
                    time = ""
                    webpage += "<div style='border-bottom: 0.2ex solid gray;" + (" background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "'><div style='display:inline-block; width:75%;'><b>" + papers['paper'] + "</b></div></div>\n"    
            webpage += "</div><br>\n"
    # Write the webpage string into the page.html file
    with open('page.html', 'w') as file:
        file.write(webpage)

if __name__ == '__main__':
    generatePages()