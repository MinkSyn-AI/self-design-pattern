from abc import ABC, abstractmethod
from typing import Dict, Optional, Type

from loguru import logger
from strenum import LowercaseStrEnum


class ModuleEngine(ABC):
    @classmethod
    @abstractmethod
    def build(cls, *args, **kwargs):
        pass

    def is_healthy(self) -> bool:
        return False

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class BaseFactoryModule(ABC):
    def __init__(self):
        self.engine_name: Optional[LowercaseStrEnum] = None
        self._module: Optional[ModuleEngine] = None

    @property
    @abstractmethod
    def _module_mapping(self) -> Dict[LowercaseStrEnum, Type[ModuleEngine]]: ...

    @classmethod
    def build(
        cls, engine_name: LowercaseStrEnum, *args, **kwargs
    ) -> "BaseFactoryModule":
        instance = cls()

        if engine_name not in instance._module_mapping.keys():
            raise ValueError(f"Engine {engine_name} not found in ModuleNames")

        instance.engine_name = engine_name
        module_class = instance._module_mapping.get(engine_name)

        logger.info(f"Building module with engine: {module_class.__name__}")
        instance._module = module_class.build(*args, **kwargs)

        if not instance._module.is_healthy():
            raise RuntimeError(f"The {engine_name} engine unhealthy")

        return instance

    def execute(self, *args, **kwargs):
        return self._module.execute(*args, **kwargs)
