//Calculates and updates position
if instance_exists(obj_player){
    x=obj_player.x+lengthdir_x(len,obj_player.image_angle+dir);
    y=obj_player.y+lengthdir_y(len,obj_player.image_angle+dir);
}   

script_execute(scr_rotate);

sprite_index = spr_turrets;
image_index = 3;
image_speed = 0;
