# Robotics examples and integration scaffolds

Small source examples for exploring manipulation workflows. Readiness differs by example.

| Directory | Current implementation |
|---|---|
| `01-grasp-showcase` | Scripted grasp calls using `Hand.mock()` and console output; no scene rendering or physical hand |
| `02-teleoperation-glove` | Prints a glove-adapter integration instruction; no glove input is read |
| `03-rl-policy-inference` | Prints policy input expectations; no model is loaded or evaluated |
| `04-mujoco-sim` | Prints setup expectations; no MJCF scene or controller is run |
| `05-ros2-moveit` | Prints setup instructions; no MoveIt planning configuration is launched |

The first script depends on the [Dexterous Hand SDK](https://github.com/stonedrum-robotics/dexterous-hand-sdk). The remaining directories are starting points for implementation, not completed demonstrations. Review their source and prerequisites before use.

For current mock-code scope, start with the SDK README. These examples do not establish device support, physics simulation, policy performance or a customer-ready integration.
