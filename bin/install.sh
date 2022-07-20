#!/bin/sh

cd "$(dirname "$0")/../src" || exit 1

src_path=$(pwd)
bin_path=$HOME/bin
mkdir -p "$bin_path"
ln -sfv "$src_path"/base_template_cli.py "$bin_path"/base-template-cli

if [ "$PATH" = "$bin_path" ] || [ "$PATH" = "${bin_path}/" ]; then
  exit
fi

if echo "$PATH" | grep -q -e "${bin_path}:" -e "${bin_path}/:" -e ":${bin_path}"; then
  exit
fi

shell_name=$(basename "$SHELL")

case $shell_name in
  bash) shell_rc_path=$HOME/.bashrc ;;
  zsh) shell_rc_path=$HOME/.zshrc ;;
  *)
    printf "Run the following command:\n\n"
    # shellcheck disable=SC2016
    echo 'echo "export PATH=\"\${HOME}/bin:\${PATH}\"" >> <your shell rc file path (e.g., ~/.bashrc)>'
    exit
    ;;
esac

echo "export PATH=\"\${HOME}/bin:\${PATH}\"" >> "$shell_rc_path"
