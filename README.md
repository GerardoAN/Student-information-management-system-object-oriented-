# Student-information-management-system-object-oriented-
This project contains a complete game loop, collision detection and explosion animation system, which is suitable for Python beginners to learn the basics of game development.
Aircraft War Game https://img.shields.io/badge/license-MIT-blue.svg
A classic 2D shooting game based on Pygame, which controls the movement of fighter planes through the direction keys, and the space bar fires three rounds of bullets to shoot down enemy planes. This project contains a complete game loop, collision detection and explosion animation system, which is suitable for Python beginners to learn the basics of game development.

./images/game_screenshot.png

functional performance
Player control system: Support the direction key (←↓→) to control the movement of fighter in real time.
Intelligent enemy aircraft AI: The enemy aircraft automatically moves left and right and touches the boundary to turn.
Three-shot system: press the space bar to trigger a multi-ballistic attack
Collision detection mechanism: Accurately judge the collision area between bullets and enemy planes.
Blasting animation sequence: 6 frames of high-definition blasting special effects (including resource files)
Smooth game cycle: 60FPS frame rate ensures smooth game.
quick start
Environmental configuration
bash
# Install the dependency library (Pygame 2.1.3+ is recommended)
Pip install -r requirements.txt # contains: pygame==2.1.3.
Run the game
bash
Gitclone https://github.com/ Your User Name/Aircraft Wars. git
Cd airplane war
python aircraft_war.py
Code architecture analysis
Core module design
python
# Player Fighter Control (Page 3)
def hero_plane():
Global hero_x, hero_y # use global coordinate variables.
# Event Listener Handles WASD and Spacebar
# Bullet objects are stored as a dictionary list structure.

# Hostile Aircraft Behavior System (webpage 2)
def enemy_plane():
Global enemy_x, enemy_path # Automatic moving path calculation
# Collision detection range: X axis [enemy_x, enemy_x+165], y axis [0,265].
# Explosion animation realizes frame sequence playback through blow_up array.
Resource management norms
python
# Resource loading specification (aircraft_war_material directory needs to be created)
background = pygame.image.load("./aircraft_war_material/background.png")
hero = pygame.image.load("./aircraft_war_material/hero1.png")
Development roadmap
Increase the scoring system (score for killing enemy aircraft)
Realization of multi-enemy aircraft generator
Add sound management system
Develop the mechanism of increasing difficulty of checkpoints
matters need attention
Must ensure that the resource file directory structure is complete.
The recommended screen resolution is 400x800 pixels.
The game speed is controlled by time.sleep(0.01), which can be adjusted to change the rhythm.
The collision detection area is set according to the material size of the enemy plane (165x265).
Contribution guide
Welcome to submit improvements through Pull Request:

Forkburn warehouse
Create a feature branch (such as feature/enhancement-collision)
Submit code changes (subject to PEP8 specification)
Initiate Pull Request
Open source protocol
This project adopts MIT License, which allows free use and secondary development, but the original copyright notice needs to be retained.

Learning Tip: It is suggested to deeply understand the game cycle and event handling mechanism in combination with the Python Core Application course. PyCharm Professional Edition is recommended for debugging during development, and its integrated Pygame debugging tool can be used to speed up the development process.
