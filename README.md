## Setup
Clone the repository and setup the conda environment: 

  ```shell
  git clone https://github.com/Audio-AGI/AudioSep.git && \
  cd AudioSep && \ 
  conda env create -f environment.yml && \
  conda activate AudioSep
  ```
Download [model weights](https://huggingface.co/spaces/Audio-AGI/AudioSep/tree/main/checkpoint) at `checkpoint/`.


## Benchmark Evaluation
Download the [evaluation data](https://drive.google.com/drive/folders/1PbCsuvdrzwAZZ_fwIzF0PeVGZkTk0-kL?usp=sharing) under the `evaluation/data` folder. The data should be organized as follows:

```yaml
evaluation:
    data:
        - audioset/
        - audiocaps/
        - vggsound/
        - music/
        - clotho/
        - esc50/
```
Run benchmark inference script, the results will be saved at `eval_logs/`


