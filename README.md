# kata-devops

Kata de **DevOps y Python**: lógica de negocio pequeña, tests con **pytest**, calidad con **tox** (lint, tipos, seguridad, cobertura) e integración con **GitHub Actions** y **SonarCloud**.

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EstebanMa12_kata-devops&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EstebanMa12_kata-devops)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=EstebanMa12_kata-devops&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=EstebanMa12_kata-devops)

[![CI](https://github.com/EstebanMa12/kata-devops/actions/workflows/ci.yml/badge.svg)](https://github.com/EstebanMa12/kata-devops/actions/workflows/ci.yml)

## Requisitos

- **Python** 3.9, 3.10, 3.11 o 3.12 (alineado con CI y `pyproject.toml`).
- **pip** reciente (recomendado: `python -m pip install -U pip`).

No hay dependencias de runtime externas: solo biblioteca estándar.

## Instalación

### Entorno de desarrollo (editable + herramientas)

Desde la raíz del repositorio:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e ".[dev]"
```

Equivale a usar el fichero `requirements.txt` (apunta al proyecto editable con extras `dev`).

### Generar un wheel

Tras instalar dependencias de desarrollo (`pip install -e ".[dev]"`):

```bash
python -m build
```

Los artefactos quedan en `dist/`.

### Solo el paquete (sin herramientas de desarrollo)

```bash
pip install .
```

## Cómo ejecutar los tests

### Con tox (recomendado; igual que en CI)

```bash
pip install tox
tox              # todos los entornos definidos
tox -e py312     # solo tests con Python 3.12
tox -e lint
tox -e type
tox -e security
tox -e coverage  # genera coverage.xml y xunit.xml (p. ej. para SonarCloud)
```

### Con pytest directamente

Con el entorno activado y dependencias de desarrollo instaladas:

```bash
pytest tests/ -v
pytest tests/ --cov=src --cov-config=pyproject.toml --cov-report=term-missing
```

## CLI: generar `config.yaml`

Tras `pip install -e .` (o `pip install .`):

```bash
generate-config
```

Escribe `config.yaml` en el directorio actual con valores por defecto (ver `src/generate_config.py`).

También puedes invocar el módulo:

```bash
python -m src.generate_config
```

## Estructura del repositorio

| Ruta | Descripción |
|------|-------------|
| `src/` | Código del paquete (`dictionary`, `costs`, `concatenate`, `generate_config`). |
| `tests/` | Tests pytest. |
| `pyproject.toml` | Metadatos del proyecto, extras `dev`, entry point `generate-config`, configuración de black/ruff/mypy/pytest/coverage. |
| `tox.ini` | Entornos de automatización local y en CI. |
| `.github/workflows/ci.yml` | CI: matriz Python, lint, tipos, Bandit, cobertura, SonarCloud. |
| `sonar-project.properties` | Parámetros del análisis SonarCloud. |

## CI/CD

En cada push o PR hacia `main`, GitHub Actions ejecuta tests en varias versiones de Python, **ruff**, **black**, **mypy**, **bandit**, generación de informes de cobertura y análisis **SonarCloud** (requiere secretos configurados en el repositorio).

## Licencia

MIT (ver `pyproject.toml`).
