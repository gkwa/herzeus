# Boilerplate Templates

Scaffold GitHub Actions workflows using boilerplate templates.

## herzeus/thisoctober
Python CI Workflow with UV Package Manager

[View source files](https://github.com/gkwa/herzeus/tree/master/thisoctober)



```bash
boilerplate --output-folder=. --template-url=--template-url=github.com/gkwa/herzeus/thisoctober 

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
└── your_project_files
```