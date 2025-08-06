import matplotlib.pyplot as plt

# Node coordinates
coords = {
    1: (0.0, 0.0),
    2: (0.6, 0.0),
    3: (1.0, 0.0),
    4: (0.6, 0.4),
    5: (0.0, 0.4)
}

# Displacements (in meters)
displacements = {
    1: (0.0, 0.0),
    2: (0.000120, 0.0),
    3: (0.000230, -0.000080),
    4: (0.000150, -0.000200),
    5: (0.0, 0.0)
}

# Scale factor for visibility
alpha = 100

# Element connectivity
elements = [
    [1, 2, 4, 5, 1],  # Q4 (closed loop)
    [2, 3, 4, 2]      # T3 (closed loop)
]

# Plot original and deformed shapes
plt.figure()
for elem in elements:
    # Original mesh
    X_orig = [coords[n][0] for n in elem]
    Y_orig = [coords[n][1] for n in elem]
    plt.plot(X_orig, Y_orig, marker='o', linestyle='-')
    
    # Deformed mesh
    X_def = [coords[n][0] + alpha * displacements[n][0] for n in elem]
    Y_def = [coords[n][1] + alpha * displacements[n][1] for n in elem]
    plt.plot(X_def, Y_def, marker='o', linestyle='--')

plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Original (solid) and Deformed (dashed) Mesh (scaled 100×)')
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()
