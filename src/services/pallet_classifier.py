from enum import Enum

import numpy as np
from src.pydantic_models.settings import ClassifierSettings


class ClassificationResult(Enum):
    HEALTHY = 0     # noqa: WPS115
    UNHEALTHY = 1   # noqa: WPS115


class PalletClassifier(object):
    def __init__(self, config: ClassifierSettings):
        self.config = config

    def classify(self, image: np.ndarray) -> ClassificationResult:
        """
        Classifies a pallet based on the provided image.

        Args:
            image (np.ndarray): the image of the pallet to be classified.

        Returns:
            ClassificationResult: the classification result of the pallet.
        """
        return ClassificationResult.HEALTHY
