# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

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