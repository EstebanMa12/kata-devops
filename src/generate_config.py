import json
from typing import Optional


def generate_config(
    app_name: str = "kata-devops",
    version: str = "1.0.0",
    environment: str = "dev",
    debug: bool = True,
    endpoints: Optional[list] = None,
    tax_rate: float = 0.09,
    output_path: str = "config.yaml",
) -> None:
    if endpoints is None:
        endpoints = ["dictionary", "costs", "concatenate"]

    def yaml_double_quoted(s: str) -> str:
        return json.dumps(s, ensure_ascii=False)

    lines = [
        "# Configuración generada automáticamente",
        "app:",
        f"  name: {yaml_double_quoted(app_name)}",
        f"  version: {yaml_double_quoted(version)}",
        f"  environment: {yaml_double_quoted(environment)}",
        f"  debug: {str(debug).lower()}",
        "  endpoints:",
    ]
    for ep in endpoints:
        lines.append(f"    - {yaml_double_quoted(str(ep))}")
    lines.append("  tax:")
    lines.append(f"    default_rate: {tax_rate}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    generate_config()
