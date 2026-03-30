from typing import Dict, Type

from ..base import BaseFactoryModule, ModuleEngine
from .base_generator import GeneratorName
from .gemini import GeminiGeneratorEngine
from .qwen import QwenGeneratorEngine


class AutoGeneratorModule(BaseFactoryModule):
    @property
    def _module_mapping(self) -> Dict[GeneratorName, Type[ModuleEngine]]:
        return {
            GeneratorName.Gemini: GeminiGeneratorEngine,
            GeneratorName.Qwen: QwenGeneratorEngine,
        }
