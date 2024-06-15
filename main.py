from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.config import Config
import subprocess

Config.set("graphics", "width", 640)
Config.set("graphics", "height", 480)

main_layout = BoxLayout(orientation="vertical")
volume_layout = BoxLayout(orientation="vertical")
volume = Slider(min=0, max=100, value=int(subprocess.run(["pamixer", "--get-volume"], capture_output=True).stdout))
volume_label = Label(text=str(int(volume.value)), font_size=25)
bright_layout = BoxLayout(orientation="vertical")
bright = Slider(min=1, max=int(subprocess.run(["brightnessctl", "max"], capture_output=True).stdout), value=int(subprocess.run(["brightnessctl", "get"], capture_output=True).stdout))
bright_label = Label(text=str(int(bright.value)), font_size=25)
timedate = Label(text=subprocess.run(["date"], capture_output=True).stdout.decode("utf-8"), font_size=18)
battery = Label(text=
                "Baterry:" +
                subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity"], capture_output=True).stdout.decode("utf-8") +
                subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity_level"], capture_output=True).stdout.decode("utf-8"),
                font_size=18, size=[640, 18])
buttons = BoxLayout(orientation="horizontal")
config_button = Button(text="Open config file", font_size=16)
shutdown_button = Button(text="Shutdown", font_size=16)
reboot_button = Button(text="Reboot", font_size=16)


def open_config_file(instance):
    subprocess.run(["foot", "nano", "~/.config/hypr/hyprland.conf"])
config_button.bind(on_press=open_config_file)

def shutdown(instance):
    subprocess.run(["systemctl", "-i", "poweroff"])
shutdown_button.bind(on_press=shutdown)

def reboot(instance):
    subprocess.run(["systemctl", "reboot"])
reboot_button.bind(on_press=reboot)

def update_volume(dt):
    subprocess.run(["pamixer", "--set-volume", str(int(volume.value))])
    volume_label.text = "Volume: " + str(int(volume.value))

def update_brightness(dt):
    subprocess.run(["brightnessctl", "-q", "set", str(int(bright.value))])
    bright_label.text = "Brightness: " + str(int(bright.value))

def update_timedate(dt):
    timedate.text = subprocess.run(["date"], capture_output=True).stdout.decode("utf-8")

def update_battery(dt):
    battery.text = "Baterry: " + subprocess.run(["cat", "/sys/class/power_supply/BAT0/capacity"], capture_output=True).stdout.decode("utf-8")

class SettingsApp(App):
    def build(self):
        volume_layout.add_widget(volume_label)
        volume_layout.add_widget(volume)
        main_layout.add_widget(volume_layout)
        bright_layout.add_widget(bright_label)
        bright_layout.add_widget(bright)
        buttons.add_widget(config_button)
        buttons.add_widget(shutdown_button)
        buttons.add_widget(reboot_button)
        main_layout.add_widget(bright_layout)
        main_layout.add_widget(timedate)
        main_layout.add_widget(battery)
        main_layout.add_widget(buttons)
        return main_layout
        
if __name__ == "__main__":
    Clock.schedule_interval(update_volume, 1/30)
    Clock.schedule_interval(update_brightness, 1/30)
    Clock.schedule_interval(update_timedate, 1)
    Clock.schedule_interval(update_battery, 1/20)
    SettingsApp().run()
