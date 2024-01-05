"""
This file is used to collect all websites used in this program.
"""
import json


class SiteInformation:

    def __init__(self, name, url, module, information):
        self.name = name
        self.url = url
        self.module = module
        self.information = information
        return

    def __str__(self):
        return f"{self.name} ({self.url})"


class SitesInformation:

    def __init__(self, data_file_path=None):
        if not data_file_path:
            # use my GitHub addr afterward.
            data_file_path = ""

        else:
            try:
                with open(data_file_path, "r", encoding="utf-8") as file:
                    try:
                        site_data = json.load(file)
                    except Exception as error:
                        raise ValueError(
                            f"Problem parsing json contents at '{data_file_path}':  {error}."
                        )
            except FileNotFoundError:
                raise FileNotFoundError(f"Problem while attempting to access "
                                        f"data file '{data_file_path}'."
                                        )
        self.sites = {}

        # add all site information
        for site_name in site_data:
            try:

                self.sites[site_name] = \
                    SiteInformation(site_name,
                                    site_data[site_name]["url"],
                                    site_data[site_name]["module"],
                                    site_data[site_name]["info"]
                                    )
            except KeyError as error:
                raise ValueError(
                    f"Problem parsing json contents at '{data_file_path}':  Missing attribute {error}."
                )

        return

    def site_name_list(self):
        return sorted([site.name for site in self], key=str.lower)

    def __iter__(self):
        for site_name in self.sites:
            yield self.sites[site_name]

    def __len__(self):
        return len(self.sites)