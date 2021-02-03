# Random Settings Generator
This script will generate a plando json file that can be fed into the Ocarina of Time randomzier with random values for each of the randomizer settings.
This script allows us to blindly randomize anything and (nearly) everything in the ranomizer, rather than just the natively supported random settings.

## Instructions
1. Download the public branch of Ocarina of Time Randomizer. Version 6.0.0  (https://github.com/TestRunnerSRL/OoT-Randomizer/tree/master).
2. Navigate to the folder that contains `Gui.py` and make a new folder named `random-settings-generator`.
3. Place the contents of this repository in this new folder.
4. Run `RandomSettingsGenerator.py` by either double clicking via the command line `$ python3 RandomSettingsGenerator.py` to generate `random_settings_generation.json`.
5. Use this file as a plando file when you generate your randomizer seed.

## Multiworld
Since rando rando seeds can take a long time, there are some settings we can use to ease the pain. You can now define the variable `mw_weights_file` (commented in `RandomSettingsGenerator.py`) to a file with edits to the weights. After loading the weight file you specify, this file will be loaded and overwrite anything included. You are also able to specify specific starting items in this file. We provide an example in `weights/rsg_multiworld.json` that we use for multiworld.

## FAQ
#### When I double click `RandomSettingsGenerator.py` nothing happens and no file is generated.

The script is crashing. Ensure that you have the correct version of Ocarina of Time randomizer 6.0.0 and that the script is in the correct directory. If it is still not working, try to run via the command line to see the error message.
