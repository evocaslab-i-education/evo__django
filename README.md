# Django application

---
![Main](https://github.com/evocaslab-i-education/evo__django/actions/workflows/python-main.yml/badge.svg)

## 🏠 Homework

Homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🏗️ Preparation

Make some initialization steps. For example, copy configs.

```shell
make init-configs-i-dev
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏯️ Run extended

Shutdown previous, run in detached mode, follow logs

```shell
make d-run-i-extended
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```

---

### Add 2 humans via docker

```shell
make d-i-django-i-create-humans-i-2
```