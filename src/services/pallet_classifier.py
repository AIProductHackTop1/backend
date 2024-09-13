from enum import Enum

import numpy as np
from ultralytics import YOLO

from src.pydantic_models.settings import ClassifierSettings


class ClassificationResult(Enum):
    HEALTHY = 0     # noqa: WPS115
    UNHEALTHY = 1   # noqa: WPS115


class PalletClassifier(object):
    def __init__(self, config: dict):
        self.config = ClassifierSettings(**config)
        self.model = YOLO(self.config.weights_path)

    def classify(self, image: np.ndarray) -> ClassificationResult:
        """
        Classifies a pallet based on the provided image.

        Args:
            image (np.ndarray): the image of the pallet to be classified.

        Returns:
            ClassificationResult: the classification result of the pallet.
        """
        detections = self.model.predict(image, conf=self.config.detection_threshold)

        pred_cls = detections[0].boxes.cls

        cls_ids, cls_counts = pred_cls.unique(return_counts=True)

        if len(cls_ids) != 0:
            for cls_id, cls_count in zip(cls_ids, cls_counts):
                if cls_count >= self.config.cls_critical_det[int(cls_id.item())]:
                    return ClassificationResult.UNHEALTHY

        return ClassificationResult.HEALTHY
