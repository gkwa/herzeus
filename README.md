# Boilerplate Templates

Scaffold GitHub Actions workflows using boilerplate templates.

## herzeus/thisoctober
Python CI Workflow with UV Package Manager

[View source files](https://github.com/gkwa/herzeus/tree/master/thisoctober)

```bash
boilerplate --template-url=https://github.com/gkwa/herzeus/thisoctober --output-folder=.

# Alternative: clone and use locally
git clone --depth 1 https://github.com/gkwa/herzeus
boilerplate --template-url=herzeus/thisoctober --output-folder=.
```

Creates:
```
.
├── .github
│   └── workflows
│       └── ci.yml
└── your_project_files
```