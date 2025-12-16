# Warhammer 40k Data Cards Website

A comprehensive website for Warhammer 40k unit data cards, featuring faction-specific unit lists, detailed datasheets, search functionality, unit comparison, army planning, and more.

## Features

- **Unit List Page**: Browse units by faction with filters for battlefield role, points range, keywords, and sorting by name or points.
- **Unit Datasheet Page**: Detailed view of unit stats, weapons, abilities, lore, and edition info.
- **Search Page**: Search units by name, keyword, or weapon name.
- **Unit Comparison Page**: Side-by-side comparison of selected units' stats, points, weapons, and abilities.
- **Army Planning Page**: Build an army list for a faction, track total points.
- **Updates/Changelog Page**: List of recent balance updates and changes.
- **About/Legal Page**: Site purpose, credits to Games Workshop, fan-made disclaimer.

## Core Features

- Fast navigation with top menu
- Clear datasheet formatting with tables
- Filtering and searching capabilities
- Mobile-friendly responsive design
- Dark theme styling

## Data

Currently includes sample units for Space Marines and Orks. Data structure supports:
- Name, Faction, Battlefield Role, Points, Keywords
- Stats (M, WS, BS, S, T, W, A, Ld, Sv)
- Weapons (Name, Range, Type, S, AP, D)
- Abilities, Lore, Edition

## Running the Site

To view the website locally:

1. Navigate to the `public` directory
2. Run a local server, e.g., `python3 -m http.server 8000`
3. Open `http://localhost:8000` in your browser

## Adding More Data

Edit the `allUnits` array in `public/index.html` to add more units or factions. Ensure the data structure matches the existing format.

## Future Expansions

- Detachment rules reference
- Stratagem database
- Save/load army lists
- Community ratings and notes