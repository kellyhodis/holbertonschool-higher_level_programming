-- Create the database hbtn_0d_2 and the user user_0d_2.
CREATE IF NOT EXISTS USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_2@localhost;
CREATE IF NOT EXISTS hbtn_0d_2;
