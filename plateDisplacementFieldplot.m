% Plate displacement field plot (Question 2)

% Node coordinates (X, Y)
nodes = [
    1, 0.00, 0.00;
    2, 0.60, 0.00;
    3, 1.00, 0.00;
    4, 0.60, 0.40;
    5, 0.00, 0.40
];

% Vertical displacements v at each node (m)
% From Part 1(c): v1=0, v2=0, v3=-0.000080, v4=-0.000200, v5=0
v = [0;    % node 1
     0;    % node 2
    -8e-05; % node 3
    -2e-04; % node 4
     0];   % node 5

% Element connectivity (split Q4 into two triangles, plus the T3)
% Each row: [node_i node_j node_k]
tri = [
    1, 2, 4;   % first half of Q4 (nodes 1-2-4)
    1, 4, 5;   % second half of Q4 (nodes 1-4-5)
    2, 3, 4    % the single T3 element
];

% Extract X, Y for plotting
X = nodes(:,2);
Y = nodes(:,3);

% Create the trisurf plot
figure
h = trisurf(tri, X, Y, v*1000);   % multiply by 1000 to convert to mm
shading interp
colormap jet
colorbar
title('Vertical Displacement Field v(X,Y) (mm)')
xlabel('X (m)')
ylabel('Y (m)')
zlabel('v (mm)')
view(45,30)
axis tight
