"""Module for generating documentation from infrastructure-as-code manifests.
"""

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