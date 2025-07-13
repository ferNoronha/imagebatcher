# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

## [0.1.2] - 2025-07-12
### Adicionado
- Novos steps: `invert`, `blur`, `threshold`, `autocontrast`, `erode`, `dilate`
- Suporte a geração de `report.jsonl` com tempo por step, status e erros
- Novo campo no YAML: `report_verbose` para ativar/desativar o relatório

### Melhorias
- Modularização de `process_single_image`
- Uso de `as_completed` com fallback seguro e logging de erro por future

## [0.1.1] - 2025-07-12
### Adicionado
- Suporte a configuração de parâmetros específicos por step no `pipeline.yaml` via campo `step_params`.
- Step `resize` agora aceita `width` e `height` como argumentos.

### Melhorias
- CLI `run-config` atualizada para repassar `step_params`.
- Refatoração do pipeline para permitir expansão dinâmica de parâmetros.

---

## [0.1.0] - 2025-07-10
### Inicial
- Primeira versão funcional do `imagebatcher`
- Processamento em lote com steps: `resize`, `grayscale`
- CLI com suporte a parâmetros: `--input`, `--output`, `--steps`, `--resize-shape`
- Execução paralela com `ThreadPoolExecutor`
- Logs com opção `--verbose`
- Suporte a execução via `pipeline.yaml`
- Barra de progresso com `tqdm`