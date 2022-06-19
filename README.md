# Django application

---

## Preparation

Make some initialization steps. For example, copy configs.

```shell
make init-configs-i-dev
```

## 🐳 Docker

### Run

Just run

```shell
make d-run
```

### Run extended

Shutdown previous, run in detached mode, follow logs

```shell
make d-run-i-extended
```

### Stop

Stop services

```shell
make d-stop
```

### Purge

Purge all data related with services

```shell
make d-purge
```