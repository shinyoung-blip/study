```
pip install huggingface_hub bop-toolkit-lib pycocotools ruamel.yaml

git clone https://github.com/WangYuLin-SEU/HCCEPose.git

huggingface-cli download SEU-WYL/HccePose --include "demo-bin-picking/*" --local-dir ./demo-bin-picking --repo-type dataset  
huggingface-cli download SEU-WYL/HccePose --include "test_imgs/*" --local-dir ./test_imgs --repo-type dataset 
huggingface-cli download SEU-WYL/HccePose --include "test_videos/*" --local-dir ./test_videos --repo-type dataset

unzip HCCEPose/bop_toolkit.zip -d . || true && \
    cp -r HCCEPose/kasal ./kasal || true
```
[기존 도커파일 참고](Uploading 스크린샷 2026-01-29 오후 3.47.32.png…)