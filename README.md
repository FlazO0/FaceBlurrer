# Desfocador de Rosto

### Visão Geral do Projeto

Este projeto é um desfocador de rosto que utiliza a biblioteca OpenCV e o módulo FaceDetector do cvzone para detectar rostos em tempo real usando a câmera do seu computador e aplicar um efeito de desfoque nas regiões dos rostos detectados.

### Funcionalidades

- Detecção de rostos em tempo real usando a câmera do computador.
- Aplicação de efeito de desfoque nas regiões dos rostos detectados.

### Tecnologias Utilizadas

- **Python:** Linguagem de programação principal do projeto.
- **OpenCV:** Biblioteca para processamento de imagens e vídeo.
- **cvzone:** Biblioteca que facilita a detecção de rostos e outras funcionalidades.

### Configuração e Instalação

#### Requisitos

- Python 3.7 ou superior
- OpenCV
- cvzone

#### Clone o Repositório

```bash
git clone https://github.com/FlazO0/FaceBlurrer.git
cd FaceBlurrer
```

#### Instale as Dependências

Certifique-se de ter o Python instalado. Em seguida, instale os pacotes necessários:

```bash
pip install opencv-python cvzone
```

### Uso

1. Certifique-se de que a câmera do seu computador está funcionando.
2. Execute o script Python:

    ```bash
    python app.py
    ```

3. A aplicação abrirá uma janela mostrando o vídeo da sua câmera com os rostos detectados desfocados.
4. Pressione `q` para sair da aplicação.

