# BCQEntangleMen
QHack Repo For the BCQEntangleMen

## Team Members

@erdabravest2001
@pranavkubc
@BestQuark
@moreza14


## Introduction

“The goal of this project is to explore the use of quantum neural networks (QNNs) for correcting sequencing errors in genomics. Current sequencing technologies suffer from high error rates, which can cause significant problems in genomics research. Traditional error-correction methods rely on heuristic algorithms, which can be computationally expensive and often fail to identify all errors. Quantum computing, on the other hand, has the potential to provide significant speedup for many types of computational problems, including those in genomics.”


## Dependencies

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

The main files can be found in the `src` directory. It contains a  `data_creation.ipynb` file which is used to create the data for the model. The `qcnn.ipynb` file is used to train and test the QCNN on the correction of genome sequences.

To run the language model we wanted to pair with the QCNN (but ran out of time), run 
    
```bash
gradio run src/app.py
```

For it to work, you will need the required API keys as local system variables.

## References

1. "Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and repeat separation" by Koren S, et al. Genome Research, 2017.
2. "Deep learning for error correction in nanopore sequencing" by Liu et al. BMC Genomics, 2019.
3. "DeepCov: predicting 3D genome folding using megabase-scale transfer learning from neural machine translation" by Hiranuma et al. Nature Communications, 2021.
4. "Highly accurate read mapping with an extended Kalman filter" by Zhang et al. PLoS ONE, 2017.