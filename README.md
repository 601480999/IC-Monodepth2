# IC-Monodepth2

This codebase implements the system described in the paper:
> **Self-Supervised Joint Learning Framework of Depth Estimation via Implicit Cues**

See the paper on [[arXiv](https://arxiv.org/abs/2006.09876)]  for more details. 


### Requirements

* ` Anaconda3,  Pytorch 1.0, CUDA 8.0 and Ubuntu 16.04 ` 
* `Monodepth2` framework (https://github.com/nianticlabs/monodepth2)


### Run train

The train  files will be uploaded in the future.


### Pretrained models

You can download the following pre-trained models:

* [MS(K 192 640)]()
* [M(K 192 640)]()
* [M(CS+K 192 640)]()


### Run evaluation

```shell
python evaluate_depth.py --load_weights_folder ~/tmp/model_name/models/weights_19/ --eval_mono
```

### Depth Results

Train  |Resolution| Abs Rel | Sq Rel | RMSE  | RMSE(log) | Acc.1 | Acc.2 | Acc.3 |
-------|----------|---------|--------|-------|-----------|-------|-------|-------|
K (M)  | (192×640)|0.106    |0.799   |4.662  |0.187      |0.889  |0.961  |0.982  |
K (M)  |(320×1024)|0.106    |0.773   |4.491  |0.185      |0.890  |0.962  |0.982  |
K (MS) |(192×640) |0.102    |0.776   |4.534  |0.183      |0.893  |0.963  |0.982  |
K (MS) |(320×1024)|0.101    |0.725   |4.360  |0.179      |0.898  |0.965  |0.983  |
CS+K(M)| (192×640)|0.106    |0.774   |4.623  |0.184      |0.886  |0.962  |0.983  |
CS+K(M)|(320×1024)|0.104    |0.771   |4.463  |0.183      |0.893  |0.963  |0.982  |

### Citation

If you reference our work, please consider citing the following:

@misc{wang2020selfsupervised,
        title={Self-Supervised Joint Learning Framework of Depth Estimation via Implicit Cues},
        author={Jianrong Wang and Ge Zhang and Zhenyu Wu and XueWei Li and Li Liu},
        year={2020},
        eprint={2006.09876},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
}



### Acknowledgements

Thanks to Niantic and Clément Godard for sharing Monodepth2 code
