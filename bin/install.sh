#!/bin/sh

cd "$(dirname "$0")/../src" || exit 1

src_path=$(pwd)
mkdir -p ~/bin

ln -sfv "$src_path"/base_template_cli.py ~/bin/base-template-cli
