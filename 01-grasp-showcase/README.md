# Grasp Showcase

Runs a scripted sequence of named grasps in in-memory mock mode.

## Setup

The demo imports `dexterous_hand` from the sibling `dexterous-hand-sdk` repository (root package `dexterous_hand/`; there is no `/src` layout). From a parent directory holding both repositories:

```bash
cd demo-apps/01-grasp-showcase
PYTHONPATH="../../dexterous-hand-sdk" python main.py
```

## Demo script

The script calls `Hand.mock()` and prints the names `open`, `pinch`, `cylindrical`, `open` in that order. It updates stored joint values; it does not render a scene, simulate contact or command hardware.

The `open` grasp entry has an empty target dictionary, so those calls leave the current mock joint values unchanged. The script ends with the cylindrical joint values still stored. `Hand.open()` is a different operation that requests zero joint targets; this script does not call it.
