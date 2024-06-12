import yaml

# Read the program.yaml file and Generate the pages based on the program.yaml file
def generatePages():
    webpage = ""
    with open('program.yaml') as file:
        program = yaml.load(file, Loader=yaml.FullLoader)
        for day in program['days']:
            webpage += "<div style='width:100%; display:inline-block; overflow-wrap: break-word;'><div><div style='display:inline-block; width:100%;'><center><h1>" + day['day'] + "</h1></center></div><div>\n"
            webpage += "<div style='width:100%; display:inline-block; overflow-wrap: break-word;'><div><div style='display:inline-block; width:100%;'><center><h3>" + day['room'] + "</h3></center></div><div>\n"
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