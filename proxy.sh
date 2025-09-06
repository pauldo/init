#!/usr/bin/env bash

stow --adopt proxy
echo "source ~/.appendshrc_proxy" >>~/.bash_profile
source ~/.bash_profile
