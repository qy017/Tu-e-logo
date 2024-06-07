clear
clc

%% Parameters for generating a helical trajectory
radius = 0.5; % Radius of the helix
numWaypoints = 40; % Number of waypoints 

% Generate waypoints for a helix
t = linspace(0, 4 * pi, numWaypoints); % Two circles
waypoints_position = [radius * cos(t); radius * sin(t); t / (3 * pi)]'; % x, y, z coordinates

% Generate orientation waypoints (zero orientation)
waypoints_orientation = zeros(size(waypoints_position, 1), 3);
Time_interval = ones(1, numWaypoints) * 2; % Time interval between waypoints

% Calculate time of arrival for each waypoint
Time_of_Arrival = cumsum([0, Time_interval(1:end-1)]);

% Combine position and orientation into waypoints matrix
waypoints = [waypoints_position, waypoints_orientation].';

%% Generate trajectory
numsamples = 100;
[q, qd, qdd, qddd, pp, timepoints, tsamples] = minjerkpolytraj(waypoints, Time_of_Arrival, numsamples);

% Extract coefficients for position and orientation
duration_time = Time_interval;
position_coefficients_x = pp.coefs(1:6:end, 8:-1:1);
position_coefficients_y = pp.coefs(2:6:end, 8:-1:1);
position_coefficients_z = pp.coefs(3:6:end, 8:-1:1);
orientation_coefficients_yaw = pp.coefs(4:6:end, 8:-1:1);

% Plotting the trajectory
figure(1)
plot3(waypoints_position(:,1), waypoints_position(:,2), waypoints_position(:,3), 'r*-') 
hold on
plot3(q(1,:), q(2,:), q(3,:), 'b-')
xlabel('x')
ylabel('y')
zlabel('z')
grid on

% Save coefficients 
fid = fopen('helix4.csv', 'w');
Coefficients = [duration_time(1:end-1).', position_coefficients_x, position_coefficients_y, position_coefficients_z, orientation_coefficients_yaw];
Create_coefficients_table_helix(Coefficients);
% 
