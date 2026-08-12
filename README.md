# EGLKeepalive

Mini script using [ModernGL](https://github.com/moderngl/moderngl) to keep a GPU from entering `D3cold`, by nudging an EGL context every second. Useful if you have a Nvidia Optimus laptop and the delay of GPU activation is annoying.

## Installing

Available on PyPI as [EGLKeepalive](https://pypi.org/project/EGLKeepalive/)

Recommended install using [pipx](https://github.com/pypa/pipx):

```
$ pipx install EGLKeepalive
```

## Example effect

Make use of the `GLCONTEXT_DEVICE_INDEX` environment variable on the command line, that overrides which graphics card / device that EGL chooses. Our Python code uses

```py
gl = mgl.create_context(standalone = True, backend = "egl")
```

but with `GLCONTEXT_DEVICE_INDEX=67` on the command line is equivalent to

```py
gl = mgl.create_context(standalone = True, backend = "egl", device_index = 67)
```

so have a play with different `GLCONTEXT_DEVICE_INDEX=123` to get it to work.

```
$ cat /sys/class/drm/card*/device/power_state
D3cold
D0
$ # lazy Nvidia GPU is fast asleep; power saving or something...

$ GLCONTEXT_DEVICE_INDEX=1 egl-keepalive &
$ # wakey wakey

$ cat /sys/class/drm/card*/device/power_state
D0
D0
$ # it's OpenGL time

```
