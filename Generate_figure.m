clear
close
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Goal: Generate different figures
%Author: Ming
%Date: May 26th, 2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Generate Waypoints of Figure 6
T = [-0.7,0,2.0; 
    0,0,2.0; 
    0.7,0,2.0; 
    0,-0.2,1.4; 
    0,-0.4,0.8; 
    0,-0.6, 0.2];
U = [-0.7,-0.2,0.9;
    -0.7,0,1.8;
    0.6,0,1.8;
    0.6,-0.2,0.9;
    -0.3,-0.4,0.2;
    0.3,-0.4,0.2];
E = [-0.7,-0.2,1.1;
    -0.4,0,1.7;
    0.4,0,1.7;
    0.7,-0.2,1.1;
    -0.55,-0.4,0.6;
    0,-0.2,1.05;
    0,-0.6,0.4];
initial_pos = [
    -0.5,1,0;
    0.5,1,0;
    -1,0,0;
    0,0,0;
    1,0,0;
    -0.5,-1,0;
    0.5,-1,0];

traj_T1 = [initial_pos(1,:);T(1,:)];
traj_T2 = [initial_pos(2,:);T(2,:)];
traj_T3 = [initial_pos(3,:);T(3,:)];
traj_T4 = [initial_pos(4,:);T(4,:)];
traj_T5 = [initial_pos(5,:);T(5,:)];
traj_T6 = [initial_pos(6,:);T(6,:)];

figure(1);
plot3(T(:,1),T(:,2),T(:,3),'*');
hold on;
plot3(U(:,1),U(:,2),U(:,3),'*');
plot3(E(:,1),E(:,2),E(:,3),'*');
plot3(initial_pos(:,1),initial_pos(:,2),initial_pos(:,3),'*');
grid on;

figure(2);
grid on;
hold on;
plot3(traj_T1(:,1),traj_T1(:,2),traj_T1(:,3),'*-',color='red');
plot3(traj_T2(:,1),traj_T2(:,2),traj_T2(:,3),'*-',color='yellow');
plot3(traj_T3(:,1),traj_T3(:,2),traj_T3(:,3),'*-',color='blue');
plot3(traj_T4(:,1),traj_T4(:,2),traj_T4(:,3),'*-',color='green');
plot3(traj_T5(:,1),traj_T5(:,2),traj_T5(:,3),'*-',color='cyan');
plot3(traj_T6(:,1),traj_T6(:,2),traj_T6(:,3),'*-',color='magenta');

waypoints_orientation1 =zeros(size(traj_T1,1),3);
waypoints_orientation2 =zeros(size(traj_T2,1),3);
waypoints_orientation3 =zeros(size(traj_T3,1),3);
waypoints_orientation4 =zeros(size(traj_T4,1),3);
waypoints_orientation5 =zeros(size(traj_T5,1),3);
waypoints_orientation6 =zeros(size(traj_T6,1),3);


% Time_interval=[1.9273,1.2,0.5,0.7654,0.7654,0.7654,0.7654,0.7654,0.7654,0.5,1];     %Figure 6 time interval
% Time_interval=[1.05,0.71,0.62,0.7,0.56,0.56,0.7,0.62,0.71,1.05,1.05];   %Figure 8 time interval
Time_T = [3,3];

for i=1:length(Time_T)-1
    Time_of_Arrival(i+1)=Time_T(i+1)+sum(Time_T(1:i));
end
Time_of_Arrival(1)=Time_T(1);
waypoints1=[traj_T1,waypoints_orientation1].';
waypoints2=[traj_T2,waypoints_orientation2].';
waypoints3=[traj_T3,waypoints_orientation3].';
waypoints4=[traj_T4,waypoints_orientation4].';
waypoints5=[traj_T5,waypoints_orientation5].';
waypoints6=[traj_T6,waypoints_orientation6].';

%% Generate trajectory
numsamples=100;
% [q,qd,qdd,qddd,pp,timepoints,tsamples] = minjerkpolytraj(waypoints1,Time_of_Arrival,numsamples);
[q1,qd1,qdd1,qddd1,pp1,timepoints1,tsamples1] = minjerkpolytraj(waypoints1,Time_of_Arrival,numsamples);
[q2,qd2,qdd2,qddd2,pp2,timepoints2,tsamples2] = minjerkpolytraj(waypoints2,Time_of_Arrival,numsamples);
[q3,qd3,qdd3,qddd3,pp3,timepoints3,tsamples3] = minjerkpolytraj(waypoints3,Time_of_Arrival,numsamples);
[q4,qd4,qdd4,qddd4,pp4,timepoints4,tsamples4] = minjerkpolytraj(waypoints4,Time_of_Arrival,numsamples);
[q5,qd5,qdd5,qddd5,pp5,timepoints5,tsamples5] = minjerkpolytraj(waypoints5,Time_of_Arrival,numsamples);
[q6,qd6,qdd6,qddd6,pp6,timepoints6,tsamples6] = minjerkpolytraj(waypoints6,Time_of_Arrival,numsamples);

duration_time=Time_T;
% position_coefficients_x1 =pp.coefs(1:6:end,8:-1:1) ;
position_coefficients_x1 =pp1.coefs(1:6:end,8:-1:1) ;
position_coefficients_y1 =pp1.coefs(2:6:end,8:-1:1) ;
position_coefficients_z1 =pp1.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw1=pp1.coefs(4:6:end,8:-1:1) ;

position_coefficients_x2 =pp2.coefs(1:6:end,8:-1:1) ;
position_coefficients_y2 =pp2.coefs(2:6:end,8:-1:1) ;
position_coefficients_z2 =pp2.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw2=pp2.coefs(4:6:end,8:-1:1) ;

position_coefficients_x3 =pp3.coefs(1:6:end,8:-1:1) ;
position_coefficients_y3 =pp3.coefs(2:6:end,8:-1:1) ;
position_coefficients_z3 =pp3.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw3=pp3.coefs(4:6:end,8:-1:1) ;

position_coefficients_x4 =pp4.coefs(1:6:end,8:-1:1) ;
position_coefficients_y4 =pp4.coefs(2:6:end,8:-1:1) ;
position_coefficients_z4 =pp4.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw4=pp4.coefs(4:6:end,8:-1:1) ;

position_coefficients_x5 =pp5.coefs(1:6:end,8:-1:1) ;
position_coefficients_y5 =pp5.coefs(2:6:end,8:-1:1) ;
position_coefficients_z5 =pp5.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw5=pp5.coefs(4:6:end,8:-1:1) ;

position_coefficients_x6 =pp6.coefs(1:6:end,8:-1:1) ;
position_coefficients_y6 =pp6.coefs(2:6:end,8:-1:1) ;
position_coefficients_z6 =pp6.coefs(3:6:end,8:-1:1) ;
orientation_coefficients_yaw6=pp6.coefs(4:6:end,8:-1:1) ;

figure(3)
hold on;
plot3(q1(1,:),q1(2,:),q1(3,:));
plot3(q2(1,:),q2(2,:),q2(3,:));
plot3(q3(1,:),q3(2,:),q3(3,:));
plot3(q4(1,:),q4(2,:),q4(3,:));
plot3(q5(1,:),q5(2,:),q5(3,:));
plot3(q6(1,:),q6(2,:),q6(3,:));
grid on

%% Save coefficients
% fid = fopen( 'T_1.csv', 'w' );
Coeffients=[duration_time(1:end-1).',position_coefficients_x1,position_coefficients_y1,position_coefficients_z1,orientation_coefficients_yaw1];
Create_coefficients_table(Coeffients);
