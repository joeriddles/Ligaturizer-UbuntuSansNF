#!/usr/bin/env bash
set -eu -o pipefail

# git module init
if [ "$( ls -A 'fonts/fira' | wc -l | xargs )" -eq 0 ]; then
  git submodule update --init
fi

# Download and unzip UbuntuSans Nerd Font
if [ -z "$(ls -A 'fonts/UbuntuSansMonoNerdFont' )" ]; then

  if [ ! -f UbuntuSans.zip ]; then
    UbuntuSansNerdFontUrl=$(curl -fsSL 'https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest' | jq -c '.assets[] | select(.name | contains("UbuntuSans.zip")) | .browser_download_url' | xargs)
    curl -fsSL "$UbuntuSansNerdFontUrl" -o UbuntuSans.zip
  fi

  unzip -d './fonts/UbuntuSansMonoNerdFont' -o UbuntuSans.zip
fi

# Make sure fontforge is installed, assumes macOS
if ! command -v fontforge >/dev/null; then
  brew install fontforge
fi

# build 'da font
make
