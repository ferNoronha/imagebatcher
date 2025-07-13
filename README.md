# imagebatcher

Framework leve para processamento em lote de imagens com steps encadeáveis como resize, grayscale.

## Como usar

```bash
python cli.py --input ./imagens --output ./saida --steps resize,grayscale
```

## 🧪 Executando com pipeline.yaml

Você pode definir todos os parâmetros em um arquivo `pipeline.yaml` e executar com um único comando.

### Exemplo de arquivo `pipeline.yaml`:

```yaml
input: "./imagens"
output: "./saida"
steps:
  - resize
  - grayscale
resize_shape: "800"
workers: 4
verbose: true
```
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
  - resize
  - grayscale

step_params:
  resize:
    width: 100
    height: 0         
workers: 4
verbose: true
```
## ⚙️ step_params disponíveis atualmente:

| Step   | Parâmetro | Tipo | Descrição                                     |
| ------ | --------- | ---- | --------------------------------------------- |
| resize | `width`   | int  | Largura final da imagem                       |
|        | `height`  | int  | Altura final; se 0, calcula proporcionalmente |


## ✅ Observações
Você pode usar resize_shape para compatibilidade, mas o recomendado agora é usar step_params.resize.

Se step_params estiver presente, ele será priorizado para os steps que aceitarem argumentos específicos.

Os parâmetros são passados como **kwargs diretamente para cada função process(...).