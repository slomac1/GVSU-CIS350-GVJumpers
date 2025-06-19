# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['game_manager.py'],
    pathex=[],
    binaries=[],
    datas=[('Platformer/images/archways.png', 'Platformer/images'), ('Platformer/images/cards_game_booth.png', 'Platformer/images'), ('Platformer/images/carnival_manager.png', 'Platformer/images'), ('Platformer/images/clouds.png', 'Platformer/images'), ('Platformer/images/dart_game_booth.png', 'Platformer/images'), ('Platformer/images/end_the_game.png', 'Platformer/images'), ('Platformer/images/ending_message.png', 'Platformer/images'), ('Platformer/images/enter_minigame_prompt.png', 'Platformer/images'), ('Platformer/images/enter_tent_prompt.png', 'Platformer/images'), ('Platformer/images/fence_tiles.png', 'Platformer/images'), ('Platformer/images/fence_tilesheet.png', 'Platformer/images'), ('Platformer/images/ferris_wheel.png', 'Platformer/images'), ('Platformer/images/game_booth.png', 'Platformer/images'), ('Platformer/images/archways.png', 'Platformer/images'), ('Platformer/images/lost.png', 'Platformer/images'), ('Platformer/images/player_controls.png', 'Platformer/images'), ('Platformer/images/player_controls_tent.png', 'Platformer/images'), ('Platformer/images/puzzle_game_booth.png', 'Platformer/images'), ('Platformer/images/ring_wall.png', 'Platformer/images'), ('Platformer/images/scaffolding_long.png', 'Platformer/images'), ('Platformer/images/scaffolding_short.png', 'Platformer/images'), ('Platformer/images/scaffolding_sides.png', 'Platformer/images'), ('Platformer/images/sprites_02.png', 'Platformer/images'), ('Platformer/images/stands.png', 'Platformer/images'), ('Platformer/images/starting_message.png', 'Platformer/images'), ('Platformer/images/tall_scaffolding.png', 'Platformer/images'), ('Platformer/images/tent.png', 'Platformer/images'), ('Platformer/images/tent_background.png', 'Platformer/images'), ('Platformer/images/tent_ground_tiles.png', 'Platformer/images'), ('Platformer/images/tiletest2.png', 'Platformer/images'), ('Platformer/images/update_tile_blocks.png', 'Platformer/images'), ('Platformer/images/won.png', 'Platformer/images'), ('Platformer/images/zombie_spritesheet.png', 'Platformer/images'), ('DartGame/images/picture_dart.png', 'DartGame/images'), ('DartGame/images/picture_dartboard.png', 'DartGame/images'), ('Blackjack/images/1C.jpg', 'Blackjack/images'), ('Blackjack/images/1D.jpg', 'Blackjack/images'), ('Blackjack/images/1H.jpg', 'Blackjack/images'), ('Blackjack/images/1S.jpg', 'Blackjack/images'), ('Blackjack/images/2C.jpg', 'Blackjack/images'), ('Blackjack/images/2D.jpg', 'Blackjack/images'), ('Blackjack/images/2H.jpg', 'Blackjack/images'), ('Blackjack/images/2S.jpg', 'Blackjack/images'), ('Blackjack/images/3C.jpg', 'Blackjack/images'), ('Blackjack/images/3D.jpg', 'Blackjack/images'), ('Blackjack/images/3H.jpg', 'Blackjack/images'), ('Blackjack/images/3S.jpg', 'Blackjack/images'), ('Blackjack/images/4C.jpg', 'Blackjack/images'), ('Blackjack/images/4D.jpg', 'Blackjack/images'), ('Blackjack/images/4H.jpg', 'Blackjack/images'), ('Blackjack/images/4S.jpg', 'Blackjack/images'), ('Blackjack/images/5C.jpg', 'Blackjack/images'), ('Blackjack/images/5D.jpg', 'Blackjack/images'), ('Blackjack/images/5H.jpg', 'Blackjack/images'), ('Blackjack/images/5S.jpg', 'Blackjack/images'), ('Blackjack/images/6C.jpg', 'Blackjack/images'), ('Blackjack/images/6D.jpg', 'Blackjack/images'), ('Blackjack/images/6H.jpg', 'Blackjack/images'), ('Blackjack/images/6S.jpg', 'Blackjack/images'), ('Blackjack/images/7C.jpg', 'Blackjack/images'), ('Blackjack/images/7D.jpg', 'Blackjack/images'), ('Blackjack/images/7H.jpg', 'Blackjack/images'), ('Blackjack/images/7S.jpg', 'Blackjack/images'), ('Blackjack/images/8C.jpg', 'Blackjack/images'), ('Blackjack/images/8D.jpg', 'Blackjack/images'), ('Blackjack/images/8H.jpg', 'Blackjack/images'), ('Blackjack/images/8S.jpg', 'Blackjack/images'), ('Blackjack/images/9C.jpg', 'Blackjack/images'), ('Blackjack/images/9D.jpg', 'Blackjack/images'), ('Blackjack/images/9H.jpg', 'Blackjack/images'), ('Blackjack/images/9S.jpg', 'Blackjack/images'), ('Blackjack/images/10C.jpg', 'Blackjack/images'), ('Blackjack/images/10D.jpg', 'Blackjack/images'), ('Blackjack/images/10H.jpg', 'Blackjack/images'), ('Blackjack/images/10S.jpg', 'Blackjack/images'), ('Blackjack/images/11C.jpg', 'Blackjack/images'), ('Blackjack/images/11D.jpg', 'Blackjack/images'), ('Blackjack/images/11H.jpg', 'Blackjack/images'), ('Blackjack/images/11S.jpg', 'Blackjack/images'), ('Blackjack/images/12C.jpg', 'Blackjack/images'), ('Blackjack/images/12D.jpg', 'Blackjack/images'), ('Blackjack/images/12H.jpg', 'Blackjack/images'), ('Blackjack/images/12S.jpg', 'Blackjack/images'), ('Blackjack/images/13C.jpg', 'Blackjack/images'), ('Blackjack/images/13D.jpg', 'Blackjack/images'), ('Blackjack/images/13H.jpg', 'Blackjack/images'), ('Blackjack/images/13S.jpg', 'Blackjack/images'), ('Blackjack/images/background.jpg', 'Blackjack/images'), ('Blackjack/images/Yellow_back.jpg', 'Blackjack/images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='game_manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
