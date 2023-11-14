# check (https://rye-up.com/guide/) for more information
curl -sSf https://rye-up.com/get | zsh

rye sync

rye run pre-commit install
