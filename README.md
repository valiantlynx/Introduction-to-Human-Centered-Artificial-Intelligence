##Exclude Changes Temporarily This will stop Git from tracking changes to these files in your local repository.
```sh
git update-index --skip-worktree .devcontainer/devcontainer.json
git update-index --skip-worktree .vscode/settings.json
```

## Reverting  back
```sh
git update-index --no-skip-worktree .devcontainer/devcontainer.json
git update-index --no-skip-worktree .vscode/settings.json
```