# mpfh
This is MPFH (menu program for Hyprland)
![зображення](https://github.com/goryan2101/mpfh/assets/153424343/7fa4e517-2608-4094-98f8-be215a281272)


# Dependencies
[brightnessctl](https://github.com/Hummer12007/brightnessctl) \
[pamixer](https://github.com/cdemoulins/pamixer)\
[foot](https://codeberg.org/dnkl/foot) \
[python 3.9>](https://python.org)\
[python-kivy](https://kivy.org)


# Installation
```bash
cd
git clone https://github.com/goryan2101/mpfh.git
sudo cp setupprogram /bin/bash
mv main.py ~
```
Add this line to `hyprland.conf`:\
`bind = $mainMod, [your shortcut], exec, setupprogram`
# To launch
`setupprogram` or main modificator + your shortcut
