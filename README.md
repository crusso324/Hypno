# Hypno

A simple hypnotic spiral generator built with Python and pygame.

## Requirements

- Python 3
- pygame (`pip install pygame`)

## Usage

Run the generator from the command line:

```bash
python hypno.py [options]
```

### Options

- `--width`, `--height` - set the window size
- `--text` - text to overlay at the center
- `--text-color` - color name for the overlay text
- `--flash-rate` - flash frequency in Hertz (0 disables flashing)
- `--show-dots` - enable rotating dots
- `--show-cross` - enable rotating cross
- `--speed` - rotation speed in radians per frame

Example:

```bash
python hypno.py --text "Look here" --flash-rate 2 --show-dots --show-cross
```

Press the window close button to quit.
