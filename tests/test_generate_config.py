import json
import runpy
from pathlib import Path

import pytest
from src.generate_config import generate_config


class TestGenerateConfig:
    def test_writes_expected_yaml_with_defaults(self, tmp_path):
        out = tmp_path / "config.yaml"
        generate_config(output_path=str(out))

        text = out.read_text(encoding="utf-8")
        assert "# Configuración generada automáticamente" in text
        assert f'name: {json.dumps("kata-devops", ensure_ascii=False)}' in text
        assert f'version: {json.dumps("1.0.0", ensure_ascii=False)}' in text
        assert f'environment: {json.dumps("dev", ensure_ascii=False)}' in text
        assert "debug: true" in text
        for ep in ("dictionary", "costs", "concatenate"):
            assert f"- {json.dumps(ep, ensure_ascii=False)}" in text
        assert "default_rate: 0.09" in text

    def test_custom_parameters(self, tmp_path):
        out = tmp_path / "out.yaml"
        generate_config(
            app_name="my-app",
            version="2.0.0",
            environment="prod",
            debug=False,
            endpoints=["a", "b"],
            tax_rate=0.21,
            output_path=str(out),
        )
        text = out.read_text(encoding="utf-8")
        assert f'name: {json.dumps("my-app", ensure_ascii=False)}' in text
        assert "debug: false" in text
        assert f"- {json.dumps('a', ensure_ascii=False)}" in text
        assert "default_rate: 0.21" in text

    def test_main_block_writes_default_config(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        repo_root = Path(__file__).resolve().parents[1]
        module_path = repo_root / "src" / "generate_config.py"
        runpy.run_path(str(module_path), run_name="__main__")
        default_out = tmp_path / "config.yaml"
        assert default_out.is_file()
        assert "kata-devops" in default_out.read_text(encoding="utf-8")

    def test_nan_tax_rate_uses_default(self, tmp_path):
        out = tmp_path / "c.yaml"
        generate_config(tax_rate=float("nan"), output_path=str(out))
        assert "default_rate: 0.09" in out.read_text(encoding="utf-8")

    def test_invalid_endpoints_fallback(self, tmp_path):
        out = tmp_path / "c.yaml"
        generate_config(endpoints="not-a-list", output_path=str(out))
        text = out.read_text(encoding="utf-8")
        for ep in ("dictionary", "costs", "concatenate"):
            assert json.dumps(ep, ensure_ascii=False) in text

    def test_output_path_null_byte_rejected(self, tmp_path):
        out = str(tmp_path / "bad\x00.yaml")
        with pytest.raises(ValueError):
            generate_config(output_path=out)

    def test_empty_output_path_rejected(self, tmp_path):
        with pytest.raises(ValueError):
            generate_config(output_path="   ")
