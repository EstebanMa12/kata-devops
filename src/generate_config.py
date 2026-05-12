import json
import math
from collections.abc import Iterable
from typing import Any, Optional, cast


def _ensure_str(value: object, default: str) -> str:
    if isinstance(value, str):
        return value
    if value is None:
        return default
    return str(value)


def _sanitize_tax_rate(tax_rate: object, default: float = 0.09) -> float:
    try:
        tr = float(cast(Any, tax_rate))
    except (TypeError, ValueError):
        return default
    if not math.isfinite(tr):
        return default
    return tr


def _normalize_endpoints(endpoints: object) -> list[str]:
    if endpoints is None:
        return ["dictionary", "costs", "concatenate"]
    if isinstance(endpoints, (str, bytes)) or not isinstance(endpoints, Iterable):
        return ["dictionary", "costs", "concatenate"]
    out: list[str] = []
    for ep in endpoints:
        out.append(str(ep))
    return out if out else ["dictionary", "costs", "concatenate"]


def _validate_output_path(output_path: object) -> str:
    if not isinstance(output_path, str) or not output_path.strip():
        raise ValueError("output_path must be a non-empty string")
    if "\x00" in output_path:
        raise ValueError("output_path must not contain null bytes")
    return output_path


def generate_config(
    app_name: str = "kata-devops",
    version: str = "1.0.0",
    environment: str = "dev",
    debug: bool = True,
    endpoints: Optional[list] = None,
    tax_rate: float = 0.09,
    output_path: str = "config.yaml",
) -> None:
    app_name_s = _ensure_str(app_name, "kata-devops")
    version_s = _ensure_str(version, "1.0.0")
    environment_s = _ensure_str(environment, "dev")
    debug_b = debug if isinstance(debug, bool) else bool(debug)
    endpoints_list = _normalize_endpoints(endpoints)
    tax = _sanitize_tax_rate(tax_rate, default=0.09)
    out = _validate_output_path(output_path)

    def yaml_double_quoted(s: str) -> str:
        return json.dumps(s, ensure_ascii=False)

    lines = [
        "# Configuración generada automáticamente",
        "app:",
        f"  name: {yaml_double_quoted(app_name_s)}",
        f"  version: {yaml_double_quoted(version_s)}",
        f"  environment: {yaml_double_quoted(environment_s)}",
        f"  debug: {str(debug_b).lower()}",
        "  endpoints:",
    ]
    for ep in endpoints_list:
        lines.append(f"    - {yaml_double_quoted(ep)}")
    lines.append("  tax:")
    lines.append(f"    default_rate: {tax}")

    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> None:
    """CLI: ejecutable ``generate-config`` o ``python -m src.generate_config``."""
    generate_config()


if __name__ == "__main__":
    main()
