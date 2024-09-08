from fastapi import Depends, UploadFile
from dependency_injector.wiring import Provide, inject

import cv2
import numpy as np

from src.routes.routers import router
from src.schemas.classifier_routes import ClassificationResponse

from src.containers.container import AppContainer
from src.services.pallet_classifier import PalletClassifier, ClassificationResult


@router.post('/classify')
@inject
async def classify(
    image: UploadFile,
    pallet_classifier: PalletClassifier = Depends(Provide[AppContainer.pallete_classifier]),
) -> ClassificationResponse:
    """Endpoint for pallet classification"""
    img = cv2.imdecode(np.frombuffer(await image.read(), np.uint8), cv2.IMREAD_COLOR)

    return ClassificationResponse(healthy_pallet=pallet_classifier.classify(img) == ClassificationResult.HEALTHY)
