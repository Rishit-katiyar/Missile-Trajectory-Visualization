import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
GRAVITATIONAL_CONSTANT = 6.67430e-11
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6371000
INITIAL_VELOCITY = 10000
LAUNCH_ANGLE = 45
TIME_STEP = 1000
SEGMENT_LENGTH = 200
DRAG_COEFFICIENT = 0.005
LIFT_COEFFICIENT = 0.001
CROSS_SECTIONAL_AREA = 1
MISSILE_MASS = 1000
STRUCTURAL_DAMPING = 0.1
STIFFNESS = 1000
ROTATIONAL_INERTIA = 5000
ANGULAR_DAMPING = 0.05

# Function to calculate air density
def air_density(altitude):
    return 1.225 * np.exp(-altitude / 8000)

# Function to calculate drag force
def drag_force(velocity, altitude):
    return 0.5 * air_density(altitude) * velocity ** 2 * DRAG_COEFFICIENT * CROSS_SECTIONAL_AREA

# Function to calculate lift force
def lift_force(velocity, altitude):
    return 0.5 * air_density(altitude) * velocity ** 2 * LIFT_COEFFICIENT * CROSS_SECTIONAL_AREA

# Function to calculate structural damping force
def structural_damping_force(velocity):
    return -STRUCTURAL_DAMPING * velocity

# Function to calculate structural spring force
def structural_spring_force(displacement):
    return -STIFFNESS * displacement

# Function to calculate total aerodynamic force
def total_aerodynamic_force(velocity, altitude, angular_velocity):
    return drag_force(velocity, altitude) + lift_force(velocity, altitude) - CROSS_SECTIONAL_AREA * ANGULAR_DAMPING * angular_velocity

# Function to calculate total structural force
def total_structural_force(velocity, displacement, angular_velocity, angular_displacement):
    return structural_damping_force(velocity) + structural_spring_force(displacement) - STIFFNESS * angular_displacement - ANGULAR_DAMPING * angular_velocity

# Function to simulate projectile motion
def simulate_projectile_motion(initial_velocity, launch_angle, time_step):
    launch_angle_radians = np.radians(launch_angle)
    x_positions = []
    y_positions = []
    x = 0
    y = 0
    altitude = EARTH_RADIUS
    v_x = initial_velocity * np.cos(launch_angle_radians)
    v_y = initial_velocity * np.sin(launch_angle_radians)
    displacement = 0
    angular_velocity = 0
    angular_displacement = 0
    apogee_reached = False
    while y >= 0:
        x_positions.append(x)
        y_positions.append(y)
        x += v_x * time_step
        y += (v_y * time_step) - (0.5 * GRAVITATIONAL_CONSTANT * EARTH_MASS / (EARTH_RADIUS + altitude) ** 2 * time_step ** 2)
        altitude = EARTH_RADIUS + y
        aerodynamic_force = total_aerodynamic_force(np.sqrt(v_x ** 2 + v_y ** 2), altitude, angular_velocity)
        structural_force = total_structural_force(np.sqrt(v_x ** 2 + v_y ** 2), displacement, angular_velocity, angular_displacement)
        v_y -= ((GRAVITATIONAL_CONSTANT * EARTH_MASS / (EARTH_RADIUS + altitude) ** 2 * time_step) + (aerodynamic_force / MISSILE_MASS * time_step))
        v_x -= (aerodynamic_force / MISSILE_MASS * v_x / np.sqrt(v_x ** 2 + v_y ** 2) * time_step)
        displacement += (v_y * time_step)
        angular_displacement += angular_velocity * time_step
        angular_velocity -= (STRUCTURAL_DAMPING / ROTATIONAL_INERTIA * angular_velocity + ANGULAR_DAMPING / ROTATIONAL_INERTIA * angular_displacement) * time_step
        if v_y < 0 and not apogee_reached:
            apogee_index = len(y_positions) - 1
            apogee_reached = True
    descent_segments = []
    segment_start = apogee_index
    while segment_start < len(y_positions) - 1:
        segment_end = min(segment_start + SEGMENT_LENGTH, len(y_positions) - 1)
        descent_segments.append((segment_start, segment_end))
        segment_start = segment_end
    return x_positions, y_positions, apogee_index, descent_segments

# Function to update the plot for each frame of the animation
def update(frame):
    if frame <= apogee_index:
        missile.set_color('#FF5733')  # Orange-red for ascending phase
        missile.set_data(x_positions[:frame], y_positions[:frame])
        label.set_text('Ascending Phase')
    else:
        for start, end in descent_segments:
            if start <= frame <= end:
                color = '#117A65'  # Dark green for descending phase
                missile.set_color(color)
                missile.set_data(x_positions[start:frame], y_positions[start:frame])
                label.set_text('Descending Phase')
                break
    return missile, label

# Function to initialize the plot
def init():
    missile.set_data([], [])
    return missile, label

# Simulate projectile motion
x_positions, y_positions, apogee_index, descent_segments = simulate_projectile_motion(INITIAL_VELOCITY, LAUNCH_ANGLE, TIME_STEP)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_title('Simulated Intercontinental Ballistic Missile Trajectory', fontsize=16)
ax.set_xlabel('Horizontal Distance (m)', fontsize=14)
ax.set_ylabel('Vertical Distance (m)', fontsize=14)
ax.set_xlim(0, max(x_positions) + 10000)  # Adjust x-axis limit for better visualization

# Adjust y-axis limit to provide space for the apogee
ax.set_ylim(0, max(y_positions) * 1.1)

ax.grid(True)

# Plot initial trajectory
missile, = ax.plot([], [], lw=2)

# Label for the phase
label = ax.text(0.5, 0.95, '', fontsize=14, transform=ax.transAxes, ha='center', va='top')

# Create animation
animation = FuncAnimation(fig, update, frames=len(x_positions), interval=50, init_func=init, blit=True)

plt.show()
