import argparse
import mlops_hyperparameter_tuning

parser = argparse.ArgumentParser()
parser.add_argument("--learning_rate", "-lr", type=float, default=1e-4)
parser.add_argument("--weight_decay", "-wd", type=float, default=0.0)
parser.add_argument("--batch_size", "-bs", type=int, default="64")
args = parser.parse_args()

mlops_hyperparameter_tuning.train(vars(args))
