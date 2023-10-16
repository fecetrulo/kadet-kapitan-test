# MWE kapitan version output break

MWE for a output (compiled) changing when compiling with kapitan `0.30.0` and `0.32.0`.

## 0.30.0 output

```yaml
data: 'bind x.x.x.x

  databases xx

  save xxx xxx'

```

## 0.32.0 output

```yaml
data: "bind x.x.x.x\ndatabases xx\nsave xxx xxx"
```

## Quick start 0.30.0

I'm using a pyenv with python `3.8` with locked `pyyaml` version, that's the unique way that i'm currently able to run kapitan `0.30.0` (that's the main reason why i'm trying to migrate to the new version).

## Quick start 0.32.0

- `poetry install`
- `poetry run kapitan compile`
