# Boilerplate Templates

Scaffold GitHub Actions workflows using boilerplate templates.

## template herzeus/thisoctober

Python CI Workflow with UV Package Manager

[View source files](/thisoctober)

```bash
boilerplate --output-folder=. --template-url=github.com/gkwa/herzeus/thisoctober
```

```bash
# Alternative: clone and use locally
git clone --depth 1 https://github.com/gkwa/herzeus
boilerplate --output-folder=. --template-url=herzeus/thisoctober
```

Creates:

```
.
├── .github
│   └── workflows
│       └── ci.yml
```
