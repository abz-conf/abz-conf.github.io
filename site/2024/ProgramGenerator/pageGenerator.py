import yaml

# Read the program.yaml file and Generate the pages based on the program.yaml file
def generatePages():
    webpage = ""
    with open('program.yaml') as file:
        program = yaml.load(file, Loader=yaml.FullLoader)
        for day in program['days']:
            webpage += "<table style='width:100%; table-layout: fixed; overflow-wrap: break-word;'><tr><th colspan=3><center><h1>" + day['day'] + "</h1></center></th><tr>\n"
            webpage += "<tr><th style='width:10%; table-layout: fixed;'><b>Time</b></th><th><b>Talk</b></th><th style='width:10%; table-layout: fixed;'><b>Topic</b></th></tr>\n"
            for papers in day['program']:
                if "start" in papers and "end" in papers:
                    time = str(papers['start']) + " - " + str(papers['end'])                
                    if "abstract" in papers:
                        webpage += "<tr" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td style='width:10%; table-layout: fixed; overflow-wrap: break-word;'>" + time + "</td><td><details><summary><b>" + papers['paper'] + "</b></summary>" + papers['abstract'] + "</details></td><td style='width:10%; table-layout: fixed;'>" + (papers['topic'] if "topic" in papers else "") + "</td></tr>\n"    
                    else:
                        webpage += "<tr" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td style='width:10%; table-layout: fixed; overflow-wrap: break-word;'>" + time + "</td><td><b>" + papers['paper'] + "</b></td><td style='width:10%; table-layout: fixed;'>" + (papers['topic'] if "topic" in papers else "") + "</td></tr>\n"    
                    if ("author" in papers):
                        webpage += "<tr><td style='width:10%; table-layout: fixed;'></td><td><i>" + str(papers['author']) + "<i></td><td></td></tr>\n"
                else:
                    time = ""
                    webpage += "<tr" + (" style='background-color:" + str(papers['background']) + "'" if "background" in papers else "") + "><td colspan=3><b>" + papers['paper'] + "</b></td></tr>\n"    
            webpage += "</table><br>\n"
    # Write the webpage string into the page.html file
    with open('page.html', 'w') as file:
        file.write(webpage)

if __name__ == '__main__':
    generatePages()