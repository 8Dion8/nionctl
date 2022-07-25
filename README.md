# `nionctl`

**Usage**:

```console
$ nionctl [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `gitclone`
* `neofetch`
* `wifi`

## `nionctl gitclone`

**Usage**:

```console
$ nionctl gitclone [OPTIONS] LINK
```

**Arguments**:

* `LINK`: [required]

**Options**:

* `--dest TEXT`: [default: /home/dion/gitclones]
* `--help`: Show this message and exit.

## `nionctl neofetch`

**Usage**:

```console
$ nionctl neofetch [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `nionctl wifi`

**Usage**:

```console
$ nionctl wifi [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `connect`
* `disconnect`
* `list`

### `nionctl wifi connect`

**Usage**:

```console
$ nionctl wifi connect [OPTIONS] SSID
```

**Arguments**:

* `SSID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `nionctl wifi disconnect`

**Usage**:

```console
$ nionctl wifi disconnect [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl wifi list`

**Usage**:

```console
$ nionctl wifi list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
