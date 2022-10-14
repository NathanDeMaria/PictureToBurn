#!/usr/bin/env bash
alias gs="git status"
alias gpuo="git push -u origin $(git branch | grep \* | cut -d " " -f2)"
alias gcm="git checkout main"
alias grbm="git stash && git rebase main && git stash pop"
