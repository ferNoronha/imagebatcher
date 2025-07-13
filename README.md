# imagebatcher

Framework leve para processamento em lote de imagens com steps encadeáveis como resize, grayscale.

## Como usar

```bash
python cli.py --input ./imagens --output ./saida --steps resize,grayscale
```

## 🧪 Executando com pipeline.yaml

Você pode definir todos os parâmetros em um arquivo `pipeline.yaml` e executar com um único comando.

### Comando para executar:

```bash
python cli.py run-config --config pipeline.yaml
```

## 📝 Parâmetros suportados:
| Parâmetro      | Tipo   | Descrição                                                      |
| -------------- | ------ | -------------------------------------------------------------- |
| `input`        | string | Caminho para a pasta com imagens originais                     |
| `output`       | string | Pasta onde serão salvos os arquivos processados                |
| `steps`        | lista  | Lista de steps aplicados em ordem (`resize`, `grayscale`, etc.)|
| `workers`      | int    | Número de threads para processamento paralelo                  |
| `verbose`      | bool   | Se `false`, esconde os logs detalhados                         |

## ✅ Comandos CLI disponíveis

```bash
# Rodar via linha de comando (modo direto)
python cli.py process-images --input ./imagens --output ./saida --steps resize --resize-shape 800

# Rodar via YAML
python cli.py run-config --config pipeline.yaml
```

## 🧪 Executando com pipeline.yaml
Você pode definir todos os parâmetros do pipeline em um arquivo YAML, incluindo parâmetros específicos para cada step.
📄 Exemplo de pipeline.yaml com step_params:
```yaml
input: "./imagens"
output: "./saida"
steps:
  - grayscale
  - autocontrast
  - blur
  - threshold
  - erode
  - dilate
  - ocr

step_params:
  blur:
    radius: 1.5
  threshold:
    threshold: 100
  autocontrast:
    cutoff: 1
  erode:
    kernel_size: 3
    iterations: 1
  dilate:
    kernel_size: 3
    iterations: 1

workers: 4
verbose: true
report_verbose: true
```
## ⚙️ step disponíveis atualmente:

| Nome           | Descrição                                                | Parâmetros disponíveis        |
| -------------- | -------------------------------------------------------- | ----------------------------- |
| `resize`       | Redimensiona imagem para largura/altura                  | `width`, `height`             |
| `grayscale`    | Converte para tons de cinza                              | —                             |
| `invert`       | Inverte as cores (negativo)                              | —                             |
| `blur`         | Aplica desfoque Gaussian                                 | `radius` (float)              |
| `threshold`    | Binariza imagem (0 ou 255)                               | `threshold` (int de 0 a 255)  |
| `autocontrast` | Ajusta contraste automaticamente                         | `cutoff` (0 a 100)            |
| `erode`        | Aplica erosão (remove bordas finas)                      | `kernel_size`, `iterations`   |
| `dilate`       | Aplica dilatação (expande bordas, bom p/ reforçar texto) | `kernel_size`, `iterations`   |



## ✅ Observações
Você pode usar resize_shape para compatibilidade, mas o recomendado agora é usar step_params.resize.

Se step_params estiver presente, ele será priorizado para os steps que aceitarem argumentos específicos.

Os parâmetros são passados como **kwargs diretamente para cada função process(...).