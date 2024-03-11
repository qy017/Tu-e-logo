function Create_coefficients_table(Coeffients)
Titile = char({'duration','x^0','x^1','x^2','x^3','x^4','x^5','x^6','x^7','y^0','y^1','y^2','y^3','y^4','y^5','y^6','y^7','z^0','z^1','z^2','z^3','z^4','z^5','z^6','z^7','yaw^0','yaw^1','yaw^2','yaw^3','yaw^4','yaw^5','yaw^6','yaw^7'});

%% Create table
fid = fopen( 'figure6_final.csv', 'w' );
% Build titile of the table
for i_column = 1 : size( Coeffients,2 )
    if i_column<size( Coeffients,2 )
        fprintf( fid, '%s,', Titile(i_column,:) );
    else
        fprintf( fid, '%s\n', Titile(i_column,:) );
    end
end

% Write coeffients
for i_row=1 : size( Coeffients,1 )
    for i_column = 1 : size( Coeffients,2 )
        if i_column<size( Coeffients,2 )
            fprintf( fid, '%f,', Coeffients(i_row,i_column) );
        else
            fprintf( fid, '%f\n', Coeffients(i_row,i_column) );
        end
    end
end
fclose( fid );
end

