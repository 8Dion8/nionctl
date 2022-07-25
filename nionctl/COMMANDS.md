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

* `bt`
* `gitclone`
* `neofetch`
* `wifi`

## `nionctl bt`

**Usage**:

```console
$ nionctl bt [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `connect`
* `disconnect`
* `list`
* `off`
* `on`
* `pair-off`
* `pair-on`
* `remove`

### `nionctl bt connect`

**Usage**:

```console
$ nionctl bt connect [OPTIONS] SSID
```

**Arguments**:

* `SSID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt disconnect`

**Usage**:

```console
$ nionctl bt disconnect [OPTIONS] SSID
```

**Arguments**:

* `SSID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt list`

**Usage**:

```console
$ nionctl bt list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt off`

**Usage**:

```console
$ nionctl bt off [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt on`

**Usage**:

```console
$ nionctl bt on [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt pair-off`

**Usage**:

```console
$ nionctl bt pair-off [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt pair-on`

**Usage**:

```console
$ nionctl bt pair-on [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `nionctl bt remove`

**Usage**:

```console
$ nionctl bt remove [OPTIONS] SSID
```

**Arguments**:

* `SSID`: [required]

**Options**:

* `--help`: Show this message and exit.

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
