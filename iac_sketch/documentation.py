"""Module for generating documentation from infrastructure-as-code manifests.
"""

import pandas as pd

from . import data

class DocumentationSystem:

    def generate_markdown(self, output_path: str, registry: data.Registry) -> None:
        """
        Generates markdown documentation for the infrastructure-as-code manifests.

        Parameters
        ----------
        output_path : str
            The file path where the markdown documentation will be saved.
        registry : data.Registry
            The registry containing the extracted entities.

        Returns
        -------
        None
        """

        pass

    def generate_component_markdown(self, comp: pd.Series, comp_type: str) -> str:

        output = f"**{comp_type}:**"

        # If there's a value, we put it right after the component type
        if not pd.isna(comp["value"]):
            output += f" {comp['value']}\n"
        else:
            output += "\n"

        # The other fields we list as bullet points
        skipped_fields = ["comp_key", "value"]
        for field, val in comp.items():
            if field in skipped_fields or pd.isna(val):
                continue
            output += f"- {field}: {val}\n"

        return output
