# Formulas Related to ICBM Trajectory

#### Gravitational Force:
The gravitational force acting on an object of mass \( m \) due to Earth's gravitational field is given by Newton's law of universal gravitation:

```
F_g = G * (m * M) / r^2
```

where:
- \( F_g \) is the gravitational force,
- \( G \) is the gravitational constant (\( 6.67430 \times 10^{-11} \, \text{m}^3 \, \text{kg}^{-1} \, \text{s}^{-2} \)),
- \( M \) is the mass of the Earth,
- \( r \) is the distance between the object and the center of the Earth.

#### Aerodynamic Forces:
The drag force experienced by the missile due to air resistance is given by:

```
F_d = 0.5 * ρ * v^2 * A * C_d
```

where:
- \( F_d \) is the drag force,
- \( ρ \) is the air density,
- \( v \) is the velocity of the missile,
- \( A \) is the cross-sectional area of the missile,
- \( C_d \) is the drag coefficient.

The lift force acting on the missile perpendicular to its velocity vector can be expressed as:

```
F_l = 0.5 * ρ * v^2 * A * C_l
```

where:
- \( F_l \) is the lift force,
- \( C_l \) is the lift coefficient.

#### Structural Dynamics:
The structural damping force opposing the motion of the missile is given by:

```
F_damping = -b * v
```

where:
- \( b \) is the damping coefficient,
- \( v \) is the velocity of the missile.

The structural spring force resisting displacements from equilibrium is given by:

```
F_spring = -k * x
```

where:
- \( k \) is the spring constant,
- \( x \) is the displacement from equilibrium.

#### Rotational Motion:
The rotational inertia \( I \) of the missile can be calculated using the formula:

```
I = ∫ r^2 dm
```

where:
- \( r \) is the distance from the axis of rotation,
- \( dm \) is an elemental mass.

The angular damping torque opposing the rotational motion is given by:

```
τ_damping = -b_angular * ω
```

where:
- \( b_{\text{angular}} \) is the angular damping coefficient,
- \( ω \) is the angular velocity.
