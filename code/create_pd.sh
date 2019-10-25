#!/usr/bin/env bash

# This script creates the imax-dataset.

# create a dataset and go into that Folder.
datalad create -c bids $1/PD
cd $1/PD

# install the build-repo
datalad install -d . -s git@github.com:TobiasKadelka/build_imax.git code/build_pd
datalad save code -m "installed the code for creating the dataset."

