# IC-Monodepth2

This codebase implements the system described in the paper:
> **Self-Supervised Joint Learning Framework of Depth Estimation via Implicit Cues**

See the paper on [[arXiv](https://arxiv.org/abs/2006.09876)]  for more details. 






### Depth Results
Train  |Resolution| Abs Rel | Sq Rel | RMSE  | RMSE(log) | Acc.1 | Acc.2 | Acc.3 |
-------|----------|---------|--------|-------|-----------|-------|-------|-------|
K (M)  | (192×640)|0.106    |0.799   |4.662  |0.187      |0.889  |0.961  |0.982  |
K (M)  |(320×1024)|0.106    |0.773   |4.491  |0.185      |0.890  |0.962  |0.982  |
K (MS) |(192×640) |0.102    |0.776   |4.534  |0.183      |0.893  |0.963  |0.982  |
K (MS) |(320×1024)|0.101    |0.725   |4.360  |0.179      |0.898  |0.965  |0.983  |
CS+K(M)| (192×640)|0.106    |0.774   |4.623  |0.184      |0.886  |0.962  |0.983  |
CS+K(M)|(320×1024)|0.104    |0.771   |4.463  |0.183      |0.893  |0.963  |0.982  |


### Acknowledgements
Thanks to Niantic and Clément Godard for sharing Monodepth2 code
