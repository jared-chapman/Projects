sprite_index = spr_turrets; 
image_index = 2;
image_speed = 0;
rotateSpeed = 5;

script_execute(scr_placeTurret);                            //updates turret's position
script_execute(scr_rotate);                                 //rotates the turret toward the mouse at variable speed
script_execute(scr_shoot, mb_left, "left", obj_gravBomb);   //handles fire rate and bullet creation
script_execute(scr_shoot, mb_right, "right", obj_gravBomb);


