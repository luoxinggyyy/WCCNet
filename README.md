# WCCNet

_Article title: Missing well log prediction using wavelet convolution and connection_  
_Journal title: Computers and Geosciences_
##  Usage
python+pytorch  
GPU: RTX 3060 or 3060+
---
## Installation
   pip install -r `requirement.txt`
 ---  

 ## Quick Start
    python run_log.py --data log1 --features M  --seq_len 48 --label_len 24 --pred_len 24 --hidden-size 4 --stacks 1 --levels 3 --lr 3e-3 --batch_size 8 --dropout 0.5 --model_name log1_M_I48_O24_lr3e-3_bs8_dp0.5_h4_s1l
   
---

## Acknowledgements


This code uses ([TimesNet](https://github.com/thuml/TimesNet), [SCINet](https://github.com/cure-lab/SCINet)) as baseline methods for comparison.
