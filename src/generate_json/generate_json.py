# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "lizlooney@google.com (Liz Looney)"

# Python Standard Library
import pathlib
import sys

# absl
from absl import app
from absl import flags
from absl import logging

# robotpy
import hal
import hal.simulation
import ntcore
import pyfrc
import wpilib
import wpilib.counter
import wpilib.drive
import wpilib.event
import wpilib.interfaces
import wpilib.shuffleboard
import wpilib.simulation
import wpimath
import wpimath.controller
import wpimath.estimator
import wpimath.filter
import wpimath.geometry
import wpimath.interpolation
import wpimath.kinematics
import wpimath.optimization
import wpimath.path
import wpimath.spline
import wpimath.system
import wpimath.system.plant
import wpimath.trajectory
import wpimath.trajectory.constraint
import wpimath.units
import wpinet
import wpiutil

# External samples
sys.path.append("../external_samples")
import color_range_sensor
import component
import rev_touch_sensor
import servo
import smart_motor
import sparkfun_led_stick

# Common modules
sys.path.append("../common")
import python_util

# Local modules
import json_util


FLAGS = flags.FLAGS

flags.DEFINE_string('output_directory', None, 'The directory where output should be written.')


def main(argv):
  del argv  # Unused.

  if not FLAGS.output_directory:
    logging.error(f'You must specify the --output_directory argument')
    return

  pathlib.Path(f'{FLAGS.output_directory}/generate_json/').mkdir(parents=True, exist_ok=True)

  robotpy_modules = [
    hal,
    hal.simulation,
    ntcore,
    wpilib,
    wpilib.counter,
    wpilib.drive,
    wpilib.event,
    wpilib.interfaces,
    wpilib.shuffleboard,
    wpilib.simulation,
    python_util.getModule('wpilib.sysid'),
    wpimath,
    wpimath.controller,
    wpimath.estimator,
    wpimath.filter,
    wpimath.geometry,
    wpimath.interpolation,
    wpimath.kinematics,
    wpimath.optimization,
    wpimath.path,
    wpimath.spline,
    wpimath.system,
    wpimath.system.plant,
    wpimath.trajectory,
    wpimath.trajectory.constraint,
    wpimath.units,
    wpinet,
    wpiutil,
  ]
  json_generator = json_util.JsonGenerator(robotpy_modules)
  file_path = f'{FLAGS.output_directory}/generate_json/robotpy_data.json'
  json_generator.writeJsonFile(file_path)

  external_samples_modules = [
    color_range_sensor,
    component,
    rev_touch_sensor,
    servo,
    smart_motor,
    sparkfun_led_stick,
  ]
  json_generator = json_util.JsonGenerator(external_samples_modules)
  file_path = f'{FLAGS.output_directory}/generate_json/external_samples_data.json'
  json_generator.writeJsonFile(file_path)



if __name__ == '__main__':
  app.run(main)
