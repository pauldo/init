#!/usr/bin/env bash

stow dotfiles
echo "source ~/.appendshrc" >>~/.bash_profile
source ~/.bash_profile
