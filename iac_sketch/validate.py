import pandas as pd


class ValidationSystem:

    def validate_requirements(self, components: dict[pd.DataFrame]) -> pd.DataFrame:

        reqs = components["requirement"]
        invalid_reqs = reqs[~reqs["is_satisfied"]]

        return invalid_reqs
