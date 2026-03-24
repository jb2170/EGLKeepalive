# EGLKeepalive

Mini script using [ModernGL](https://github.com/moderngl/moderngl) to keep a GPU from entering `D3cold`, by nudging an EGL context every second. Useful if you have a Nvidia Optimus laptop and the delay of GPU activation is annoying.

## Installing

Available on PyPI as [EGLKeepalive](https://pypi.org/project/EGLKeepalive/)

Recommended install using [pipx](https://github.com/pypa/pipx):

```
$ pipx install EGLKeepalive
```

## Example effect

```
$ cat /sys/class/drm/card*/device/power_state
D3cold
D0
$ # lazy Nvidia GPU is fast asleep; power saving or something...

$ DRI_PRIME=0 glxinfo | grep "OpenGL renderer"
OpenGL renderer string: Mesa Intel(R) HD Graphics 630 (KBL GT2)
$ # not this one

$ DRI_PRIME=1 glxinfo | grep "OpenGL renderer"
OpenGL renderer string: NV136
$ # this one, so use DRI_PRIME=1

$ DRI_PRIME=1 egl-keepalive &
$ # wakey wakey

$ cat /sys/class/drm/card*/device/power_state
D0
D0
$ # it's OpenGL time

```
