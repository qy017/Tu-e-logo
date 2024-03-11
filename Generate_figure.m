clear
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Goal: Generate different figures
%Author: Ming
%Date: May 26th, 2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Generate Waypoints of Figure 6
waypoints_position=[-2.5,0,0;
    -sqrt(2)/2,-sqrt(2)/2,0;
    0,-1,0;
    sqrt(2)/2,-sqrt(2)/2,0;
    1,0,0;
    sqrt(2)/2,sqrt(2)/2,0;
    0,1,0;
    -sqrt(2)/2,sqrt(2)/2,0;
    -1,0,0;
    -sqrt(2)/2,-sqrt(2)/2,0;
    0,0,0];
 
% % Generate Waypoints of Figure 8
% waypoints_position=[0,0,0;
%                     0.395637,-0.363356,0;
%                     0.922494,-0.356094,0;
%                     0.922494,0.363356,0;
%                     0.395637,0.363356,0;
%                     0,0,0;
%                     -0.395637,-0.363356,0;
%                     -0.922494,-0.363356,0;
%                     -0.922494,0.356094,0;
%                     -0.395637,0.363356,0;
%                     0,0,0;];


waypoints_orientation =zeros(size(waypoints_position,1),3);
Time_interval=[1.9273,1.2,0.5,0.7654,0.7654,0.7654,0.7654,0.7654,0.7654,0.5,1];     %Figure 6 time interval
% Time_interval=[1.05,0.71,0.62,0.7,0.56,0.56,0.7,0.62,0.71,1.05,1.05];             %Figure 8 time interval


for i=1:length(Time_interval)-1
    Time_of_Arrival(i+1)=Time_interval(i+1)+sum(Time_interval(1:i));
end
Time_of_Arrival(1)=Time_interval(1);
waypoints=[waypoints_position,waypoints_orientation].';

%% Generate trajectory
numsamples=100;
[q,qd,qdd,qddd,pp,timepoints,tsamples] = minjerkpolytraj(waypoints,Time_of_Arrival,numsamples);

duration_time=Time_interval;
position_coefficients_x =pp.coefs(1:6:end,8:-1:1) ;
position_coefficients_y =pp.coefs(2:6:end,8:-1:1) ;
position_coefficients_z =pp.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw=pp.coefs(4:6:end,8:-1:1) ;
figure(1)
subplot(1,2,1)
plot(qd(1,:))
subplot(1,2,2)
plot(qd(2,:))
figure(2)
subplot(1,2,1)
plot(qdd(1,:))
subplot(1,2,2)
plot(qdd(2,:))
figure(3)
plot(waypoints_position(:,1),waypoints_position(:,2),'r*-')
hold on
plot(q(1,:),q(2,:),'b-')
grid on


%% Save coefficients
fid = fopen( 'figure6_final.csv', 'w' );
Coeffients=[duration_time(1:end-1).',position_coefficients_x,position_coefficients_y,position_coefficients_z,orientation_coefficients_yaw];
Create_coefficients_table(Coeffients);
