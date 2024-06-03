clear
clc

% Parameters for generating a circular trajectory
radius = 0.75; % Radius of the circle
numWaypoints = 20; % Number of waypoints defining the circle

% Generate waypoints for a circle
phi = linspace((3*pi/2), 2 * pi + (3*pi/2), numWaypoints); %  Od zera do 2pi, tyle punktów ile numWaypoints
waypoints_position = radius * [cos(phi); sin(phi); zeros(1, numWaypoints)]'; % Just polar cordinates, x=...,y=...,z=0 matrix

% Shifting the circle to the left by 0.75 units
%waypoints_position(:,1) = waypoints_position(:,1) + 0.75;


% Just copied

waypoints_orientation = zeros(size(waypoints_position, 1), 3);
Time_interval = ones(1, numWaypoints) * 0.8; 


for i = 1:length(Time_interval)-1
    Time_of_Arrival(i+1) = Time_interval(i+1) + sum(Time_interval(1:i));
end
Time_of_Arrival(1) = Time_interval(1);
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

% Plotting the trajectory, I don't plot the two subplots they made
figure(1)
plot(waypoints_position(:,1), waypoints_position(:,2), 'r*-') 
hold on
plot(q(1,:), q(2,:), 'b-')
grid on

%% Save coefficients
fid = fopen( 'D2.csv', 'w' );
Coeffients=[duration_time(1:end-1).',position_coefficients_x,position_coefficients_y,position_coefficients_z,orientation_coefficients_yaw];
Create_coefficients_table(Coeffients);