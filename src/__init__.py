"""Paquete de la kata DevOps (módulos de dominio y utilidades)."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("kata-devops")
except PackageNotFoundError:
    __version__ = "0.0.0"  # editable sin instalar metadatos
