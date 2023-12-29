import os
import re
import requests
import json
import pandas as pd

## GOOGLE FONTS API KEY
GOOGLE_FONTS_API_KEY = "AIzaSyAoR3wuiZCbhCCNCJBHE0RRkvtlOu3HYO4"
GOOGLE_FONTS_API_URL = (
    f"https://www.googleapis.com/webfonts/v1/webfonts?key={GOOGLE_FONTS_API_KEY}"
)

directory_path = "./48px/compressed"

# Specify the output file path
output_file_path = "./fonts-json.txt"

if __name__ == "__main__":

    def split_camel_case(s):
        # Use a regular expression to split CamelCase string
        parts = re.findall(r"[A-Z][a-z0-9]*", s)
        return parts

    # Check if the directory exists
    if os.path.exists(directory_path):
        output_json_arr = []
        used_font_names = []
        # Get the list of files in the directory
        file_names = os.listdir(directory_path)
        response = requests.get(GOOGLE_FONTS_API_URL)

        # Parse the response content (JSON, XML, etc.)
        data = response.json()  # Assuming the response is in JSON format
        all_google_fonts = data["items"]

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            for file_name in file_names:
                parts = file_name.split("-")
                font_name_camel_case = parts[0]
                font_name_arr = split_camel_case(font_name_camel_case)

                real_font_name = "+".join(font_name_arr)
                font_name_with_space = " ".join(font_name_arr)

                ## If any variant has been fetched so far, we are moving ahead
                if real_font_name in used_font_names:
                    continue

                curr_google_font = next(
                    (
                        item
                        for item in all_google_fonts
                        if item.get("family") == font_name_with_space
                    ),
                    None,
                )
                if curr_google_font == None:
                    continue

                def map_variants(n: str):
                    if (
                        n == "100"
                        or n == "200"
                        or n == "300"
                        or n == "400"
                        or n == "500"
                        or n == "600"
                        or n == "700"
                        or n == "800"
                        or n == "900"
                        or n == "regular"
                    ):
                        return n if n != "regular" else "400"
                    return None

                mapped_variants = [
                    map_variants(x) for x in curr_google_font["variants"]
                ]
                filteredVariants = [
                    item for item in mapped_variants if item is not None
                ]
                # for google_font_item in all_items:
                optimized_dict = {
                    "family": curr_google_font["family"],
                    "category": curr_google_font["category"],
                    "variants": filteredVariants,
                    "img_url": f"https://raw.githubusercontent.com/berkorg/GoogleWebFonts-FontFamilyPreviewImages/master/48px/compressed/{file_name}",
                }
                output_json_arr.append(optimized_dict)
                used_font_names.append(real_font_name)
                # print(optimized_dict)
        else:
            # Print an error message if the request was not successful
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        df = pd.DataFrame(output_json_arr)

        distinct_category_values = df["category"].unique()

        print(distinct_category_values)
        # Open the file in write mode ('w')
        with open(output_file_path, "w") as file:
            # Serialize the array of dictionaries and write it to the file
            json.dump(output_json_arr, file, indent=2)

    else:
        print(f"The directory '{directory_path}' does not exist.")
