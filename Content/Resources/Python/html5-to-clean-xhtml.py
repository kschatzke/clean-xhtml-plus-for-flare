# Convert HTML5 Features to Clean XHTML Plus
# Version 1.0 - July 16, 2025
# (C) 2025 Ken Schatzke

# Import pre-installed modules
import os
import random
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("html5_to_clean_xhtml")

# Import Beautiful Soup or log an error if it doesn't already exist
try:
    from bs4 import BeautifulSoup
except:
    logger.error("The Beautiful Soup and/or LXML packages are not installed. To install them, open a command prompt and enter pip install beautifulsoup4 lxml.")

# Set the location of the source files
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
directory = os.path.dirname(parent_directory)

# Set file extensions for images
extension = ".htm"

for root, dirs, filenames in os.walk(directory, topdown=True):
    for filename in filenames:
        if filename.endswith(".htm"):
            file_path = os.path.join(root, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                xml_content = file.read()
            
            soup = BeautifulSoup(xml_content, "xml")

            # Convert text popups
            for old_tag in soup.find_all("MadCap:popupHead"):
                children = old_tag.contents
                for child in children:
                    old_tag.insert_before(child)
                old_tag.decompose()

            for old_tag in soup.find_all("MadCap:popupBody"):
                new_tag = soup.new_tag("span", **old_tag.attrs)

                for child in old_tag.contents:
                    new_tag.append(child)

                if not new_tag.has_attr("class"):
                    new_tag["class"] = "cxp-text-popup-content"
                else:
                    new_tag["class"] += " cxp-text-popup-content"

                old_tag.replace_with(new_tag)

            for old_tag in soup.find_all("MadCap:popup"):
                new_tag = soup.new_tag("a", **old_tag.attrs)

                for child in old_tag.contents:
                    new_tag.append(child)

                for child in old_tag.contents:
                    new_tag.append(child)
            
                new_tag["href"] = "#"

                if not new_tag.has_attr("class"):
                    new_tag["class"] = "cxp-text-popup"
                else:
                    new_tag["class"] += " cxp-text-popup"

                old_tag.replace_with(new_tag)

            # Convert topic popups
            body_tag = soup.find("body")

            for tag in soup.find_all("a"):
                if tag.has_attr("target") and tag["target"] == "_popup":
                    popup_href = tag["href"]
                    popup_id = random.randint(1, 1000000)

                    tag["href"] = "#"
                    tag["data-cxp-topic-popup-link"] = popup_id
                    del tag["target"]

                    popup_iframe = soup.new_tag("iframe")
                    popup_iframe["src"] = popup_href

                    popup_dialog = soup.new_tag("dialog")
                    popup_dialog["data-cxp-topic-popup"] = popup_id
                    popup_dialog.append(popup_iframe)

                    body_tag.append(popup_dialog)

            # Convert togglers
            for old_tag in soup.find_all("MadCap:toggler"):
                new_tag = soup.new_tag("a", **old_tag.attrs)

                for child in old_tag.contents:
                    new_tag.append(child)
                
                new_tag["href"] = "#"

                new_tag["data-cxp-toggler-link"] = new_tag["targets"]
                del new_tag["targets"]

                old_tag.replace_with(new_tag)

            for tag in soup.find_all(True):
                if tag.has_attr("MadCap:targetName"):
                    tag["data-cxp-toggler"] = tag["MadCap:targetName"]
                    del tag["MadCap:targetName"]
            
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(str(soup))