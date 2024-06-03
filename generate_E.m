clear
close
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Goal: Generate different figures
%Author: Qianyu
%Date: May 22nd, 2024
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Generate Waypoints of TU/e logo
%% 18 drones
% T = [-1.9,0,1.7;
%     -2.6,0,1.7;
%     -1.2,0,1.7;
%     -1.9,-0.2,1.2;
%     -1.9,-0.4,0.7;
%     -1.9,-0.6,0.2];
% U = [-0.7,-0.2,0.9;
%     -0.7,0,1.7;
%     0.6,0,1.7;
%     0.6,-0.2,0.9;
%     -0.3,-0.4,0.2;
%     0.3,-0.4,0.2];
% E = [1.2,-0.2,0.9;
%     1.5,0,1.5;
%     2.3,0,1.5;
%     1.35,-0.4,0.4;
%     1.9,-0.2,0.85;
%     1.9,-0.6,0.2;
%     2.6,-0.2,0.9];

%% Separate:
T = [-0.7,0,1.7; 
    0,0,1.7; 
    0.7,0,1.7; 
    0,-0.2,1.2; 
    0,-0.4,0.7; 
    0,-0.6, 0.2];
U = [-0.7,0,1.7;
    0.7,0,1.7;
    -0.6,-0.2,0.9;
    0.6,-0.2,0.9;
    -0.3,-0.4,0.2;
    0.3,-0.4,0.2];
E = [-0.7,-0.2,0.9;
    -0.4,0,1.5;
    0.4,0,1.5;
    0.7,-0.2,0.9;
    -0.55,-0.4,0.4;
    0,-0.2,0.85;
    0,-0.6,0.2];
initial_pos = [
    -0.5,1,0;
    0.5,1,0;
    -1,0,0;
    0,0,0;
    1,0,0;
    -0.5,-1,0;
    0.5,-1,0];

% Target position plot:
figure(1);
hold on;
plot3(T(:,1),T(:,2),T(:,3),'*');
plot3(U(:,1),U(:,2),U(:,3),'*');
plot3(E(:,1),E(:,2),E(:,3),'*');
plot3(initial_pos(:,1),initial_pos(:,2),initial_pos(:,3),'*',color='black');
grid on;
xlim([-1.2,1.2]);
xlabel('x');
ylabel('y');
zlabel('z');
ylim([-1.2,1.2]);
zlim([0,1.8]);

%% Draw trajectories:
for i=1:1:6
    mid(i,:)= [(T(i,1)+initial_pos(i,1))/2, (T(i,2)+initial_pos(i,2))/2, (T(i,3)+initial_pos(i,3))/2]; %middle point
    traj_T(:,:,i)=[initial_pos(i,:);mid(i,:);T(i,:)];
    mid_U(i,:)= [(T(i,1)+U(i,1))/2, (T(i,2)+U(i,2))/2, (T(i,3)+U(i,3))/2];
    traj_U(:,:,i)=[T(i,:);mid_U(i,:);U(i,:)];
    mid_E(i,:)= [(U(i,1)+E(i,1))/2, (U(i,2)+E(i,2))/2, (U(i,3)+E(i,3))/2];
    traj_E(:,:,i)=[U(i,:);mid_E(i,:);E(i,:)];
end
mid_E(7,:)= [(initial_pos(7,1)+E(7,1))/2, (initial_pos(7,2)+E(7,2))/2, (initial_pos(7,3)+E(7,3))/2];
traj_E(:,:,7)=[initial_pos(7,:);mid_E(7,:);E(7,:)];

% Trajectories plot:
figure(2);
grid on;
hold on;
plot3(traj_T(:,1,1),traj_T(:,2,1),traj_T(:,3,1),'*-',color='red');
plot3(traj_T(:,1,2),traj_T(:,2,2),traj_T(:,3,2),'*-',color='yellow');
plot3(traj_T(:,1,3),traj_T(:,2,3),traj_T(:,3,3),'*-',color='blue');
plot3(traj_T(:,1,4),traj_T(:,2,4),traj_T(:,3,4),'*-',color='green');
plot3(traj_T(:,1,5),traj_T(:,2,5),traj_T(:,3,5),'*-',color='cyan');
plot3(traj_T(:,1,6),traj_T(:,2,6),traj_T(:,3,6),'*-',color='magenta');

plot3(traj_U(:,1,1),traj_U(:,2,1),traj_U(:,3,1),'*-',color='red');
plot3(traj_U(:,1,2),traj_U(:,2,2),traj_U(:,3,2),'*-',color='yellow');
plot3(traj_U(:,1,3),traj_U(:,2,3),traj_U(:,3,3),'*-',color='blue');
plot3(traj_U(:,1,4),traj_U(:,2,4),traj_U(:,3,4),'*-',color='green');
plot3(traj_U(:,1,5),traj_U(:,2,5),traj_U(:,3,5),'*-',color='cyan');
plot3(traj_U(:,1,6),traj_U(:,2,6),traj_U(:,3,6),'*-',color='magenta');

plot3(traj_E(:,1,1),traj_E(:,2,1),traj_E(:,3,1),'*-',color='red');
plot3(traj_E(:,1,2),traj_E(:,2,2),traj_E(:,3,2),'*-',color='yellow');
plot3(traj_E(:,1,3),traj_E(:,2,3),traj_E(:,3,3),'*-',color='blue');
plot3(traj_E(:,1,4),traj_E(:,2,4),traj_E(:,3,4),'*-',color='green');
plot3(traj_E(:,1,5),traj_E(:,2,5),traj_E(:,3,5),'*-',color='cyan');
plot3(traj_E(:,1,6),traj_E(:,2,6),traj_E(:,3,6),'*-',color='magenta');
plot3(traj_E(:,1,7),traj_E(:,2,7),traj_E(:,3,7),'*-',color='black');
xlim([-1.2,1.2]);
xlabel('x');
ylabel('y');
zlabel('z');
ylim([-1.2,1.2]);
zlim([0,1.8]);
for i=1:1:7
    waypoints_orientation(:,:,i)=zeros(size(traj_U,1),3);
end
% Time_interval=[1.9273,1.2,0.5,0.7654,0.7654,0.7654,0.7654,0.7654,0.7654,0.5,1];     %Figure 6 time interval
% Time_interval=[1.05,0.71,0.62,0.7,0.56,0.56,0.7,0.62,0.71,1.05,1.05];   %Figure 8 time interval
Time_T = [3,3,3];

for i=1:length(Time_T)-1
    Time_of_Arrival(i+1)=Time_T(i+1)+sum(Time_T(1:i));
end
Time_of_Arrival(1)=Time_T(1);

for i=1:1:7
    waypoints(:,:,i)=[traj_E(:,:,i),waypoints_orientation(:,:,i)].';
end

%% Generate trajectory
numsamples=100;
% [q,qd,qdd,qddd,pp,timepoints,tsamples] = minjerkpolytraj(waypoints1,Time_of_Arrival,numsamples);
for i=1:1:7
    [q(:,:,i),qd(:,:,i),qdd(:,:,i),qddd(:,:,i),pp(:,:,i),timepoints(:,:,i),tsamples(:,:,i)] = minjerkpolytraj(waypoints(:,:,i),Time_of_Arrival,numsamples);
end

duration_time=Time_T;

for i=1:1:7
    position_coefficients_x(:,:,i) =pp(:,:,i).coefs(1:6:end,8:-1:1) ;
    position_coefficients_y(:,:,i) =pp(:,:,i).coefs(2:6:end,8:-1:1) ;
    position_coefficients_z(:,:,i) =pp(:,:,i).coefs(3:6:end,8:-1:1) ;
    orientation_coefficients_yaw(:,:,i)=pp(:,:,i).coefs(4:6:end,8:-1:1) ;
end

% figure(3)
% hold on
% plot3(q(1,:,1),q(2,:,1),q(3,:,1),'*');
% plot3(q(1,:,2),q(2,:,2),q(3,:,2),'*');
% plot3(q(1,:,3),q(2,:,3),q(3,:,3),'*');
% plot3(q(1,:,4),q(2,:,4),q(3,:,4),'*');
% plot3(q(1,:,5),q(2,:,5),q(3,:,5),'*');
% plot3(q(1,:,6),q(2,:,6),q(3,:,6),'*');
% grid on

%% Save coefficients
Coeffients1=[duration_time(1:end-1).',position_coefficients_x(:,:,1),position_coefficients_y(:,:,1),position_coefficients_z(:,:,1),orientation_coefficients_yaw(:,:,1)];
Create_coefficients_table(Coeffients1,'E_1.csv');

Coeffients2=[duration_time(1:end-1).',position_coefficients_x(:,:,2),position_coefficients_y(:,:,2),position_coefficients_z(:,:,2),orientation_coefficients_yaw(:,:,2)];
Create_coefficients_table(Coeffients2,'E_2.csv');

Coeffients3=[duration_time(1:end-1).',position_coefficients_x(:,:,3),position_coefficients_y(:,:,3),position_coefficients_z(:,:,3),orientation_coefficients_yaw(:,:,3)];
Create_coefficients_table(Coeffients3,'E_3.csv');

Coeffients4=[duration_time(1:end-1).',position_coefficients_x(:,:,4),position_coefficients_y(:,:,4),position_coefficients_z(:,:,4),orientation_coefficients_yaw(:,:,4)];
Create_coefficients_table(Coeffients4,'E_4.csv');

Coeffients5=[duration_time(1:end-1).',position_coefficients_x(:,:,5),position_coefficients_y(:,:,5),position_coefficients_z(:,:,5),orientation_coefficients_yaw(:,:,5)];
Create_coefficients_table(Coeffients5,'E_5.csv');

Coeffients6=[duration_time(1:end-1).',position_coefficients_x(:,:,6),position_coefficients_y(:,:,6),position_coefficients_z(:,:,6),orientation_coefficients_yaw(:,:,6)];
Create_coefficients_table(Coeffients6,'E_6.csv');

Coeffients7=[duration_time(1:end-1).',position_coefficients_x(:,:,7),position_coefficients_y(:,:,7),position_coefficients_z(:,:,7),orientation_coefficients_yaw(:,:,7)];
Create_coefficients_table(Coeffients7,'E_7.csv');




