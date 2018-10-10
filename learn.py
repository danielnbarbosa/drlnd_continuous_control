#!/usr/bin/env pythonw

import argparse
import environment, agent, model, training

parser = argparse.ArgumentParser()
parser.add_argument("--load", help="path to saved model", type=str, default=None)
args = parser.parse_args()

# create objects and run training
environment = environment.UnityMLVectorMultiAgent()
model = model.LowDim2x()
agent = agent.DDPG(model, load_file=args.load)
training.train(environment, agent)
