# Description:
This repository contains a re-upload of the original work by the Audio-AGI team. All credit for the model, training pipeline, and core implementation goes to the original authors.

# Original Repository:
https://github.com/Audio-AGI/AudioSep

https://audio-agi.github.io/Separate-Anything-You-Describe/

https://audio-agi.github.io/Separate-Anything-You-Describe/AudioSep_arXiv.pdf

https://huggingface.co/spaces/Audio-AGI/AudioSep/tree/main/checkpoint

https://drive.google.com/drive/folders/1PbCsuvdrzwAZZ_fwIzF0PeVGZkTk0-kL


# My Contribution:
I have cloned and uploaded the project here for personal use, learning, and reference. No modifications have been made to the original source code.



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

## Having trouble running the project? You can reach out to me anytime at: shyamchauhan5702@gmail.com