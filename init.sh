#!/usr/bin/env bash

stow --adopt dotfiles
echo "[[ -f ~/.append ]] && source ~/.append" >>$HOME/.bash_profile
[[ -f $HOME/.zshrc ]] && echo "[[ -f ~/.append ]] && source ~/.append" >>$HOME/.zshrc
[[ -f ~/.append ]] && source ~/.append
